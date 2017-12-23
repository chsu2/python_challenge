# import libraries 
import re
import urllib2
from bs4 import BeautifulSoup


pageExtensions = []
# Specify the URL 
quote_page = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'

while quote_page[0:61] == 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=':

	# query the website and return the html to the variable 'page'
	page = urllib2.urlopen(quote_page)

	# parse the html
	soup = BeautifulSoup(page, 'html.parser')

	s = str(soup)

	num = re.findall(r'\d+', s)
	print(num)

	if len(num) != 1:
		print(s)
		userInput = raw_input("Extension or write 'stop' to stop running: ")

		if userInput == 'stop':
			print "finished executing program"
			break
		else:

			quote_page = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + userInput
			pageExtensions.append(userInput)

	else:

		pageExtensions.append(num[0])

		quote_page = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(num[0])
print pageExtensions