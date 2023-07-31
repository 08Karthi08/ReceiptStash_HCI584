# ReceiptStash
ReceiptStash is a web application that allows you to upload and organize your receipts. It uses Flask as the backend framework and integrates Tesseract OCR for extracting text from uploaded receipt images.

# Prerequisites
Make sure you have the following prerequisites installed on your system:

Python 3.x: [Download Python](https://www.python.org/downloads/)

Tesseract OCR: [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)

# Requirement.txt
`Flask==2.1.1`

`flask-table==0.5.0`

`pytesseract==0.3.8`

`Pillow==8.3.2`
# Installation
1. Clone the repository:
  `git clone (https://github.com/08Karthi08/ReceiptStash_HCI584.git)`

1. Create a virtual environment (optional but recommended):
`python3 -m venv venv`

1. Activate the virtual environment:
   - On Windows:
`venv\Scripts\activate`
   - On macOS and Linux:
`source venv/bin/activate`

4. Install the project dependencies:
`pip install -r requirements.txt`

5. Configuration (skip) Open the app.py file and set a secret key for session management. Modify the following line:
app.secret_key = 'your_secret_key'

6. Usage:
   
- Start the Flask development server:
`python3 app.py`

- Open your web browser and go to 
http://localhost:5000.

- You should see the homepage of the ReceiptStash web application.

Contributing Contributions to the project are welcome! If you find any issues or have any suggestions, please create a new issue or submit a pull request.

License This project is licensed under the MIT License.

Please replace your-username in the URLs with your actual GitHub username when creating the repository.






