from Crypto.Cipher import AES

# Encryption
def encrypt(message):
	obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
	ciphertext = obj.encrypt("Hi hello")
	return ciphertext

# Decryption
def decrypt(ciphertext):
	obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
	cleartext = obj2.decrypt(ciphertext)
	return cleartext

print("\t\t Welcome! \n")
choice1 = int(input("Enter the choice: 1. Encrypt 2.Decrypt 3. Exit"))

if choice1 == 1:
	infile = input("Enter the file name which is to be encrypted: ")
	outfile = input("Enter the location to store the secured data: ")

	file1 = open(infile, 'r')
	data = file1.read()
	ciphertext = encrypt(data)

	file2 = open(outfile,'w')
	file2.write(str(ciphertext))

	print("Encryption Succcessful!")

	file2.close()
	file1.close()	
	exit()

elif choice1 == 2:
	infile = input("Enter the filename which is to be decrypted: ")
	outfile = input("Enter the file where the cleartext has to be saved: ")

	file1 = open(infile, 'r')
	data = file1.read()
	cleartext = decrypt(str.encode(data))

	print(cleartext)

	file2 = open(outfile,'w')
	file2.write(str(cleartext))

	print("Decryption Succcessful!")

	file2.close()
	file1.close()
	exit()

elif choice1 == 3:
	print("Thank you!")
	exit()

else:
	print("Enter the valid choice!")
	exit()


# from Crypto.Cipher import AES
# obj = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
# message = "Hemang"
# ciphertext = obj.encrypt(message)
# print(ciphertext)
# obj2 = AES.new('This is a key123', AES.MODE_CFB, 'This is an IV456')
# cleartext = obj2.decrypt(ciphertext)
# print(cleartext)