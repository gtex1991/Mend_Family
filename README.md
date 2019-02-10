************************************************

# TABLE OF CONTENTS
* [INTRODUCTION](#INTRODUCTION)
* [PREREQUISITE](#PREREQUISITE)
* [SETUP](#SETUP)
* [LAUNCH](#LAUNCH)

# INTRODUCTION

The purpose of this program is to Retrieve the contents of the contact list from the
[API](https://www.senate.gov/general/contact_information/senators_cfm.xml) in the raw XML format
and outputting it to a JSON format.
The data contained inside the Member fields of the XML file is converted into
the JSON format listed below.

```
{
	“firstName”: “First”,
	“lastName”: “Last”,
	“fullName”: “First Last”,
	“chartId”: “:Contents of bioguide_id:”,
	“mobile”: “Phone”,
	“address”: [
		{
			“street”: “123 Main Street”,
			“city”: “Orlando”,
			“state”: “FL”,
			“postal”: 32825
				]
		}
}
```


## PREREQUISITE

1. OS : Mac OS X
2. Language: Python 3.7.2
3. pip (For installing python packages/modules)

**NOTE THIS CAN RUN ON ANY MACHINE THAT IS COMPATIBLE WITH PYTHON3**

## SETUP
**Make sure the following modules are installed for python3**

1. in mac os x terminal,	type : python3
2. in the python console	type : import requests
3. if you get an error
	install requests package  - > Ctrl c (to go back to terminal), type: $  ```$ sudo pip3 install requests```
4. install xmltodict : ```$ sudo pip install xmltodict```


## LAUNCH
1. download the project folder to desktop folder and unzip it
2. open terminal in mac: **Cmd + 'spacebar'** type **terminal**
3. Navigate to the projects location
	for my location machine its "/Users/gastonmulisanga/Desktop/Mend_Pro".**This will be different from your machine**
4. to run the program, in terminal type : ```$ python3 mend.py```
5. check the output of the program in terminal, it should be JSON output from the http request.
