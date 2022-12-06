from PIL import Image
from pytesseract import pytesseract
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract
path_to_image = input("Path : ")
img = Image.open(path_to_image)
text = pytesseract.image_to_string(img)
print(text)
