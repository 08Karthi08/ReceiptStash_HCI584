# Import necessary modules and libraries
from flask import Flask, render_template, request, redirect, url_for, make_response, flash
from flask_table import Table, Col, LinkCol
from datetime import datetime
import os
from ocr import OCR
from receipt_db import Receipt, ReceiptDB
from date_utils import DateConverter

# Create a Flask web application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set the secret key for session security

# Create a database instance and create the table if it doesn't exist
db = ReceiptDB('receipts.db')
db.create_table()

# Define the ReceiptTable class for displaying receipts in a table format
class ReceiptTable(Table):
    # Define table columns and attributes
    """A table class for displaying receipts in a tabular format."""
    
    vendor_name = Col('Vendor Name', allow_sort=True)
    date = Col('Date', allow_sort=True)
    total_amount = Col('Total Amount')
    edit = LinkCol('Edit', 'edit_receipt', url_kwargs=dict(receipt_id='id'), attr='id', allow_sort=False, anchor_attrs={'class': 'btn btn-secondary'})
    delete = LinkCol('Delete', 'delete_receipt', url_kwargs=dict(receipt_id='id'), attr='id', allow_sort=False, anchor_attrs={'class': 'btn btn-danger', 'onclick': 'return confirmDelete(\'id\')'})

    # Define a method to generate URLs for sorting columns
    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction = 'desc'
        else:
            direction = 'asc'
        return url_for('application', sort=col_key, direction=direction)

    # Add Bootstrap class attributes to table elements
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover']

# Define the route for the home page (root URL)
@app.route('/')
def home():
    return redirect(url_for('application'))  # Redirect to the main application page
 """Redirect to the main application page."""
 
# Define the route for the main application page
@app.route('/app', methods=['GET', 'POST'])
def application():
    # Handling file uploads and the OCR processing when the form is submitted
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400

        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        else:
            file_bytes = file.read()  # Read the file content as bytes

            # Extract text, vendor name, date, and total amount using OCR
            extracted_text = OCR.extract_text_from_bytes(file_bytes)
            total_amount = OCR.extract_total_amount(extracted_text)
            vendor_name = OCR.extract_vendor_name(extracted_text)
            date = OCR.extract_date(extracted_text)

            # Display a flash message if OCR extraction fails
            if not (extracted_text or total_amount or vendor_name):
                flash('Image is not Supported')
            else:
                # Create a Receipt object and insert it into the database
                receipt = Receipt({
                    0: None,
                    1: vendor_name,
                    2: date,
                    3: total_amount
                })
                db.insert_receipt(receipt)
                flash('Upload successful')  # Display a success flash message

            return redirect(request.url)  # Redirect back to the application page

    # Retrieve the start and end dates from the query parameters
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    # Convert the date strings to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date() if start_date_str else None
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date() if end_date_str else None

    receipts = db.get_all_receipts()

    # Filter the receipts based on the selected date range
    filtered_receipts = filter_receipts_by_date(receipts, start_date, end_date)

    # Create a ReceiptTable object with the filtered receipts
    table = ReceiptTable(filtered_receipts)
    table.border = True  # Optionally, set a border for the table

    # Render the application page with the table and date filters
    return render_template('app.html', table=table, start_date=start_date_str, end_date=end_date_str)

# Define the route for editing a receipt
@app.route('/edit/<int:receipt_id>', methods=['GET', 'POST'])
def edit_receipt(receipt_id):
    if request.method == 'POST':
        # Update receipt information based on the submitted form data
        vendor_name = request.form.get('vendor_name')
        date = request.form.get('date')
        total_amount = request.form.get('total_amount')

        data = [receipt_id, vendor_name, date, total_amount]
        receipt = Receipt(data)

        db.update_receipt(receipt_id, vendor_name, date, total_amount)

        return redirect(url_for('application'))  # Redirect back to the application page

    receipt = db.get_receipt(receipt_id)
    return render_template('edit.html', receipt=receipt)  # Render the edit receipt page

# Define the route for deleting a receipt
@app.route('/delete/<int:receipt_id>', methods=['GET', 'POST'])
def delete_receipt(receipt_id):
    if request.method == 'GET':
        db.delete_receipt(receipt_id)  # Delete the receipt from the database
        return redirect(url_for('application'))  # Redirect back to the application page

# Define the route for downloading the receipt table as a CSV file
@app.route('/download/table')
def download_table():
    receipts = db.get_all_receipts()
    if not receipts:
        return 'No receipts found', 404

    # Generate the table data as a CSV file
    csv_data = "Receipt ID,Vendor Name,Date,Total Amount\n"
    for receipt in receipts:
        csv_data += "{},{},{},{}\n".format(receipt.id, receipt.vendor_name, receipt.date, receipt.total_amount)

    # Create the response with the CSV data
    response = make_response(csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=receipts.csv"
    response.headers["Content-type"] = "text/csv"

    return response

# Helper function to convert date format from 'YYYY-MM-DD' to 'DD/MM/YYYY'
def convert_date_format(date_str):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    formatted_date = date_obj.strftime('%Y-%m-%d')
    return formatted_date

# Helper function to filter receipts by date range
def filter_receipts_by_date(receipts, start_date, end_date):
    start_date = DateConverter.convert_to_date(start_date)
    end_date = DateConverter.convert_to_date(end_date)

    filtered_receipts = []
    for receipt in receipts:
        receipt_date = DateConverter.convert_to_date(receipt.date)
        if start_date and end_date:
            if start_date <= receipt_date <= end_date:
                filtered_receipts.append(receipt)
        elif start_date:
            if start_date <= receipt_date:
                filtered_receipts.append(receipt)
        elif end_date:
            if receipt_date <= end_date:
                filtered_receipts.append(receipt)
        else:
            filtered_receipts.append(receipt)

    return filtered_receipts

# Run the Flask application
if __name__ == '__main__':
    app.run(port=5001, debug=True)