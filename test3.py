import fileinput

#takes in a text file and finds the frequency of character
def rareChars(input):

	#open file and store as a string
	f = open(input, 'r')
	readInFile = f.read()

	#string to append secret message to 
	stringOf = ""

	#dictionary to store the characters
	chars = {}

	#for looping purposes
	i = 0

	#loop through the entire string of file 
	while i < len(readInFile):

		character = readInFile[i]

		# if already in the dictionary incriment count
		if character in chars:
			chars[character] += 1

		# if it's a letter, append to a string and add to dictionary
		elif character.isalpha():
			stringOf+=character
			chars[character] = 1

		# add to dictionary if new key
		else:
			chars[character] = 1

		# incriment count
		i+=1

	# loop through dictionary and print out characters and frequency 
	for elt in chars:
		print elt, chars[elt]

	# return the hidden message
	return stringOf

# take user input and store in a variable 
userInput = raw_input("Enter file name: ")

# call function
print rareChars(userInput)