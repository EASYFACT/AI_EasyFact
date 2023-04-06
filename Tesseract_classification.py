import os
import shutil
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Set up paths for input and output folders
input_folder = "C:/Users/Administrator/Desktop/EasyFact/Model/JPG/Yes"
output_folder = "C:/Users/Administrator/Desktop/EasyFact/Model/JPG/TTC"
# Loop through all the files in the input folder
i=0
for filename in os.listdir(input_folder):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Read the image using PIL
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        # Convert the image to grayscale
        image_gray = image.convert('L')

        # Apply OCR using pytesseract
        text = pytesseract.image_to_string(image_gray)
    
        # Check if the word "T.T.C" is in the OCR result
        if ("total ttc" or "tot ttc") in text.lower():
            i=i+1
            print(i)
            # Copy the image to the output folder
            output_path = os.path.join(output_folder, filename)
            shutil.copyfile(image_path, output_path)