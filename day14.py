rocks = []
with open("day14input.txt") as file:
	for line in file:
		rocks.append(line.strip())

def rotate(rocks, rotations):
	if rotations == 1:
		new_rocks = [["" for x in range(len(rocks))] for y in range(len(rocks[0]))]
		for i in range(len(rocks)):
			for j in range(len(rocks[i])):
				new_rocks[j][len(rocks)-1-i] = rocks[i][j]
	elif rotations == 2:
		new_rocks = [["" for x in range(len(rocks[0]))] for y in range(len(rocks))]
		for i in range(len(rocks)):
			for j in range(len(rocks[i])):
				new_rocks[i][j] = rocks[len(rocks) - i - 1][len(rocks[i]) - j - 1]
	elif rotations == 3:
		temp = rotate(rocks, 2)
		return rotate(temp, 1)
	hehe = []
	for y in new_rocks:
		temp = ""
		for x in y:
			temp+=x
		hehe.append(temp)
	return hehe


def rocks_roll(direction, rocks):
	if direction == "NORTH":
		for j in range(len(rocks[0])):
			place = False
			for i in range(len(rocks)):
				if rocks[i][j] == "." and not place:
					next_place = i
					place = True
				if rocks[i][j] == "O" and place:
					rocks[next_place] = rocks[next_place][:j] + "O" + rocks[next_place][j+1:]
					rocks[i] = rocks[i][:j] + "." + rocks[i][j+1:]
					next_place = next_place + 1
				if rocks[i][j] == "#":
					place = False
	elif direction == "WEST":
		temp = rotate(rocks, 1)
		hehe = rocks_roll("NORTH", temp)
		return rotate(hehe, 3)
	elif direction == "SOUTH":
		temp = rotate(rocks, 2)
		hehe = rocks_roll("NORTH", temp)
		return rotate(hehe, 2)
	elif direction == "EAST":
		temp = rotate(rocks, 3)
		hehe = rocks_roll("NORTH", temp)
		return rotate(hehe, 1)

	return rocks

def calc_score(rocks):
	tots = 0
	for i in range(len(rocks)):
		score_for_row = len(rocks) - i
		rocks_n = 0
		for j in range(len(rocks[i])):
			if rocks[i][j] == "O":
				rocks_n += 1
		tots += score_for_row * rocks_n
	return tots


rolls = []
repeat = 0
lol_big = 1000000000
for i in range(lol_big):
	rocks = rocks_roll("NORTH", rocks)
	rocks = rocks_roll("WEST", rocks)
	rocks = rocks_roll("SOUTH", rocks)
	rocks = rocks_roll("EAST", rocks)
	if rocks in rolls:
		repeat = [rolls.index(rocks)+1, i-rolls.index(rocks)]
		break
	rolls.append(rocks.copy())

for i in range(((lol_big-repeat[0]) % repeat[1])):
	rocks = rocks_roll("NORTH", rocks)
	rocks = rocks_roll("WEST", rocks)
	rocks = rocks_roll("SOUTH", rocks)
	rocks = rocks_roll("EAST", rocks)

# for x in rolls:
# 	for y in x:
# 		for z in y:
# 			print(z, end="")
# 		print()
# 	print()
# 	print()
print(calc_score(rocks))

