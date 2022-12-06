from PIL import Image
from pytesseract import pytesseract
from pdf2image import convert_from_path

path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd = path_to_tesseract


print("~"*90)
n=int(input("\t1) All at once\n\t2)From X upto Y\n\t3)Single page\n\nYour Choice : "))
with open("TextfromPDF.txt","a+") as f:
    f.write("~"*90,"\n")
if n==1:
    images = convert_from_path(str(input("PDF location : ")),poppler_path = r"C:\Program Files\poppler-0.68.0\bin")
    for i in range(len(images)):
        print("Reading page "+str(i+1)+"....")
        s=r'E:\trash' ;
        st=r'\page'+ str(i) +'.jpg'
        images[i].save(s+st,'JPEG')
        path_to_image = s+st
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        with open("TextfromPDF.txt","a+") as f:
            f.write(text)
    print("\nText extracted from pdf Successfully.")
elif n==2:
    images = convert_from_path(str(input("PDF location : ")),poppler_path = r"C:\Program Files\poppler-0.68.0\bin")
    X=int("From : ")
    Y=int("Upto : ")                           
    for i in range(len(images)):
        print("Reading page "+str(i+1)+"....")
        if i+1>=X and i+1<=Y:
            s=r'E:\trash' ;
            st=r'\page'+ str(i) +'.jpg'
            images[i].save(s+st,'JPEG')
            path_to_image = s+st
            img = Image.open(path_to_image)
            text = pytesseract.image_to_string(img)
            with open("TextfromPDF.txt","a+") as f:
                f.write(text)
    print("\nText extracted from pdf Successfully.")
elif n==3:
    images = convert_from_path(str(input("PDF location : ")),poppler_path = r"C:\Program Files\poppler-0.68.0\bin")
    X=int(input("Pg No. : "))
    for i in range(len(images)):
        print("Reading page "+str(i+1)+"....")
        if i+1==X:
            s=r'E:\trash' ;
            st=r'\page'+ str(i) +'.jpg'
            images[i].save(s+st,'JPEG')
            path_to_image = s+st
            img = Image.open(path_to_image)
            text = pytesseract.image_to_string(img)
            with open("TextfromPDF.txt","a+") as f:
                f.write(text)
    print("\nText extracted from pdf Successfully.")

#Idea by Ishan Gupta