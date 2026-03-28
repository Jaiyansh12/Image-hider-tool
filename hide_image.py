import os           # OS for using system command like attrib here
import tkinter as tk         # for GUI file selection dialog box
from tkinter import filedialog     # file dialog is function of TK to open file selection dialog box

def hide_file(file_path):
    if not os.path.exists(file_path):                # if file not found then return file does not exists 
        print(" File not found!")
        return

    os.system(f'attrib +h "{file_path}"')             # for the file input founbd then we will use attrib command to hide the file and +h is for hide attribute
    print(" File hidden successfully!")

# Ask user
choice = input("Do you want to hide a file? (yes/no): ").strip().lower()              # first ask yes or no to hide a file 

if choice == "yes":   
    root = tk.Tk()                    # creates main window 
    root.withdraw()                   # hide main window after selection 
    root.update()                     #  forces window to load properly

    file_path = filedialog.askopenfilename(                # dialog box open for slecting files 
        title="Select an image file",                                                                                                                                   
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.gif *.bmp")]               # only image files will be shown in dialog box 
    )

    root.destroy()                   # clean exit 

    if file_path:                                
        hide_file(file_path)                 # if user select file then execute function which is to hide the file 
    else:                              
        print(" No file selected.")                     # if not then print no file selected 
             
elif choice == "no":                                      # for starting if user says no for hiding a file 
    print(" Program closed.")                              # then clode program 

else:  
    print(" Invalid input. Type yes or no.")              # for inputs other than yes or no 