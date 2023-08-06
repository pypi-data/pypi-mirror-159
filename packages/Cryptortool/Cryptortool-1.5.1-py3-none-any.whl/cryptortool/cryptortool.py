try:
    import pyAesCrypt, os, sys
    import requests as r
    from stegano import lsb
except ModuleNotFoundError:
    print("\n[Error] Module pyAesCrypt or requests or Stegano not found")
    modules = input("Do you want install them right now (Y/N)? ").lower()
    if modules == "y" or modules == "yes":
        import os, sys
        os.system("pip install pyAesCrypt requests stegano||pip3 install pyAesCrypt requests stegano")
        print("[SUCCESS] Successfully installed pyAesCrypt and requests\nPlease, restart program")
        sys.exit()
    else:
        import sys
        sys.exit()

class Cryptor:
    def __init__(self):
        self.PyVersion = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        self.CryptorVersion = "1.5.0"
        self.headers = {'user-agent': 'Python/'+self.PyVersion+' | Cryptor/'+self.CryptorVersion}
    def encrypt(self, data, key, method):
        enc = r.post(f"https://api.vaar.pp.ua/crypt/", data={"data": data, "key": key, "method": method, "mode": "e"}, headers=self.headers)
        status_code = enc.status_code
        enc = enc.json()
        if status_code == 200:
            return enc["text"]
        else:
            return "[Error] "+str(enc["message"])

    def decrypt(self, data, key, method):
        enc = r.post(f"https://api.vaar.pp.ua/crypt/", data={"data": data, "key": key, "method": method, "mode": "d"}, headers=self.headers)
        status_code = enc.status_code
        enc = enc.json()
        if status_code == 200:
            return enc["text"]
        else:
            return "[Error] "+str(enc["message"])
    def EncryptFile(self, file, password):
        bufferSize = 512*1024
        pyAesCrypt.encryptFile(
            str(file),
            str(file)+".aes",
            password,
            bufferSize
        )
        # os.remove(file)
        print(f"[SUCCESS]: File {file} successfully encrypted")
        delete = str(input("Do you want to delete original file (Y/N)? "))
        if delete.lower() == "y" or delete.lower() == "yes":
            os.remove(file)
            print("[INFO]: Original file was deleted")

    def DecryptFile(self, file, password):
        bufferSize = 512*1024
        try:
            pyAesCrypt.decryptFile(
                str(file),
                str(os.path.splitext(file)[0]),
                password,
                bufferSize
            )
            print(f"[SUCCESS]: File {file} successfully decrypted")
            delete = str(input("Do you want to delete encrypted file (Y/N)? "))
            if delete.lower() == "y" or delete.lower() == "yes":
                os.remove(file)
                print("[INFO]: Encrypted file was deleted")
        except:
            print("[Error]: Wrong password or file is damaged!")

# def logo():
#     os.system('cls||clear')
#     print("""                                                                    
                                                                                                                                                                                                        
