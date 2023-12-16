data = []
with open("day16input.txt") as file:
	data = []
	i = 0
	for line in file:
		line = line.strip()
		data.append([])
		for char in line:
			# Current direction [DOWN, UP, RIGHT, LEFT]
			if char == ".":
				data[i].append([["DOWN"], ["UP"], ["RIGHT"], ["LEFT"]])
			elif char == "-":
				data[i].append([["LEFT", "RIGHT"], ["LEFT", "RIGHT"], ["RIGHT"], ["LEFT"]])
			elif char == "|":
				data[i].append([["DOWN"], ["UP"], ["UP", "DOWN"], ["UP", "DOWN"]])
			elif char == "/":
				data[i].append([["LEFT"], ["RIGHT"], ["UP"], ["DOWN"]])
			else:
				# \
				data[i].append([["RIGHT"], ["LEFT"], ["DOWN"], ["UP"]])
		i+=1

# Current direction:
DOWN = 0
UP = 1
RIGHT = 2
LEFT = 3
def route(hehex,hehey, dirt):
	stack = [[x, [hehex,hehey]] for x in data[hehex][hehey][dirt]]
	visited = [[[hehex,hehey], dirt]]
	while(len(stack) > 0):
		direction, cords = stack.pop(0)
		if direction == "LEFT":
			new_cords = [cords[0], cords[1]-1]
			if new_cords[1] >= 0 and [new_cords, LEFT] not in visited:
				[stack.append([x, new_cords]) for x in data[new_cords[0]][new_cords[1]][LEFT]]
				visited.append([new_cords, LEFT])
		elif direction == "RIGHT":
			new_cords = [cords[0], cords[1]+1]
			if new_cords[1] < len(data[new_cords[0]]) and [new_cords, RIGHT] not in visited:
				[stack.append([x, new_cords]) for x in data[new_cords[0]][new_cords[1]][RIGHT]]
				visited.append([new_cords, RIGHT])
		elif direction == "DOWN":
			new_cords = [cords[0]+1, cords[1]]
			if new_cords[0] < len(data) and [new_cords, DOWN] not in visited:
				[stack.append([x, new_cords]) for x in data[new_cords[0]][new_cords[1]][DOWN]]
				visited.append([new_cords, DOWN])
		elif direction == "UP":
			new_cords = [cords[0]-1, cords[1]]
			if new_cords[0] >= 0 and [new_cords, UP] not in visited:
				[stack.append([x, new_cords]) for x in data[new_cords[0]][new_cords[1]][UP]]
				visited.append([new_cords, UP])
	real_fields = []
	for visit in visited:
		if visit[0] not in real_fields:
			real_fields.append(visit[0])
	return len(real_fields)
print("part1:",route(0,0, RIGHT))

trial = []
for i in range(len(data)):
	trial.append([i,0, RIGHT])
	trial.append([i,len(data[i])-1, LEFT])
for i in range(len(data[0])):
	trial.append([0,i, DOWN])
	trial.append([len(data)-1,i, UP])

maxi = 0
for x in trial:
	a,b,c = x
	temp = route(a,b,c)
	if temp > maxi:
		maxi = temp
		print(a,b,c)
print("part2:",maxi)