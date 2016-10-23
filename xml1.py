import urllib
import xml.etree.ElementTree as ET

url = raw_input("URL: ")

data = urllib.urlopen(url).read()

print 'Retrieved',len(data),'characters'

tree = ET.fromstring(data)
counts = tree.findall('.//count')
print "Count: ", len(counts)
sum = 0
for count in counts:
    sum = sum + int(count.text)
print "Sum: ", sum

