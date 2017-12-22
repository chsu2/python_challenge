import string 
alphabetList = list(string.ascii_lowercase)
# print(alphabetList)

def caesarShift(entry, shift):

	decoded = ""

	i = 0
	while i < len(entry):

		# print(entry[i])

		if entry[i].isalpha():
			index = alphabetList.index(entry[i]) + shift 
			# print(index)
			if index > 25:
				decoded += alphabetList[index % 25 - 1] 
			else:
				decoded += alphabetList[index]
			
		else:
			decoded += entry[i]
			# print("i'm in the first if")
		i+=1
	return decoded
# print(string.maketrans("http://www.pythonchallenge.com/pc/def/map.html"))
# print(caesarShift("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.", 2))
print(caesarShift("map", 2))