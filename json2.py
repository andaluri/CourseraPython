import urllib
import json

url = raw_input("URL: ")

data = urllib.urlopen(url).read()

print 'Retrieved',len(data),'characters'

info = json.loads(data)
sum = 0
print "Count: ", len(info["comments"])
for item in info["comments"]:
    sum = sum + int(item["count"])

print "Sum: ", sum
