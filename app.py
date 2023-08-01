"""
ReceiptStash: Flask web application for managing receipts.

This application allows users to upload receipts, view, edit, delete them.
Receipts are stored in an SQLite database, and the application provides the option to download receipt data in CSV format.

Modules:
    - flask: The Flask web framework.
    - flask_table: A package for generating HTML tables in Flask.
    - datetime: Date and time-related functionalities.
    - os: Operating system-related functionalities.
    - ocr: Optical Character Recognition (OCR) module for text extraction from images.
    - receipt_db: Module for managing the SQLite database for receipts.
    - date_utils: Utility functions for working with date formats.

Classes:
    - ReceiptTable: A subclass of FlaskTable used to display receipt data in an HTML table.

Functions:
    - home(): Redirects users to the 'application' route.
    - application(): Handles the main application route and displays receipts in a table.
    - edit_receipt(receipt_id): Handles the 'edit' route for editing a specific receipt.
    - delete_receipt(receipt_id): Handles the 'delete' route for deleting a specific receipt.
    - download_table(): Generates a CSV file and allows users to download all receipts.

Helper Functions:
    - convert_date_format(date_str): Converts a date from 'YYYY-MM-DD' to 'DD/MM/YYYY' format.
    - filter_receipts_by_date(receipts, start_date, end_date): Filters receipts based on the selected date range.
"""


from flask import Flask, render_template, request, redirect, url_for, make_response, flash
from flask_table import Table, Col, LinkCol
from datetime import datetime
import os
from ocr import OCR
from receipt_db import Receipt, ReceiptDB
from date_utils import DateConverter

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db = ReceiptDB('receipts.db')
db.create_table()

class ReceiptTable(Table):
    # id = Col('Receipt ID')
    
    vendor_name = Col('Vendor Name', allow_sort=True)
    date = Col('Date', allow_sort=True)
    total_amount = Col('Total Amount')
    edit = LinkCol('Edit', 'edit_receipt', url_kwargs=dict(receipt_id='id'), attr='id', allow_sort=False, anchor_attrs={'class': 'btn btn-secondary'})
    delete = LinkCol('Delete', 'delete_receipt', url_kwargs=dict(receipt_id='id'), attr='id', allow_sort=False, anchor_attrs={'class': 'btn btn-danger', 'onclick': 'return confirmDelete(\'id\')'})

    def sort_url(self, col_key, reverse=False):
        if reverse:
            direction = 'desc'
        else:
            direction = 'asc'
        return url_for('application', sort=col_key, direction=direction)

    # Add Bootstrap class attributes to table elements
    classes = ['table', 'table-striped', 'table-bordered', 'table-hover']

@app.route('/')
def home():
    return redirect(url_for('application'))


@app.route('/app', methods=['GET', 'POST'])
def application():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded', 400

        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        else:
            print("I am after")
            file_bytes = file.read()  # Read the file content as bytes

            extracted_text = OCR.extract_text_from_bytes(file_bytes)
            total_amount = OCR.extract_total_amount(extracted_text)
            vendor_name = OCR.extract_vendor_name(extracted_text)
            date = OCR.extract_date(extracted_text)

            if(not(extracted_text or total_amount or vendor_name)):
                flash('Image is not Supported')
            else:    
                receipt = Receipt({
                    0: None,
                    1: vendor_name,
                    2: date,
                    3: total_amount
                })
                db.insert_receipt(receipt)
                # Clear the form data to prevent resubmission on refresh
                flash('Upload successful')

            return redirect(request.url)

    # Retrieve the start and end dates from the query parameters
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')

    # Convert the date strings to datetime objects
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date() if start_date_str else None
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date() if end_date_str else None

    receipts = db.get_all_receipts()

    # Filter the receipts based on the selected date range
    filtered_receipts = filter_receipts_by_date(receipts, start_date, end_date)

    table = ReceiptTable(filtered_receipts)  # Pass the filtered receipts to the table object
    table.border = True  # Optionally, set a border for the table

    return render_template('app.html', table=table, start_date=start_date_str, end_date=end_date_str)


@app.route('/edit/<int:receipt_id>', methods=['GET', 'POST'])
def edit_receipt(receipt_id):
    if request.method == 'POST':
        vendor_name = request.form.get('vendor_name')
        date = request.form.get('date')
        total_amount = request.form.get('total_amount')

        data = [receipt_id, vendor_name, date, total_amount]
        receipt = Receipt(data)

        db.update_receipt(receipt_id, vendor_name, date, total_amount)

        return redirect(url_for('application'))

    receipt = db.get_receipt(receipt_id)
    return render_template('edit.html', receipt=receipt)


@app.route('/delete/<int:receipt_id>', methods=['GET', 'POST'])
def delete_receipt(receipt_id):
    if request.method == 'GET':
        db.delete_receipt(receipt_id)
        return redirect(url_for('application'))


@app.route('/download/table')
def download_table():
    receipts = db.get_all_receipts()
    if not receipts:
        return 'No receipts found', 404

    # Generate the table data as a CSV file
    csv_data = "Receipt ID,Image Path,Vendor Name,Date,Total Amount\n"
    for receipt in receipts:
        csv_data += "{},{},{},{}\n".format(receipt.id, receipt.vendor_name, receipt.date, receipt.total_amount)

    # Create the response with the CSV data
    response = make_response(csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=receipts.csv"
    response.headers["Content-type"] = "text/csv"

    return response

from datetime import datetime

def convert_date_format(date_str):
    # Convert date from 'YYYY-MM-DD' to 'DD/MM/YYYY' format
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    formatted_date = date_obj.strftime('%Y-%m-%d')
    return formatted_date

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

if __name__ == '__main__':
    app.run(port=5001, debug=True)