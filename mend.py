''''
	The puporse of this program is to Retrieve the contents of the contact list from the
	[API](https://www.senate.gov/general/contact_information/senators_cfm.xml) in the raw XML format to a JSON output.
	The data contained inside the Member fields in the XML file, convert the data into
	the JSON format listed below.

'''



import os
from xml.etree import ElementTree
import xml.etree.ElementTree as ET
import parser
import json
import array as arr



#FETCH XML DATA FROM AN API
#---------------------------------------------------------------------------
'''
	1. fetch the xml raw data from End point
			1.1.  send an http request to the web to get access to the xml data
			1.2.  once  you recieve request of 200.
			1.3 . parse the xml , then get the root of the element tree

'''
# ---------------------------------------------------------------------------

'''
URL = 'https://www.senate.gov/general/contact_information/senators_cfm.xml'
session = requests.session()
session.trust_env = False
R = requests.get(URL)							#send an http request to the web api
root = R.getroot()								#get the root of the element tree
#print (R.status_code)							# print the status of the api respnse, it should be 200

'''

'''
	READ XML DATA FROM A FILE
	-----------------------------------------------------------------------
	1. Read the data from local file
	2. parse the xml from elements to tree nodes
	3. getthe root

'''

R= ElementTree.parse('xml_Rawdata2.xml') 		# read the xml file from the folder, returns tree structure
root = R.getroot() 								# get the root of the xml  document
#print (root.attrib)
#print (root.getchildren())

g = 0
'''
	DISPLAY THE OUTPUT TO A JSON FORMAT
	-----------------------------------------------------------------------------------
	1. In this section of the program , it illustrates the algorithm on how the output would be displayed
			1.1. once it recieves the xml raw data from the "API " link.
	1. Loop through the xml elements  to access the values of the attributes
	2. print out the values of the attributes in a JSON format
	3.



'''
for x in root.findall("member"): 				# access point to the xml tree structure

	#values to be displayed
	firstN = x.findtext('first_name')
	lastN = x.findtext('last_name')
	fullN = x.findtext('member_full')
	chartId = x.findtext('bioguide_id')
	mobile = x.findtext('phone')
	content = x.findtext("address")
	content1 = []


	#PRINT THE XML DATA TO A JSON FORMAT
	#----------------------------------------------------------------------------------
	print ('{')
	print ('\t','"firstName:"', '"',firstN,'"')
	print ('\t','"lastName:"', '"',lastN,'"')
	print ('\t','"fullName:"', '"',fullN,'"')
	print ('\t','"chartId:"', '"',chartId,'"')
	print ('\t','"mobile:"', '"',mobile,'"')
	print ('\t','"address:"', '"',content,)

	print ('\t','"address:"[ \n',
		'\t','{\n'
		'\t','\t','"street:",'"123 main street"'\n',
		'\t','\t','"city:",'"Orlando"'\n',
		'\t','\t','"state:",'"FL"'\n',
		'\t','\t','"postal:",'"32825"'\n',
		'\t',']')

	print ('}','\n')


'''
sample = "123 Main Street Orlando state FL postal 32825 "
#print (sample)
sampleNew = sample.split() # this is a list

#print (sampleNew) # print the list
sampleLen = len(sampleNew)# list length=8
#print (sampleLen) # length of the list




g = 0
while g < sampleLen:
	if g ==0:
		adr1 = "".join(sampleNew[g])
	elif g == 1:
		adr2 = "".join(sampleNew[g])
	elif g == 2:
		adr3 = "".join(sampleNew[g])
	g +=1

#adr_total = adr1 +adr2+adr3
print (adr1,'', adr2, '', adr3)




# lets print out the Address format

f= 0
while f < sampleLen:
	if f == 3:
		city = sampleNew[f]
		#print ('city: ', sampleNew[f])
	elif f == 4:
		state = sampleNew[f+1]
		#print ('state: ', sampleNew[f+1])
	elif f == 6:
		postal = sampleNew[f+1]
		#print ('postal: ', sampleNew[f+1])

	else:
		print ('')
	f +=1

print (city, state,postal)







pos = 0
#print(content)

#print ("this is a string ")
newContent = content.split()
#print (len(newContent))

print (newContent)

for w in newContent:
	#print (w)

	if len(w) == 1:
		print (w)


	#if len(w) <= 2:
	#	var = ''.join(w)
	#	print ("street: ",'position',pos,' ', w, var)


	elif len(w )== 3:
		print ("city: ",'position', pos,' ', w)
	elif len(w) == 4:
		print ("state: ",'position',pos,' ',w)
	elif len(w) == 5:
		print ("postal:",'position',pos,' ', w) '''
