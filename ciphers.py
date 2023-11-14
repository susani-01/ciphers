try:
	import pyperclip

except ImportError:

	pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRST'

while True:
	print("Do you want to (e)ncrypt or (d)ecrypt ?")

	response = input('> ').lower()
	if response.startswith('e'):
		mode = 'encrypt'
		break

	elif response.startswith('d'):
		mode = 'decrypt'
		break

	print("Enter the letter e or  d")

#Let the user again Enter the key

while True:
	maxKey=len(SYMBOLS)-1
	print('Please enter the key (0 to {}) to use.'.format(maxKey))
	response=input('> ').upper()
	if not response.isdecimal():
		continue

	if 0 <= int(response)<len(SYMBOLS):
		key = int(response)
		break

#Let the user Enter the the message to encrypt/decrypt:
print('Enter the message to {}.'.format(mode))
message = input('> ')

#caesar cipher only work on the upper case letter

message = message.upper()

#store the encrypted/decrypted form of the message:
translated = ''

#Encrypted/decrypted each symbols in the message:
for symbol in message:
	if symbol in SYMBOLS:
		#Get the encr or decry number for this symbol.
		num = SYMBOLS.find(symbol) #Get the number of the symbol.

		if mode == 'encrypt':
			num = num+key

		elif mode == 'decrypt':
			num=num-key

			if num>=len(SYMBOLS):
				num = num-len(SYMBOLS)
			elif num<0:
				num=num+len(SYMBOLS)

		translated=translated+SYMBOLS[num]

	else:

		#just add the symbol without any encry or decry to the screen:

		translated = translated + symbol

print(translated)

try:
	pyperclip.copy(translated)
	print('Full {}ed text copied to clipboard.'.format(mode))

except:
	pass








