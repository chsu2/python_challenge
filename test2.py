import string 

# make a list of the alphabet 
alphabetList = list(string.ascii_lowercase)
# print(alphabetList)

def caesarShift(entry, shift):

	# store the decoded string
	decoded = ""

	# for looping purposes 
	i = 0

	# loop through inputed string 
	while i < len(entry):

		# print(entry[i])

		# shift by the given shift 
		if entry[i].isalpha():
			index = alphabetList.index(entry[i]) + shift 
			# print(index)
			if index > 25:

				# - 1 since indexing starts at 0
				decoded += alphabetList[index % 25 - 1] 
			else:
				decoded += alphabetList[index]
			
		else:
			decoded += entry[i]

		# incriment. never forget the incriment! 
		i+=1
	return decoded

# print(caesarShift("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.", 2))
print(caesarShift("map", 2))