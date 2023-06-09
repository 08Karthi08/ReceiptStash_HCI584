import cv2
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text
img = cv2.imread('/Users/karthi/Documents/584/Git/ReceiptStash_HCI584/ReceiptScanner/img.jpeg')
print(ocr_core(img))
