import xml.etree.ElementTree as ET
import urllib.request
import xmltodict
import json
import sys
#import pdb; 

### reads in the xml and creates a tree for parsing ###
url = 'https://politepol.com/fd/2DbU8Ei8mH9F'
response = urllib.request.urlopen(url)
data = response.read()
response.close()

# Writes data to file for testing.
dataDict = xmltodict.parse(data) #dataDict is a OrderedDict obj
with open("Output.txt", "w") as text_file:
    text_file.write(json.dumps(dataDict))

# Get item (forum posts) array out of data.
# pdb.set_trace()

# Posts is a List object
posts = dataDict['rss']['channel']['item']

# iterating over the ordereddict
for post in posts:
    print(post['pubDate'])

# TODO 
# get latest post from mongodb, compare against pubDates, 
# and trim from the posts obj where pubDate is less than latest date from db


# ### retrieves title ###
# for compTitle in tree.findall('.//title'):
#      print(compTitle.text)

# ### retrieves published date ###
# for compPubDate in tree.findall('.//pubDate'):
#      print(compPubDate.text)

# ### retrieves hyperlinks ###
# for compLink in tree.findall('.//link'):
#      print(compLink.text)

