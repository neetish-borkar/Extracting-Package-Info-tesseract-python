from PIL import Image
import pytesseract, re
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
f = "sample.jpg"                                                                                      #sample.jpg is the image with the inforation
t = pytesseract.image_to_string(Image.open(f))                                                        #Extracting the text from the image
Name = re.findall(r"Shipping Address :\n+[\w]+ [\w]+", t)                                             #Finding the Name from the text
Phone = re.findall(r"Phone: [\d]+", t)                                                                #Finding the Phone Number from the text
Pincode = re.findall(r"PINCODE - [\d]+", t)                                                           #Finding the Pincode from the image
print(t)                                                                                              #All the text information extracted from the image
print(Name)                                                                                           #Name extracted from the image
print(Phone)                                                                                          #Phone Number extracted from the image
print(Pincode)                                                                                        #Pincode extracted from the image