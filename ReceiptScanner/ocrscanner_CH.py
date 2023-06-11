import cv2
import pytesseract 


def preprocess_image(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    img = cv2.medianBlur(img, 5)
    return img

def ocr_core(img):
    text = pytesseract.image_to_string(img)
    return text

img = cv2.imread('ReceiptScanner/img.png')
img = preprocess_image(img)

#img = cv2.imread('/Users/karthi/Documents/584/Git/ReceiptStash_HCI584/ReceiptScanner/img.jpeg')
img = cv2.imread('ReceiptScanner/img.jpeg') # always use relative paths!
print(ocr_core(img))
