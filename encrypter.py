# Making a Program that Encrypts and Decrypts Files

import os
from cryptography import fernet
from cryptography.fernet import Fernet

class Encrypter:

    def createKey(self):
        ''' This function creates a Key for Encryption and Decryption.'''

        # creating a variable key_generated to check if key is generated
        key_generated=False

        while key_generated==False:

            # Creating A Try Except Block when key folder is not found.

            try:
                # If the function doesn't raise an exception it creates a file key.key and writes the encryption key in it.
                
                with open('key/key.key','wb') as f:
                    f.write(Fernet.generate_key())
                    f.close()

                print('Key Generated.')
                key_generated=True

     
            except:
                # The program raises an exception when it doesn't find the key
                # folder so it creates one instead of throwing an error.

                os.makedirs('./key')

    def encryptFile(self,file):
        '''This Function Encrypts the file which is given as the parameter'''

        # Creating filename variable so that the function extracting only the filename from the file location
        filename=file.split('\\')[-1]

        # Reading the file to get the data from the file 
        # so that it can be encrypted in another file
        with open(file,'rb') as f:
            data=f.read()
            f.close()


        # Using a Try an Except block to get the encryption key

        try:
            # Tries to to read the key 
            with open('key/key.key','rb') as f:
                key=f.read()
                f.close()

        except:
            # The function raises an exception if the key is not found

            print('Key Not Found Please Generate a Key')


        # Creating a file_written variable to check if the file is written
        file_written=False

        # While file is not written 
        while file_written==False:

            # Tries to make a directory if the directory exists then
            # creates the file in that directory  

            try:
                os.makedirs('./Encrypted Files')
                
            except FileExistsError:
                with open('Encrypted Files/Encrypted {}'.format(filename),'wb') as f:
                    f.write(Fernet(key).encrypt(data))
                    f.close()
                os.remove(file)
                print('File Encrypted')
                file_written=True

    def decryptFile(self,encryptedfile):
        '''This Function Decrypts the file'''

        # Creating a filename variable to store the original filename.
        filename=encryptedfile.split('\\')[-1]
        filename=filename.split(' ')[-1]

        # Opening the encrypted file to read the data
        with open(encryptedfile,'rb') as f:
            data=f.read()
            f.close()

        # Opening the key file to get the key
        with open('key/key.key','rb') as f:
            key=f.read()
            f.close()
        
        # Using variable file_written  to check if decrypted file is written or not.
        file_written=False

        # while it is not written

        while file_written==False:
        
            # Tries to make the directory first if directory exist then 
            # it creates the original file in the decrypted files directory
            
            try:
            
                os.makedirs('./Decrypted Files')
            
            except FileExistsError:
            
                with open('Decrypted Files/{}'.format(filename),'wb') as f:
                    f.write(Fernet(key).decrypt(data))
                    f.close()
            
                print('File Decrypted.')
                file_written=True





