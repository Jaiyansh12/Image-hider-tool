import os
import ctypes          # to use windows API for (here checking file attributes))
import tkinter as tk
from tkinter import filedialog

FILE_ATTRIBUTE_HIDDEN = 0x2    # it is the flag for hidden attribute in windows file system

def is_hidden(filepath):
    try:
        attrs = ctypes.windll.kernel32.GetFileAttributesW(filepath)            # checks and return the attributes of all the files 
        return attrs != -1 and bool(attrs & FILE_ATTRIBUTE_HIDDEN)             # if hiddden file then true otherwise false
    
    except:
        return False


def get_hidden_files(folder_path):                     # function ofr folder path 
    hidden_files = []                                  # empty list to store hidden files 

    for file in os.listdir(folder_path):                            #  in that folder searcher for hidden files and finds the path 
        full_path = os.path.join(folder_path, file)                 # joins the folder and file name to get full path 

        if is_hidden(full_path):                         
            hidden_files.append(full_path)       # if hidden file found then add in the empty list 

    return hidden_files      # function return


def unhide_file(file_path):                           # function to unhide the files 
    os.system(f'attrib -h "{file_path}"')                   # remove the attribute from the file name 
    print(f"\n File unhidden successfully:\n{file_path}")      


# Step 1: Ask user
choice = input("Do you want to unhide files? (yes/no): ").strip().lower()     # ask yes or no to unhide files 

if choice == "yes":          
    # Step 2: Folder select GUI
    root = tk.Tk()     # if yes show dialog box to select folder 
    root.withdraw()     # to withdraw the dial0og box after selection 
    root.update()     # to propely load dialog box of the explorer

    folder_path = filedialog.askdirectory(title="Select Folder")           # dialog box appearence 

    root.destroy()        # dialog box close       

    if not folder_path:
        print(" No folder selected.")     # if no folder slected then print no folder selected and exits the dialog box 
        exit()

    # Step 3: Scan hidden files
    hidden_files = get_hidden_files(folder_path)         # funciton to scan the hidden files 
 
    if not hidden_files:
        print("\n No hidden files found in this folder.")      # if no files found then print no hidden files found and exit 
        exit()

    # Step 4: Show list in CMD         
    print("\n Hidden files found:\n")

    for i, file in enumerate(hidden_files):     # numbering of the files shown whichn are hidden 
        print(f"{i+1}. {file}")     #$ forn 1,2,3... and so on 

    # Step 5: User chooses file
    choice_num = input("\nEnter file number to unhide (0 to exit): ")

    if choice_num.isdigit():              # chekc for the file input is a number 
        choice_num = int(choice_num)     

        if choice_num == 0:
            print(" Exiting...")                          # if 0 then exit
        elif 1 <= choice_num <= len(hidden_files):        # if number is valid 
            unhide_file(hidden_files[choice_num - 1])     # the use function for unhiding the file 
        else:
            print(" Invalid number.")
    else:
        print(" Enter a valid number.")

elif choice == "no":
    print(" Program closed.")

else:
    print(" Invalid input.")