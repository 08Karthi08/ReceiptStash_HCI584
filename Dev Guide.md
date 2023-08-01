# ReceiptStash - Developer's Guide

## Overview
Welcome to the ReceiptStash Developer's Guide! This document serves as a comprehensive resource for developers who want to contribute to or understand the inner workings of ReceiptStash, a web application for uploading and organizing receipts. It provides an overview of the software, installation, and deployment instructions, user interaction flow, known issues, and more.

## Installation and Deployment

Here are additional considerations for deployment and administration:

Ensure the correct versions of dependencies are installed by checking the requirements.txt file.

Set the SECRET_KEY environment variable to ensure session security if deploying the application in a production environment.

Configure the database connection string in the ReceiptDB class constructor (receipt_db.py) to match the desired deployment environment.

## User Interaction and Flow
The user interaction flow in ReceiptStash involves the following steps:

1. The user visits the application URL and is redirected to the main application page.
2. The user can upload receipt images on the main application page using the "Upload Receipt" button.
3. After the user selects an image, the application processes it using OCR to extract text, including vendor name, date, and total amount.
4. If the OCR extraction succeeds, the application stores the extracted data in the database, displaying a success message.
5. The user can filter receipts by date range using the date filters provided on the main application page.
6. The "View Receipts" table displays the filtered receipts, and the user can edit or delete individual receipts.
7. User can download the receipts to a CSV file using the download button.

## Code Structure
The main Flask application (app.py) is responsible for handling user requests and rendering templates. The project is organized into several modules:

- `app.py: `Contains the main Flask application and routes.
- `ocr.py: `Implements Optical Character Recognition (OCR) functions to extract text from receipt images.
- `receipt_db.py: `Provides functions for interacting with the SQLite database to manage receipt data.
- `date_utils.py: `Includes utility functions for handling data-related operations.

### Modules:
    * flask: The Flask web framework.
    * flask_table: A package for generating HTML tables in Flask.
    * datetime: Date and time-related functionalities.
    * os: Operating system-related functionalities.
    * ocr: Optical Character Recognition (OCR) module for text extraction from images.
    * receipt_db: Module for managing the SQLite database for receipts.
    * date_utils: Utility functions for working with date formats.

### Classes:
    * ReceiptTable: A subclass of FlaskTable used to display receipt data in an HTML table.

### Functions:
    * home(): Redirects users to the 'application' route.
    * application(): Handles the main application route and displays receipts in a table.
    * edit_receipt(receipt_id): Handles the 'edit' route for editing a specific receipt.
    * delete_receipt(receipt_id): Handles the 'delete' route for deleting a specific receipt.
    * download_table(): Generates a CSV file and allows users to download all receipts.

### Helper Functions:
    * convert_date_format(date_str): Converts a date from 'YYYY-MM-DD' to 'DD/MM/YYYY' format.
    * filter_receipts_by_date(receipts, start_date, end_date): Filters receipts based on the selected date range.

## Known Issues
While ReceiptStash is a functional project, some known issues should be addressed:

The application does not handle pdf or file formats other than image files.

## Optional Improvements
Consider implementing a more robust OCR solution or integrating with an OCR service for better accuracy.
Enhance the user interface with additional features and customization options.
