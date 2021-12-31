import xml.etree.ElementTree as ET
import urllib.request
import xmltodict
import json
import sys

### reads in the xml and creates a tree for parsing ###
url = 'https://politepol.com/fd/2DbU8Ei8mH9F'
response = urllib.request.urlopen(url)
tree = ET.fromstring(response.read())
response.close()


### reads in the xml for direct mapping to json ###
file = urllib.request.urlopen('https://politepol.com/fd/2DbU8Ei8mH9F')
data = file.read()
data = xmltodict.parse(data)
### check to ensure all data got read ###
# text = json.dumps(data)
# with open('check', 'w') as f:
#     f.write(text)
# f.closed
file.close()

### retrieves title ###
for compTitle in tree.findall('.//title'):
     print(compTitle.text)

### retrieves published date ###
for compPubDate in tree.findall('.//pubDate'):
     print(compPubDate.text)

### retrieves hyperlinks ###
for compLink in tree.findall('.//link'):
     print(compLink.text)

