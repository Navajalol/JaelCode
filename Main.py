import os
import shutil
import tkinter as tk
from tkinter import filedialog

def Main():
    root = tk.Tk()
    root.withdraw()
    source_folder_path = filedialog.askdirectory(title = "Select a folder")

    if not source_folder_path:
        exit()

    dest_folder_path = filedialog.askdirectory(title = "select destination folder")
    if not dest_folder_path:
        exit()

    os.makedirs(dest_folder_path, exist_ok=True)

    for file_name in os.listdir(source_folder_path):
        if file_name.lower().endswith(".mp3"):
            src_path = os.path.join(source_folder_path, file_name)
            dst_path = os.path.join(dest_folder_path, file_name) 

    shutil.copy2(src_path, dst_path)
    print(f"Moved: {file_name}") 
    
Main()

