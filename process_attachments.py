import os
import shutil


class ProcessAttachments:

    def __init__(self, attachments_folder="attachments"):
        self.attachments_folder = attachments_folder
        self.processed_files_folder = "processed"
        if not os.path.exists(self.processed_files_folder):
            os.makedirs(self.processed_files_folder)

    def get_files(self):
        # Walk through all directories and subdirectories
        for root, dirs, files in os.walk(self.attachments_folder):
            for file in files:
                source_path = os.path.join(root, file)
                
                # Create relative path to maintain directory structure
                relative_path = os.path.relpath(root, self.attachments_folder)
                dest_folder = os.path.join(self.processed_files_folder, relative_path)
                
                # Create destination directory if it doesn't exist
                os.makedirs(dest_folder, exist_ok=True)
                
                dest_path = os.path.join(dest_folder, file)
                
                # Copy the file
                shutil.copy2(source_path, dest_path)
                print(f"Copied: {source_path} -> {dest_path}") 