#            ```````                                                    ```                         v.1.5.0      
#         .ohdmNNNmdy/`                                                sddd`                              
#       `sMMMMMNNNMMMMm:   ```  ````  ````     `````  ```   ````     `-MMMM.``     ```````      ````  ``` 
#       sMMMMm:``.+MMMMN. -mmmh/dMMd -mmmmy   `dmmmo ommmoodNMMNh:  /mNMMMMmmy   :ydNMMMNdy:   `mmmd/dNMN 
#       NMMMM/     +ssss. -MMMMMMMMm  oMMMM:  +MMMm` sMMMMMdhmMMMM+ :hNMMMMhhs `hMMMNysyNMMMh` `MMMMMMMMN 
#      `MMMMM:            -MMMMN/..`   hMMMm `NMMM-  sMMMM/   dMMMN   yMMMM`   +MMMM:   :MMMM+ `MMMMN+..` 
#       mMMMMs     sNNNN- -MMMMs       `mMMM+oMMMo   sMMMM.   hMMMM   yMMMM`   sMMMM.   .MMMMs `MMMMy     
#       :MMMMMh+/+hMMMMd  -MMMMo        -NMMNNMMh    sMMMMh--/NMMMd   yMMMM:`  :MMMMs.`.sMMMM- `MMMMy     
#        -hMMMMMMMMMMNs`  -MMMMo         /MMMMMN.    sMMMMMMMMMMMm.   +MMMMMMh  :mMMMMMMMMMd:  `MMMMy     
#          `:osyyss+:`    `oooo:          dMMMM/     sMMMM:/syso:`     -osyys/    -+ssyss+-    `oooo:     
#                                     /yydMMMN+      sMMMM-                                               
#                                     omNNNds.       +dddd.                                               
#                                      `````          ````                                                
#     """)
# try:
#     logo()
#     cryptor = Cryptor()
#     print("Menu: ")
#     print("1 - Encrypt or Decrypt text\n2 - Encrypt or Decrypt file\n3 - Encrypt or Decrypt text in photo(PNG only)\n4 - Exit")
#     FileOrText = input("[+] What do you want to do? ").lower()
#     if FileOrText == "1":
#         logo()
#         print("Menu: ")
#         print("1 - Encrypt text\n2 - Decrypt text\n3 - Exit")
#         mode = input("[+] What do you want to do? ").lower()
#         data = input("[+] Enter text: ")
#         print("--------------------")
#         password = input("[+] Enter password: ")
#         if mode == "1":
#             encrypted = cryptor.encrypt(data, password, "AES-256-CBC")
#             if "[Error]" in encrypted:
#                 print(encrypted)
#             else:
#                 print("Encrypted text: "+str(encrypted))
#         elif mode == "2":
#             decrypted = cryptor.decrypt(data, password, "AES-256-CBC")
#             if "[Error]" in decrypted:
#                 print(decrypted)
#             else:
#                 print("Decrypted text: "+str(decrypted))
#         elif mode == "3":
#             import sys
#             sys.exit()
#         else:
#             print("[Error] Unknown mode")
#     elif FileOrText == "2":
#         logo()
#         print("Menu: ")
#         print("1 - Encrypt file\n2 - Decrypt file\n3 - Exit")
#         mode = input("[+] What do you want to do? ").lower()
#         dir = input("[+] Enter file: ")
#         print("--------------------")
#         password = input("[+] Enter password: ")

#         if mode == "1":
#             cryptor.EncryptFile(dir, password)
#         elif mode == "2":
#             cryptor.DecryptFile(dir, password)
#         elif mode == "3":
#             import sys
#             sys.exit()
#         else:
#             print("[Error] Unknown mode")
#     elif FileOrText == "3":
#         logo()
#         print("Menu: ")
#         print("1 - Hide text in image\n2 - Show hidden text\n3 - Exit")
#         mode = input("[+] What do you want to do? ").lower()
#         if mode == "1":
#             input_image = input("[+] Enter input image name: ")
#             output_image = input("[+] Enter output image name: ")
#             data = input("[+] Enter text: ")
#             print("--------------------")
#             password = input("[+] Enter password: ")
#             stegano = lsb.hide(input_image, cryptor.encrypt(data, password, "AES-256-CBC"))
#             stegano.save(output_image)
#             print(f"[SUCCESS] Successfully hidden text in image({output_image})")
#         if mode == "2":
#             image = input("[+] Enter image name: ")
#             print("--------------------")
#             password = input("[+] Enter password: ")
#             clear_message = lsb.reveal(image)
#             print(f"Hidden text: {cryptor.decrypt(clear_message, password, 'AES-256-CBC')}")
#         elif mode == "3":
#             import sys
#             sys.exit()
#     elif mode == "4":
#         import sys
#         sys.exit()
#     else:
#         print("[Error] Unknown mode")
#     # input("\nPress enter to exit...")
# except Exception as ex:
#     print(ex)