from Crypto.Hash import SHA256
from Crypto.Cipher import AES
import os, random, pkg_resources

def encrypt(key, filename):
	chunkSize = 64 * 1024
	outFile = "(encrypted)"+filename
	fileSize = str(os.path.getsize(filename)).zfill(16)
	IV = os.urandom(16)

	encryptor = AES.new(key, AES.MODE_CBC, IV)

	with open(filename, "r") as inFile:
		with open(outFile, "wb") as outFile:
			outFile.write(fileSize.encode('utf-8'))
			outFile.write(IV)
			while True:
				chunk = inFile.read(chunkSize)
				if len(chunk) == 0:
					break
				elif len(chunk) % 16 != 0:
					chunk += ' ' * (16 - (len(chunk) % 16))
				outFile.write(encryptor.encrypt(chunk))

def decrypt(key, filename):
	chunkSize = 64 * 1024
	outFile = filename[11:]

	with open(filename, "rb") as inFile:
		fileSize = int(inFile.read(16))
		IV = inFile.read(16)

		decryptor = AES.new(key, AES.MODE_CBC, IV)

		with open(outFile, "wb") as outFile:
			while True:
				chunk = inFile.read(chunkSize)
				if len(chunk) == 0:
					break
				outFile.write(decryptor.decrypt(chunk))
			outFile.truncate(int(fileSize))

def getKey(password):
	hasher = SHA256.new(str(password).encode('utf-8')).digest()
	return hasher

def main():
	choice = input("Would you like to [E]ncrypt or [D]ecrypt: ").upper()

	keyboard = Controller()

	if choice == 'E':
		filename = input("File to encrypt: ")
		password = input("Enter password: ")
		encrypt(getKey(password), filename)
		print("Encryption Complete")
	elif choice == 'D':
		filename = input("File to Decrypt: ")
		password = input("Enter password: ")
		decrypt(getKey(password), filename)
		print("Decryption Complete")
	else:
		print("No option selected, closing...")

if __name__ == "__main__":
	main()
