import os
import shutil
import re
from datetime import datetime

def process_image_filenames(input_folder, output_folder, customer_id, machine_id):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Regex pattern for matching the filename format
    pattern = re.compile(rf'^{customer_id}-{machine_id}-(?P<datetime>\d{{4}}-\d{{2}}-\d{{2}}_\d{{2}}_\d{{2}}_\d{{2}})\.(?P<extension>tiff|png|jpg|jpeg|bmp|gif)$')

    for root, _, files in os.walk(input_folder):
        for file in files:
            match = pattern.match(file)
            if match:
                file_path = os.path.join(root, file)
                
                datetime_part = match.group('datetime')
                file_extension = match.group('extension')

                try:
                    dt = datetime.strptime(datetime_part, "%Y-%m-%d_%H_%M_%S")
                    formatted_datetime = dt.strftime("%Y%m%d_%H%M%S")
                    
                    # Construct new filename
                    new_filename = f"ID{customer_id.zfill(4)}_MID{machine_id.zfill(4)}_{formatted_datetime}.{file_extension}"
                    
                    # Copy the file to the output folder with the new name
                    new_file_path = os.path.join(output_folder, new_filename)
                    shutil.copy(file_path, new_file_path)
                    print(f"Copied and renamed: {file_path} to {new_file_path}")
                except ValueError:
                    print(f"Skipping file {file} due to incorrect date format.")
            else:
                print(f"Skipping file {file} due to incorrect filename format.")
 

# Example usage

customer_id = '8'   # Change this to your customer ID
machine_id = '3'    # Change this to your machine ID


                    
input_folder = r'D:\future link\AljalaliAli\OCR Tesseract Feintuning\OCR Test 001\Results\Mues\check the results\OLD_MDE\images_Mues_3_from_20.02.024 to 05.06.2024'
output_folder = 'renamed_images'
process_image_filenames(input_folder, output_folder, customer_id, machine_id)

