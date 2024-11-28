###

from tkinter import filedialog
import os

# Open folder dialog
folder_selected = filedialog.askdirectory()

# # Check if a folder was selected
# if folder_selected:
#     print("Selected folder:", folder_selected)
# else:
#     print("No folder selected.")

files = os.listdir(folder_selected)

# Print each file name
for file_name in files:
    print(file_name)
