# py to exe converter
# ====================================================== #

# Libraries
import os, sys, time

# installing the pyinstaller using cmd (pyinstaller = the tool to convert)

try:
    os.system("pip install pyinstaller")
    
    # except means if any error happend the tool will still installing the library
    
except:
    os.system("pip install pyinstaller")
    
    # cls or clear means the tool will auto clear the cmd

os.system("cls || clear")

# printing the logo - Programmed by : The Great Vex -

print('''
         ██████╗ ██╗   ██╗    ████████╗ ██████╗     ███████╗██╗  ██╗███████╗
         ██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗    ██╔════╝╚██╗██╔╝██╔════╝
         ██████╔╝ ╚████╔╝        ██║   ██║   ██║    █████╗   ╚███╔╝ █████╗  
         ██╔═══╝   ╚██╔╝         ██║   ██║   ██║    ██╔══╝   ██╔██╗ ██╔══╝  
         ██║        ██║          ██║   ╚██████╔╝    ███████╗██╔╝ ██╗███████╗
         ╚═╝        ╚═╝          ╚═╝    ╚═════╝     ╚══════╝╚═╝  ╚═╝╚══════╝
                       |- Programmed By : TheGreatVex -| 
''')

# asking the user for the file name.py

try:
 fname = input("[+] Enter File Name (Must be in the same path as tool and .py) : ")

# the tool will sleep for 1 second

 time.sleep(1)

  # the tool will use pyinstaller to convert the file like = pyinstaller -F filename.py
    
 os.system(f"pyinstaller -F {fname}")

 # the tool will sleep for 1 second

 time.sleep(1)

 # telling the user the operation

 print("[+] Successfully...")

# cls or clear means the tool will auto clear the cmd

 os.system("cls || clear")
    
    # printing the logo - Programmed by : The Great Vex -
    
 print('''
         ██████╗ ██╗   ██╗    ████████╗ ██████╗     ███████╗██╗  ██╗███████╗
         ██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗    ██╔════╝╚██╗██╔╝██╔════╝
         ██████╔╝ ╚████╔╝        ██║   ██║   ██║    █████╗   ╚███╔╝ █████╗  
         ██╔═══╝   ╚██╔╝         ██║   ██║   ██║    ██╔══╝   ██╔██╗ ██╔══╝  
         ██║        ██║          ██║   ╚██████╔╝    ███████╗██╔╝ ██╗███████╗
         ╚═╝        ╚═╝          ╚═╝    ╚═════╝     ╚══════╝╚═╝  ╚═╝╚══════╝
                       |- Programmed By : TheGreatVex -| 
''')

# telling user that done converting
 print("[+] Done converting the file you will find it in |dist| folder")
    
    # space between lines to give it better look
    
 print("")

# telling user if any issue happend and how to solve it

 print("[!] if error happend please restart the tool and make sure your file in the same path as this tool and make sure to type the name and .py")
    
    # space between lines to give it better look
    
 print("")

  # except means if any error happend the tool will not print any errors

except:     
 print("[!] Error please try again")

# space between lines to give it better look

 print("")
    
    # input so user press any key on the keyboard and the tool will be closed
    
input("[-] Enter any key for close....")



# all rights reserved to TheGreatVex ,, mention me if you're going to use this basic tool ,, thanks for viewing my tool .
