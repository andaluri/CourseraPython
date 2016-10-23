# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program
#http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Iria.html
import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
cnt = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: '))

for i in range(1, cnt+1):
    print "Retrieving: ", url
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    j = 0
    for tag in tags:
        j += 1
        if j == pos:
            url = tag.get('href', None)         
            break

print "Last Url: ", url
