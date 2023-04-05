from PIL import Image
import os
import shutil

# set the paths of the input and output folders
input_folder = "C:/Users/Administrator/Desktop/STAGE/PDF_to_JPG/JPG"
output_folder = "C:/Users/Administrator/Desktop/STAGE/PDF_to_JPG/receipts"

# loop through all the files in the input folder
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".jpg"):
            input_file_path = os.path.join(root, file)
            
            # create the same folder structure in the output folder
            rel_path = os.path.relpath(input_file_path, input_folder)
            output_file_path = os.path.join(output_folder, rel_path)
            output_dir = os.path.dirname(output_file_path)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            
            # open the image and get its width
            with Image.open(input_file_path) as img:
                width, height = img.size
            
            # check if the width is greater than 2000 pixels
            if width < 2000:
                shutil.move(input_file_path, output_file_path)
                print(f"Moved {input_file_path} to {output_file_path}")
            else:
                print(f"Skipping {input_file_path} because width is {width}px")
