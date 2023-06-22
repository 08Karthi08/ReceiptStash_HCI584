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
        # pattern = r'\b(\d{1,2}/\d{1,2}/\d{2,4})\b'
        pattern = r'((?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4})'
        match = re.search(pattern, extracted_text)
        if match:
            date = match.group(1)
            return date
        else:
            return None