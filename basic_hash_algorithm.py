# imports random module which choses a given variable randomly
import random

# a class objective that will be used for encryption
class Encryption():
	
	# initial function of the class objective
	def __init__(self):

		# storage used by function to temporarily load strings and intigers
		self.main_list = []
		self.seq_one = []
		self.seq_two = []
		self.seq_three = []
		self.seq_four = []
		self.seq_five = []
		self.seq_six = []
		self.seq_seven = []
		self.seq_eight = []
		self.seq_nine = []
		
	# XOR function
	def xor_func(self,value,variables):

		# grabs the string value and adds it to the self.main_list
		for i in value:
			self.main_list.append(i)

		# right bit-shift
		# pulls the value in index[0] and moves it to the end of the string
		# adds the result to the self.seq_one list
		for i in range(0,16):
			sXor = self.main_list[i][1:] + self.main_list[i][0]
			self.seq_one.append(sXor)

		# performs XOR 
		# converts the string value to an integer using base of 2
		s0 = int(self.seq_one[0],2)^int(self.seq_one[1],2)
		s1 = int(self.seq_one[2],2)^int(self.seq_one[3],2)
		s2 = int(self.seq_one[4],2)^int(self.seq_one[5],2)
		s3 = int(self.seq_one[6],2)^int(self.seq_one[7],2)
		s4 = int(self.seq_one[8],2)^int(self.seq_one[9],2)
		s5 = int(self.seq_one[10],2)^int(self.seq_one[11],2)
		s6 = int(self.seq_one[12],2)^int(self.seq_one[13],2)
		s7 = int(self.seq_one[14],2)^int(self.seq_one[15],2)

		# adds the XOR results to the self.seq_two list
		self.seq_two.append(s0)
		self.seq_two.append(s1)
		self.seq_two.append(s2)
		self.seq_two.append(s3)
		self.seq_two.append(s4)
		self.seq_two.append(s5)
		self.seq_two.append(s6)
		self.seq_two.append(s7)

		# right bit-shift
		# pulls the value in index[0] and moves it to the end of the string
		# adds the result to the self.seq_three list
		for i in range(0,8):
			sXor = bin(self.seq_two[i])[3:] + bin(self.seq_two[i])[2]
			self.seq_three.append(sXor)

		# performs XOR 
		# converts the string value to an integer using base of 2
		s0 = int(self.seq_three[0],2)^int(self.seq_three[1],2)
		s1 = int(self.seq_three[2],2)^int(self.seq_three[3],2)
		s2 = int(self.seq_three[4],2)^int(self.seq_three[5],2)
		s3 = int(self.seq_three[6],2)^int(self.seq_three[7],2)

		# adds the XOR results to the self.seq_four list
		self.seq_four.append(s0)
		self.seq_four.append(s1)
		self.seq_four.append(s2)
		self.seq_four.append(s3)

		# right bit-shift
		# pulls the value in index[0] and moves it to the end of the string
		# adds the result to the self.seq_five list
		for i in range(0,4):
			sXor = bin(self.seq_four[i])[3:] + bin(self.seq_four[i])[2]
			self.seq_five.append(sXor)

		# performs XOR 
		# converts the string value to an integer using base of 2
		s0 = int(self.seq_five[0],2)^int(self.seq_five[1],2)
		s1 = int(self.seq_five[2],2)^int(self.seq_five[3],2)

		# adds the XOR results to the self.seq_six list
		self.seq_six.append(s0)
		self.seq_six.append(s1)

		# right bit-shift
		# pulls the value in index[0] and moves it to the end of the string
		# adds the result to the self.seq_seven list
		for i in range(0,2):
			sXor = bin(self.seq_six[i])[3:] + bin(self.seq_six[i])[2]
			self.seq_seven.append(sXor)

		# performs the final XOR function from the string value
		h0 = int(self.seq_seven[0],2)^int(self.seq_seven[1],2)

		# mixes the final result to the variables generated randomly
		# adds the results to the self.seq_eight list
		# bin() - converts to binary string
		# ^ - XOR logic function
		# & - AND logic function
		# | - OR logic function
		# << - bitwise shift left
		# >> - bisewise shoft right
		h1 = int(variables[0],2)^h0
		h1 = bin(h1 >> 1)
		self.seq_eight.append(h1[2:].ljust(32,'0'))
		h2 = int(variables[1],2)|h0
		h2 = bin(h2 << 1)
		self.seq_eight.append(h2[2:].ljust(32,'0'))
		h3 = int(variables[2],2)^h0
		h3 = bin(h3 >> 1)
		self.seq_eight.append(h3[2:].ljust(32,'0'))
		h4 = int(variables[3],2)|h0
		h4 = bin(h4 << 1)
		self.seq_eight.append(h4[2:].ljust(32,'0'))

		# converts the string binary to hexadecimal string
		# adds the results into the self.seq_nine list
		for i in range(0,4):
			sXor = hex(int(self.seq_eight[i],2))[2:].zfill(8)
			self.seq_nine.append(sXor)

		# joins the string value from the self.seq_nine list into a single string
		hex_result = ''.join(self.seq_nine)

		# prints the final hash result
		print('\nThe Encrypted data is: {0}'.format(hex_result[0:32]))
		
# a function that converts a string value to binary string
def to_binary(string_value):

	# stores the string value of the input
	# it is used to build the list
	binary_string = ""

	# stores a list of the input value
	# it is used to build the binary list
	binary_list = []

	# length of the input string
	length = len(string_value)

	# covnerts every character of the input string into binary string
	# adds '1' a the end of the binary
	# adds the converted length of the input string
	# str() - converts a value string
	# bin() - converts a value to binary
	# ord() - converts a value to ascii
	# .ljust - adds zero to the right of the string until it reaches its maximum number
	for char in string_value:
		binary_string += (str(bin(ord(char))[2:]) + '1').ljust(448, '0') + str(bin(length)[2:]).zfill(64)

	# creates a list of the 512 and divides it into 32 bits
	for i in range(0,512,32):
		multi_line = binary_string[i:i+32]
		binary_list.append(multi_line)
	
	# returns the value of the binary_list
	return binary_list

# generates 5 random 32 bit variables
def variables():

	# used to store a string value which will be used later on for a list
	variable_string = ""

	# used to store a list for the generated variable
	variable_list = []

	# creates a random integer up to 160 bits
	# . randint() - selects a given value randomly
	for i in range(0,160):
		variable_string += str(random.randint(0,1))

	# divides the 160 bit into 32 bit variable per item in a list
	for i in range(0,160,32):
		var = variable_string[i:i+32]
		variable_list.append(var)

	# returns the value of the variable_list
	return variable_list

def main():

	while True:

		try:

			# reminds the user to how to exit the program
			print('\nPress [ctrl + c] to close the program.\n\n\n')

			# prompts the user to enter the word/words to be encrypted
			string_value = input('\nPlease enter the word/words to be encrypted: ')

			# converts the input value into binary
			binary = to_binary(string_value)

			# generates the variable
			variable_list = variables()

			# assigns the class Encryption() into a variable
			encode = Encryption()

			# assigns the binary and varaible_list and passes in for encryption
			encode.xor_func(binary,variable_list)

		except KeyboardInterrupt:
			print('Program closed...')
			exit()

		except EOFError:
			print('\nPress [ctrl + c] to close the program.')
			continue

		except IndexError:
			print('An index error occured')
			continue

if __name__ == "__main__":
	main()