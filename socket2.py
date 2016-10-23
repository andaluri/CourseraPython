import urllib

web = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in web:
	print line

