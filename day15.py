texts = ""
with open("day15input.txt") as file:
	for line in file:
		texts = line.strip().split(",")

def score(hashable):
	tots = 0
	for char in hashable:
		tots+=ord(char)
		tots*=17
		tots = tots % 256
	return tots

tots = 0
for x in texts:
	tots += score(x)
print("part1:",tots)
boxes = [[] for x in range(256)]
for y in texts:
	if "=" in y:
		indicator, num = y.split("=")
		num = int(num)
		ind = score(indicator)
		found = False
		for i in range(len(boxes[ind])):
			if boxes[ind][i][0] == indicator:
				boxes[ind][i][1] = num
				found = True
		if not found:
			boxes[ind].append([indicator, num])
	elif "-" in y:
		indicator = y.split("-")[0]
		ind = score(indicator)
		total = []
		found = False
		for x in boxes[ind]:
			if x[0] == indicator:
				total = x
				found = True
				break
		if found:
			boxes[ind].remove(total)
tots = 0
for i in range(len(boxes)):
	for j in range(len(boxes[i])):
		tots += boxes[i][j][1] * (i+1) * (j+1)
print("part2:", tots)
