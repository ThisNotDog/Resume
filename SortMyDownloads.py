#downloads folder organizer
#organizes files in downloads folder into folders based on file type
#created by: @ThisNotDog
#last updated: 10/10/2023

import os
import shutil

#path to downloads folder
path = "C:/Users/[username]/Downloads"

#list of file types
file_types = [
    "exe", "7z", "pdf", "webp", "jpg", "csv", "json",
    "py", "txt", "zip", "iso", "png", "mp4", "mp3",
    "wav", "docx", "xlsx", "pptx", "doc", "xls", 
    "ppt", "msi", "lnk", "url", "rar"
    ]

#list of folders to be created
folders = ["Applications", "Archives", "Documents", "Images", "Scripts", "Videos", "Audio", "Other"]

#creates folders
for folder in folders:
    try:
        os.mkdir(path + "/" + folder)
    except FileExistsError:
        pass

#moves files into folders
for file in os.listdir(path):
    if os.path.isfile(path + "/" + file):
        file_type = file.split(".")[-1]
        if file_type in file_types:
            if file_type == "exe" or file_type == "msi" or file_type == "lnk":
                shutil.move(path + "/" + file, path + "/" + folders[0])
            elif file_type == "7z" or file_type == "zip" or file_type == "iso" or file_type == "rar":
                shutil.move(path + "/" + file, path + "/" + folders[1])
            elif file_type == "pdf" or file_type == "docx" or file_type == "xlsx" or file_type == "pptx" or file_type == "doc" or file_type == "xls" or file_type == "ppt":
                shutil.move(path + "/" + file, path + "/" + folders[2])
            elif file_type == "webp" or file_type == "jpg" or file_type == "png":
                shutil.move(path + "/" + file, path + "/" + folders[3])
            elif file_type == "csv" or file_type == "json" or file_type == "py" or file_type == "txt":
                shutil.move(path + "/" + file, path + "/" + folders[4])
            elif file_type == "mp4":
                shutil.move(path + "/" + file, path + "/" + folders[5])
            elif file_type == "mp3" or file_type == "wav":
                shutil.move(path + "/" + file, path + "/" + folders[6])
            else:
                shutil.move(path + "/" + file, path + "/" + folders[7])

print("Done!")


