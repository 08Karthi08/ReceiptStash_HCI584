# ReceiptStash
ReceiptStash is a web application that allows you to upload and organize your receipts. The application enables users to upload, store, filter, edit, delete, and download their receipts digitally, making it easy to track expenses and manage financial records. It uses Flask as the backend framework and integrates Tesseract OCR for extracting text from uploaded receipt images.

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
http://127.0.0.1:5001

![Screenshot 2023-08-04 at 11 38 12 AM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/4fc0ef74-d347-4a1c-987e-d666a06e2b42)


   + You should see the homepage of the ReceiptStash web application.

## User Interface
 * **Dashboard**
 ![Screenshot 2023-08-04 at 1 03 48 PM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/51ef03df-9e14-412e-82b3-4af6fe2ce00c)

 * **Error message when you upload images that are not receipts:**
![Screenshot 2023-08-04 at 1 04 29 PM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/13a73de5-d756-464e-8b01-b834fd5ec950)

  * **Filter Receipts by date:** 
![Screenshot 2023-07-31 at 3 28 47 PM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/9c70f4b2-e082-470c-8bde-532c1b3d0da3)
  * **Download CSV file:**
  
![Screenshot 2023-07-31 at 3 25 11 PM](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/2a88c110-640d-4158-b117-0621a76f1e29)








