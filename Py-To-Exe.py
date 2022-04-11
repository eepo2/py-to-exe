import os, sys, time

try:
    os.system("pip install pyinstaller")
except:
    os.system("pip install pyinstaller")

os.system("cls || clear")

print('''
         ██████╗ ██╗   ██╗    ████████╗ ██████╗     ███████╗██╗  ██╗███████╗
         ██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗    ██╔════╝╚██╗██╔╝██╔════╝
         ██████╔╝ ╚████╔╝        ██║   ██║   ██║    █████╗   ╚███╔╝ █████╗  
         ██╔═══╝   ╚██╔╝         ██║   ██║   ██║    ██╔══╝   ██╔██╗ ██╔══╝  
         ██║        ██║          ██║   ╚██████╔╝    ███████╗██╔╝ ██╗███████╗
         ╚═╝        ╚═╝          ╚═╝    ╚═════╝     ╚══════╝╚═╝  ╚═╝╚══════╝
                       |- Programmed By : TheGreatVex -| 
''')

try:
 fname = input("[+] Enter File Name (Must be in the same path as tool and .py) : ")

 time.sleep(1)

 os.system(f"pyinstaller -F {fname}")

 time.sleep(1)

 print("[+] Successfully...")
 os.system("cls || clear")
 print('''
         ██████╗ ██╗   ██╗    ████████╗ ██████╗     ███████╗██╗  ██╗███████╗
         ██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗    ██╔════╝╚██╗██╔╝██╔════╝
         ██████╔╝ ╚████╔╝        ██║   ██║   ██║    █████╗   ╚███╔╝ █████╗  
         ██╔═══╝   ╚██╔╝         ██║   ██║   ██║    ██╔══╝   ██╔██╗ ██╔══╝  
         ██║        ██║          ██║   ╚██████╔╝    ███████╗██╔╝ ██╗███████╗
         ╚═╝        ╚═╝          ╚═╝    ╚═════╝     ╚══════╝╚═╝  ╚═╝╚══════╝
                       |- Programmed By : TheGreatVex -| 
''')
 print("[+] Done converting the file you will find it in |dist| folder")
 print("")
 print("[!] if error happend please restart the tool and make sure your file in the same path as this tool and make sure to type the name and .py")
 print("")

except:     
 print("[!] Error please try again")
 print("")
input("[-] Enter any key for close....")
