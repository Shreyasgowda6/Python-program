import os
import zipfile
def create_zip_folder(folder_path, zip_filename):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: Folder '{folder_path}' does not exist.")
        return

    # Check if the zip file already exists
    if os.path.exists(zip_filename):
        print(f"Warning: File '{zip_filename}' already exists. Overwriting...")

    try:
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the folder and add its content to the ZIP file
            for foldername, subfolders, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(foldername, filename)
                    # Add the file to the ZIP file with the relative path
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))

        print(f"ZIP file '{zip_filename}' created successfully.")
    except Exception as e:
        print(f"Error: Failed to create ZIP file '{zip_filename}'.")
        print(f"Reason: {e}")
folder_path = "/content/Myzip"
zip_filename = "zipped.zip"
create_zip_folder(folder_path,zip_filename)



\\OR\\
import os
import sys
import pathlib
import zipfile

dirName = input("Enter Directory name that you want to backup : ")
if not os.path.isdir(dirName):
    print("Directory", dirName, "doesn't exists")
    sys.exit(0)

curDirectory = pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip", mode="w") as archive:
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path, arcname=file_path.relative_to(curDirectory))

if os.path.isfile("myZip.zip"):
    print("Archive", "myZip.zip", "created successfully")
else:
    print("Error in creating zip archive")

