import pyAesCrypt

password = input('Type password: ')

# encrypt
# pyAesCrypt.encryptFile('data.txt', 'encrypt-data.txt.aes', password)

# decrypt
pyAesCrypt.decryptFile('encrypt-data.txt.aes', 'data-out', password)