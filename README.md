# ReceiptStash
ReceiptStash is a web application that allows you to upload and organize your receipts. The application enables users to upload, store, filter, and download their receipts digitally, making it easy to track expenses and manage financial records. It uses Flask as the backend framework and integrates Tesseract OCR for extracting text from uploaded receipt images.

## Prerequisites
Make sure you have the following prerequisites installed on your system:

Python 3.x: [Download Python](https://www.python.org/downloads/)

Tesseract OCR: [Tesseract OCR GitHub](https://github.com/tesseract-ocr/tesseract)

## Requirement.txt
`Flask>=2.1.1`

`flask-table>=0.5.0`

`pytesseract>=0.3.8`

`Pillow>=8.3.2`
## Installation
1. **Clone the repository:**
  `git clone (https://github.com/08Karthi08/ReceiptStash_HCI584.git)`

1. **Change into the project directory:**
   `cd ReceiptStash_HCI584`

1. **Create a virtual environment (optional but recommended):**
`python3 -m venv venv`

1. **Activate the virtual environment:**
   - On Windows:
`venv\Scripts\activate`
   - On macOS and Linux:
`source venv/bin/activate`

4. **Install the project dependencies:**
`pip install -r requirements.txt`

5. **Configuration (skip) Open the app.py file and set a secret key for session management. Modify the following line:**
`app.secret_key = 'your_secret_key'`

6. **Usage:**
   
   + Start the Flask development server:
`python3 app.py`

   + Open your web browser and go to 
http://localhost:5000.

   + You should see the homepage of the ReceiptStash web application.

## User Interface
 * **Dashboard**
  ![Screenshot 2023-07-31 at 3 23 31 PM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/d105c339-b97f-4fc6-92c9-e7828c6ba97d)
 * **Error message when you upload images that are not receipts:**
![Screenshot 2023-07-31 at 3 27 00 PM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/e2317a69-43af-4f92-aa77-5c341d059e6f)
  * **Filter Receipts by date:** 
![Screenshot 2023-07-31 at 3 28 47 PM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/9c70f4b2-e082-470c-8bde-532c1b3d0da3)
  * **Download CSV file:**
  
![Screenshot 2023-07-31 at 3 25 11 PM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/2a88c110-640d-4158-b117-0621a76f1e29)








