fh = open("/Users/andaluri/CourseraPython/mbox-short.txt")
hourCount = dict()

for line in fh:
    l = line.split()
    if len(l) > 2:
        if l[0]=="From":
            hour = l[5].split(":")[0]
            hourCount[hour] = hourCount.get(hour, 0) + 1

for hour in sorted(hourCount):
    print hour, hourCount[hour]