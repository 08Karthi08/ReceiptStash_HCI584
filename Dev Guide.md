# ReceiptStash - Developer's Guide

## Overview
Welcome to the ReceiptStash Developer's Guide! This document serves as a comprehensive resource for developers who want to contribute to or understand the inner workings of ReceiptStash. It provides an overview of the software, installation, deployment instructions, user interaction flow, known issues, and more.
## Tasks and Target Users
* **Task Vignette 1:** Uploading and Scanning Receipts- 
 **User 1:** User wants to digitize their receipts for better organization and easy access.
* **Task Vignette 2:** Searching and Retrieving Receipts-
 **User 2:** User wants to quickly locate a specific receipt.
* **Task Vignette 3:** Generating Expense Excel Report- 
 **User 3:** User wants to generate an expense report for documentation.
## Installation and Deployment
 ***Refer to user guide/README for more details***
 
Here are additional considerations for deployment and administration:

Ensure the correct versions of dependencies are installed by checking the requirements.txt file.

Set the SECRET_KEY environment variable to ensure session security if deploying the application in a production environment.

Configure the database connection string in the ReceiptDB class constructor (receipt_db.py) to match the desired deployment environment.

## User Interaction and Flow
The user interaction flow in ReceiptStash involves the following steps:

1. User accesses the web application by navigating to the application URL.
2. The application's main page is displayed, showing a table with existing receipts (if any) and options to upload new receipts.
3. After the user selects an image, the application processes it using OCR to extract text, including vendor name, date, and total amount.
4. If the OCR extraction succeeds, the application stores the extracted data in the database, displaying a success message.
5. The user can filter receipts by date range using the date filters provided on the main application page.
6. The table displays the filtered receipts
7. The user can edit or delete individual receipts.
8. User can download the receipts to a CSV file using the download button.
   
![image](https://github.com/08Karthi08/ReceiptStash_HCI584/assets/135080809/35f6f97d-f4e0-4c99-a4ba-8c64f33b0e94)


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

## Future Work
- **User Authentication:** Implement user authentication and user accounts to allow users to securely access and manage their own receipts. This would enable personalized views and data organization.

- **User Profiles and Tags:** Create user profiles where users can add tags or categories to their receipts. This feature would improve organization and make it easier for users to search and filter receipts.

- **OCR Improvements:** Explore advanced OCR techniques to improve text extraction accuracy from receipt images. Investigate OCR libraries with better support for various receipt formats and languages.

- **Data Visualization:** Integrate data visualization tools to provide users with insights into their spending patterns. Display statistics, charts, and graphs to help users analyze their expenses.

- **Export and Reporting:** Enable users to export receipt data in various formats, such as PDF or link, for easy sharing and reporting purposes.

- **Batch Processing:** Allow users to upload multiple receipt images at once and process them in a batch. This feature would save time for users with multiple receipts to upload.

- **Mobile App Integration:** Develop a mobile application that allows users to capture and upload receipt images directly from their mobile devices. This would enhance the user experience and accessibility.

- **Automated Expense Tracking:** Implement an automated expense tracking system that categorizes expenses and provides budgeting suggestions based on user spending patterns.

- **Collaborative Receipt Management:** Introduce collaborative features to allow multiple users to manage receipts for shared expenses or projects.
