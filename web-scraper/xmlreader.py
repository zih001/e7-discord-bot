import xml.etree.ElementTree as ET
import urllib.request
import xmltodict
import json
import sys

### reads in the xml and creates a tree for parsing ###
url = 'https://politepol.com/fd/2DbU8Ei8mH9F'
response = urllib.request.urlopen(url)
data = response.read()
response.close()

# Writes data to file for testing.
dataStr = xmltodict.parse(data)
with open("Output.txt", "w") as text_file:
    text_file.write(json.dumps(dataStr))


# ### retrieves title ###
# for compTitle in tree.findall('.//title'):
#      print(compTitle.text)

# ### retrieves published date ###
# for compPubDate in tree.findall('.//pubDate'):
#      print(compPubDate.text)

# ### retrieves hyperlinks ###
# for compLink in tree.findall('.//link'):
#      print(compLink.text)

