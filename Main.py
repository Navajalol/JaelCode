import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def Main():
    root = tk.Tk()

    choice = messagebox.askyesno(
        "Folder Selection", 
        "Do you want to select a parent folder (all subfolders included)? \n\n"
        "Yes = select one parent folder. \nNo = select multiple folders manually"
    )

    if choice:
        parent_folder = filedialog.askdirectory(title = "Select parent folder containing multiple folders")
        if not parent_folder:
            print("no parent folder selected.")
            exit()
        source_folders = [os.path.join(parent_folder, d) for d in os.listdir(parent_folder) if os.path.isdir(os.path.join(parent_folder, d))]
       
    
    else: 
        source_folders = select_multiple_folders()
        if not source_folders:
            print("no folders selected.")
            exit()
    
    destination_folder = filedialog.askdirectory(title = "select the destination folder")
    if not destination_folder:
        print("no folder detected.")
        exit()
    
    move_folder(source_folders, destination_folder)




def select_multiple_folders():
    folders = []
    while True: 
        folder = filedialog.askdirectory(Title = "select a source folder (Cancel to stop)")
        if not folder: 
            break 
        folders.append(folder)
    return folders

def move_folder(source_folders, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    print("test in move_folder")
    for source_folder in source_folders:
        for file_name in os.listdir(source_folder):
            if file_name.lower().endswith(".mp3"):
                source_path = os.path.join(source_folder, file_name)
                dest_path = os.path.join(destination_folder, file_name)
    
                shutil.copy2(source_path, dest_path)


Main()

