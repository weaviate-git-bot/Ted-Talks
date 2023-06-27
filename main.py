import os
import zipfile

def extract(folder_path: str):
    if os.path.exists(folder_path):
        extract_directory = "dataset"
        with zipfile.ZipFile(folder_path, 'r') as zip_ref:
            zip_ref.extractall(extract_directory)
        print(folder_path, "extracted")
        os.remove(folder_path)
        print(folder_path, "deleted")
    else:
        print(folder_path, "does not exist")

extract("ted_talks_it.zip")
