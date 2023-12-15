looping = {}
starting_idex = []
full_input = []
with open('day10input.txt') as file:
	i = 0
	for line in file:
		full_input.append(line.strip())
		for j in range(len(line)):
			pipe = line[j]
			if(  pipe == "-"):
				looping[str([i,j])] = [str([i,j-1]), str([i,j+1])]
			elif(pipe == "|"):
				looping[str([i,j])] = [str([i+1,j]), str([i-1,j])]
			elif(pipe == "L"):
				looping[str([i,j])] = [str([i-1,j]), str([i,j+1])]
			elif(pipe == "J"):
				looping[str([i,j])] = [str([i-1,j]), str([i,j-1])]
			elif(pipe == "7"):
				looping[str([i,j])] = [str([i+1,j]), str([i,j-1])]
			elif(pipe == "F"):
				looping[str([i,j])] = [str([i+1,j]), str([i,j+1])]
			elif(pipe == "S"):
				starting_idex = str([i,j])
				#looping[str([i,j])] = [str([i-1,j]), str([i,j+1])]
				looping[str([i,j])] = [str([i+1,j]), str([i,j-1])]
		i+=1


last = starting_idex
current = looping[starting_idex][0]
length = 1
loop_pipes = [eval(current)]
while(current != starting_idex):
	opt1, opt2 = looping[current]
	correct_opt = ""
	if opt1 == last:
		correct_opt = opt2
	else:
		correct_opt = opt1

	temp = current
	current = correct_opt
	last = temp
	length += 1
	loop_pipes.append(eval(current))
print("part1:",length//2)

def look_lefty(hehe, a, b):
	empty = []
	if hehe == "a":
		i = b - 1
		while [a, i] not in loop_pipes:
			empty.append([a, i])
			i -= 1
	elif hehe == "b":
		i = b + 1
		while [a, i] not in loop_pipes:
			empty.append([a, i])
			i += 1
	elif hehe == "c":
		i = a + 1
		while [i, b] not in loop_pipes:
			empty.append([i, b])
			i += 1
	elif hehe == "d":
		i = a - 1
		while [i, b] not in loop_pipes:
			empty.append([i, b])
			i -= 1
	return empty

def look_left(last, current):
	a,b = current
	empty = []
	if last[0] > current[0]:
		# Going up so look left
		empty = look_lefty("a", a, b)
		if full_input[a][b] == "F":
			empty += look_lefty("d", a, b)
	elif last[0] < current[0]:
		# Going Down so look right
		empty = look_lefty("b", a, b)
		if full_input[a][b] in ["J"]:
			empty += look_lefty("c", a, b)
	elif last[1] > current[1]:
		# Going Left so look down
		empty = look_lefty("c", a, b)
		if full_input[a][b] in ["L"]:
			empty += look_lefty("a", a, b)
	elif last[1] < current[1]:
		# Going Right so look up
		empty = look_lefty("d", a, b)
		if full_input[a][b] in ["7", "S"]:
			empty += look_lefty("b", a, b)
		
	return empty

surounded_boxes = []
last = starting_idex
current = looping[starting_idex][1]
while(current != starting_idex):
	opt1, opt2 = looping[current]
	correct_opt = ""
	if opt1 == last:
		correct_opt = opt2
	else:
		correct_opt = opt1

	surounded_boxes += look_left(eval(current), eval(last))
	temp = current
	current = correct_opt
	last = temp

surounded_boxes += look_left(eval(current), eval(last))
tots = 0
for i in range(len(surounded_boxes)):
	if surounded_boxes[i] not in surounded_boxes[:i]:
		tots+=1
print("part2:", tots)