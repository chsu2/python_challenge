import fileinput

# need to find the order: lower/Upper/Upper/Upper/lower/Upper/Upper/Upper/lower
def threeOneThree(input):

	#open file and store as a string
	f = open(input, 'r')
	readInFile = f.read()

	#for looping purposes
	i = 0


	# save all the letters to a string
	omg = ""

	#loop through the entire string of file 
	while i < len(readInFile) - 8:

		s = readInFile[i:i+9]

		if s[0].islower() and s[1].isupper() and s[2].isupper() and s[3].isupper() and s[4].islower() and s[5].isupper() and s[6].isupper() and s[7].isupper() and s[8].islower():
			omg+=s[4]

		i+=1
	return omg

# take user input and store in a variable 
userInput = raw_input("Enter file name: ")

# call function
print threeOneThree(userInput)

