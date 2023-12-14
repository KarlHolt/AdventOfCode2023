inputs = []
inputs2 = []
with open('day12example.txt') as file:
	i = 0
	for line in file:
		inputs2.append(["", []])
		mapped, numbers = line.strip().split(" ")
		inputs.append([mapped, [int(x) for x in numbers.split(",")]])
		inputs2[-1][0] = mapped
		for i in range(4):
			inputs2[-1][0] += "?"+mapped
			for y in inputs[-1][1]:
				inputs2[-1][1].append(y)

def insert_earlies(earliest_index, number, string):
	start_indexs = []
	current = 0
	for i in range(earliest_index, len(string)):
		char = string[i]
		if char in ["?", "#"]:
			current += 1
			if current >= number:
				start = i - number + 1
				end = i+1
				if end < len(string):
					if string[end] in [".", "?"]:
						if (string[start-1] in [".", "?"] and start > 0) or start == 0:
							start_indexs.append(start)
				else:
					if (string[start-1] in [".", "?"] and start > 0) or start == 0:
						start_indexs.append(start)
		if char == ".":
			current = 0
	return start_indexs

tots = 0
for ins in inputs2:
	nums = ins[1][0]
	stack = [[x+nums+1, 1, ins[0][x:x+nums]] for x in insert_earlies(0, nums, ins[0])]
	temp = 0
	while(len(stack) > 0):
		current = stack.pop(0)
		nums = ins[1][current[1]]
		if current[1] == len(ins[1]) - 1:
			puff = insert_earlies(current[0], nums, ins[0])
			for p in puff:
				if (current[2]+ins[0][p:p+nums]).count("#") == ins[0].count("#"):
					temp+=1
		else:
			wow = insert_earlies(current[0], nums, ins[0])
			for w in wow:
				stack.append([w+nums+1, current[1]+1, current[2]+ins[0][w:w+nums]])
	#print(ins, temp)
	tots += temp

print(tots)