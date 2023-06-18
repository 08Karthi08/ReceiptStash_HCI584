from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os
from ocr import OCR
from receipt_db import Receipt, ReceiptDB

app = Flask(__name__)
app.secret_key = 'your_secret_key'

db = ReceiptDB('receipts.db')
db.create_table()

@app.route('/')
def home():
    return redirect(url_for('upload'))

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # print("I am here");
        # if 'receipt' not in request.files:
        #     return redirect(request.url)

        # receipt_file = request.files['receipt']
        # print("I am here2");
        # if receipt_file.filename == '':
        #     return redirect(request.url)

        if 'file' not in request.files:
            return 'No file uploaded', 400

        file = request.files['file']
        if file.filename == '':
            return 'No file selected', 400
        
        image_path = os.path.join('uploads', file.filename)
        file.save(image_path)

        extracted_text = OCR.extract_text(image_path)
        print(extracted_text);
        total_amount = OCR.extract_total_amount(extracted_text)
        vendor_name = OCR.extract_vendor_name(extracted_text)
        date = OCR.extract_date(extracted_text)

        receipt = Receipt({
            'image_path': image_path,
            'vendor_name': vendor_name,
            'date': date,
            'total_amount': total_amount
        })
        db.insert_receipt(receipt)

        return 'Receipt uploaded successfully!'

    return render_template('upload.html')

@app.route('/receipts')
def receipts():
    receipts1 = db.get_all_receipts()
    print(receipts1)
    return render_template('receipts.html', receipts=receipts1)

if __name__ == '__main__':
    app.run(debug=True)