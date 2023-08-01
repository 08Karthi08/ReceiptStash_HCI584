# ReceiptStash - Developer's Guide

## Overview
Welcome to the ReceiptStash Developer's Guide! This document serves as a comprehensive resource for developers who want to contribute to or understand the inner workings of ReceiptStash, a web application for uploading and organizing receipts. It provides an overview of the software, installation and deployment instructions, user interaction flow, known issues, and more.

## Installation and Deployment
Assuming the developer has already read the user's guide and installed the project, here are additional considerations for deployment and administration:

Ensure the correct versions of dependencies are installed by checking the requirements.txt file.

Set the SECRET_KEY environment variable to ensure session security if deploying the application in a production environment.

Configure the database connection string in the ReceiptDB class constructor (receipt_db.py) to match the desired deployment environment.

## User Interaction and Flow
The user interaction flow in ReceiptStash involves the following steps:

The user visits the application URL and is redirected to the main application page.

The user can upload receipt images on the main application page using the "Upload Receipt" button.

After the user selects an image, the application processes it using OCR to extract text, including vendor name, date, and total amount.

If the OCR extraction succeeds, the application stores the extracted data in the database, displaying a success message.

The user can filter receipts by date range using the date filters provided on the main application page.

The "View Receipts" table displays the filtered receipts, and the user can edit or delete individual receipts.

## Code Structure
The main Flask application (app.py) is responsible for handling user requests and rendering templates. The project is organized into several modules:

- `app.py: `Contains the main Flask application and routes.
- `ocr.py: `Implements Optical Character Recognition (OCR) functions to extract text from receipt images.
- `receipt_db.py: `Provides functions for interacting with the SQLite database to manage receipt data.
- `date_utils.py: `Includes utility functions for handling data-related operations.

## Known Issues
While ReceiptStash is a functional project, some known issues should be addressed:

The application does not handle pdf or file formats other than image files.

## Optional Improvements
Consider implementing a more robust OCR solution or integrating with an OCR service for better accuracy.
Enhance the user interface with additional features and customization options.
