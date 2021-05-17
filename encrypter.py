# Making a Program that Encrypts and Decrypts Files

import os
from cryptography import fernet
from cryptography.fernet import Fernet

class Encrypter:

    def createKey(self):
        key_generated=False

        while key_generated==False:
            try:
                with open('key/key.key','wb') as f:
                    f.write(Fernet.generate_key())
                    f.close()
                print('Key Generated.')
                key_generated=True
                break

            except:
                os.makedirs('./key')

    def encryptFile(self,file):

        filename=file.split('\\')[-1]

        with open(file,'rb') as f:
            data=f.read()
            f.close()
            
        try:
            with open('key/key.key','rb') as f:
                key=f.read()
                f.close()
        except:
            print('Key Not Found Please Generate a Key')


        while True:
            try:
                os.makedirs('./Encrypted Files')
            except FileExistsError:
                break

        file_written=False

        while file_written==False:
            try:
                with open('Encrypted Files/Encrypted {}'.format(filename),'wb') as f:
                    f.write(Fernet(key).encrypt(data))
                    f.close()
                print('File Encrypted')
                file_written=True
            except:
                print('Error Occurred')
                break

# ====== WORK IN PROGRESS ===== # 
    def decryptFile(self,file):
        filename=file
