def next_to():
	result = 0
	max_row = len(matrix)
	for i in range(max_row):
		max_column = len(matrix[i])
		for j in range(max_column):
			cell = matrix[i][j]
			taken = -1
			temp = 1
			if(cell == 0):
				adjacent = 0
				for k in range(max(0, i-1), min(i+1, max_row-2)+1):
					for l in range(max(0, j-1), min(j+1, max_column-2)+1):
						try:
							if(matrix[k][l] > 0 and matrix[k][l] != taken):
								adjacent += 1
								temp*=matrix[k][l]
								taken = matrix[k][l]
						except: 
							print(i, j, max_row, max_column)
							print(k, l)
				if adjacent == 2:
					result+=temp
	return result

values = []
matrix = [[]]
with open('day3input.txt') as f:
	for line in f:
		temp = ""
		length = 0
		for char in line:
			if char.isnumeric():
				temp+=char
				length += 1
			else:
				if(temp != ""):
					for i in range(length):
						matrix[-1].append(int(temp))
					temp = ""
					length = 0
					
				if(char == "*"):
					matrix[-1].append(0)
				else:
					matrix[-1].append(-1)
		if(temp != ""):
			matrix[-1].append(int(temp))
			temp = ""
		matrix.append([])
print("result:", next_to())