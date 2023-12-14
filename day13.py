notes = []
with open("day13input.txt") as file:
	current = []
	for line in file:
		if line == "\n" and len(current) > 0:
			notes.append(current)
			current = []
		else:
			current.append(line.strip())
	if len(current) > 0:
		notes.append(current)

def count_diff(x,y):
	nums = 0
	for i in range(len(x)):
		if x[i] != y[i]:
			nums += 1
	return nums

def comp(list1, list2):
	length1 = len(list1)
	length2 = len(list2)
	# For part 1 solution just set repair = 1
	repair = 0
	if length1 == 0 or length2 == 0:
		return False
	for i in range(min(length1, length2)):
		if not list1[-(i+1)] == list2[i]:
			if count_diff(list1[-(i+1)], list2[i]) == 1 and repair == 0:
				repair = 1
				continue
			return False
	if repair == 1:
		return True
	else:
		return False

def mirror_point(note):
	x = len(note) // 2
	for i in range(len(note) - x):
		if comp(note[:x+i+1], note[x+i+1:]):
			return x+i+1
		if comp(note[:x-i+1], note[x-i+1:]):
			return x-i+1

	return -1

def transpose(note):
	result = ["" for x in range(len(note[0]))]
	for i in range(len(note)):
		for j in range(len(note[i])):
			result[j] += note[i][j]
	return result

tots = 0
for note in notes:
	temp = mirror_point(note)
	if temp == -1:
		temp = mirror_point(transpose(note))
		print("x",temp)
	else:
		print("y",temp)
		temp = temp * 100

	tots += temp
print(tots)

# 30811 < 33778 < answer part 1 < 36850