import os
from pdf2image import convert_from_path

input_path = "C:/Users/Administrator/Desktop/STAGE/PDF_to_JPG/PDF"
output_path = "C:/Users/Administrator/Desktop/STAGE/PDF_to_JPG/JPG"

for root, dirs, files in os.walk(input_path):
    for file in files:
        if file.endswith('.pdf'):
            input_file_path = os.path.join(root, file)
            output_subdir = os.path.relpath(root, input_path)
            output_dir_path = os.path.join(output_path, output_subdir)
            os.makedirs(output_dir_path, exist_ok=True)
            pages = convert_from_path(input_file_path, dpi=300)
            for i, page in enumerate(pages):
                output_file_path = os.path.join(output_dir_path, f"{os.path.splitext(file)[0]}_{i+1}.jpg")
                page.save(output_file_path, 'JPEG')