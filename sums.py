import sys
import re

file = open(sys.argv[1])
sum = 0
for line in file:
	line = line.strip()
	nums = re.findall("[0-9]+", line)
	if len(nums) > 0:
		for num in nums:
			sum += int(num)

print sum
