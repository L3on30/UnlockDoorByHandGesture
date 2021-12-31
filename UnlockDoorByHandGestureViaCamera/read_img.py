import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import cv2
from playsound import playsound

Path = "Image"
myImage = os.listdir(Path)
core = "password_record.png"

if core in myImage:
    image = cv2.imread('Image/password_record.png', cv2.IMREAD_UNCHANGED)
else:
    image = cv2.imread('Image/blank.png', cv2.IMREAD_UNCHANGED)

#scale_percent = 50 # percent of original size
#width = int(image.shape[1] * scale_percent / 600)
#height = int(image.shape[0] * scale_percent / 1066)
#dim = (width, height)

#resized_img = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)

cs_config = r'-c tessedit_char_whitelist=ABCDEFGH123456789 --psm 7 --oem 3'
#config='--psm 10 --oem 3 -c tessedit_char_whitelist=ABCD0123456789'
image_text = pytesseract.image_to_string(image, lang='eng', config=cs_config)



