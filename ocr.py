import pytesseract
from PIL import Image
import re
from io import BytesIO
import datetime

"""
The decision to make the functions in the OCR class static is likely driven by the nature of the class and its purpose. Here are a few possible reasons:

1. Simplicity: Making the functions static allows them to be accessed without the need to create an instance of the OCR class. It simplifies the usage of the OCR functionality by avoiding the need to create an unnecessary instance.

2. Utility Functions: The functions in the OCR class seem to provide utility operations for extracting specific information from the extracted text. They are standalone functions that don't require any state or instance-specific data. In such cases, making them static methods is a common design choice.

3. Code Organization: Making the functions static allows them to be grouped together within the OCR class, providing a logical organization of related OCR operations.

It's important to note that the decision to make functions static or instance methods depends on the specific requirements and design choices of the application. In this case, making the functions static seems appropriate given their purpose and usage within the application.
"""

class OCR:
    @staticmethod
    def extract_text_from_bytes(image_bytes):
        image = Image.open(BytesIO(image_bytes))
        extracted_text = pytesseract.image_to_string(image, lang='eng')
        return extracted_text

    @staticmethod
    def extract_total_amount(extracted_text):
        pattern = r"(?i)(?:Total Amount|Total|Amount)[:\s]*([$]?\d+(?:\.\d{2})?)"  # Example pattern for extracting total amount
        match = re.search(pattern, extracted_text, re.IGNORECASE)
        if match:
            total_amount = match.group(1)
            return total_amount
        else:
            return None

    @staticmethod
    def extract_vendor_name(extracted_text):
        # Example 1: Look for the first line before a line break
        pattern_1 = r'^.*?(?=\n)'
        match_1 = re.search(pattern_1, extracted_text, re.MULTILINE)
        if match_1:
            vendor_name = match_1.group(0)
            return vendor_name.strip()

        # Example 2: Look for text within parentheses
        pattern_2 = r'\((.*?)\)'
        match_2 = re.search(pattern_2, extracted_text)
        if match_2:
            vendor_name = match_2.group(1)
            return vendor_name.strip()

        return None

    @staticmethod
    def extract_date(extracted_text):
        pattern = r'((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})'
        match = re.search(pattern, extracted_text)
        if match:
            date_str = match.group(1)
            date_obj = datetime.datetime.strptime(date_str, '%B %d, %Y').date()
            formatted_date = date_obj.strftime('%Y-%m-%d')
            return formatted_date
        else:
            return None