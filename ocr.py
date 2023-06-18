import pytesseract
from PIL import Image
import re

class OCR:
    @staticmethod
    def extract_text(image_path):
        extracted_text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
        return extracted_text

    @staticmethod
    def extract_total_amount(extracted_text):
        pattern = r'Total\s(\$?\d+(?:\.\d{2})?)'  # Example pattern for extracting total amount
        match = re.search(pattern, extracted_text, re.IGNORECASE)
        if match:
            total_amount = match.group(1)
            return total_amount.strip()
        else:
            return None

    @staticmethod
    def extract_vendor_name(extracted_text):
        # TODO: Implement logic to extract vendor name from the extracted text
        # Example: If vendor name appears in a specific format, you can use regex or string manipulation to extract it
        return 'Uber'

    @staticmethod
    def extract_date(extracted_text):
        # TODO: Implement logic to extract date from the extracted text
        # Example: If date appears in a specific format, you can use regex or string manipulation to extract it
        return None