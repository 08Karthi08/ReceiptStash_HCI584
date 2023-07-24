# ReceiptStash
ReceiptStash is a web application that allows you to upload and organize your receipts. It uses Flask as the backend framework and integrates Tesseract OCR for extracting text from uploaded receipt images.

# Prerequisites
Make sure you have the following prerequisites installed on your system:

Python 3.x: [Download Python](https://www.python.org/downloads/)

Tesseract OCR: [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)
# Requirement.txt
Flask==2.1.1

flask-table==0.5.0

pytesseract==0.3.8

Pillow==8.3.2

# Bugs

1. Vendor name is printed differently on different receipts. Most of them use their logo. It's difficult to extract from the receipts.- Error fixed


