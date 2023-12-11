galaxy_map = []
with open("day11input.txt") as file:
	for line in file:
		galaxy_map.append(line.strip())

# Finding expanding rows and columns
column_to_be_expanded = [True for x in range(len(galaxy_map[0]))]
rows_to_be_expanded = [True for x in range(len(galaxy_map))]
for i in range(len(galaxy_map)):
	for j in range(len(galaxy_map[i])):
		if galaxy_map[i][j] != ".":
			column_to_be_expanded[j] = False
			rows_to_be_expanded[i] = False

# Expand Coulmns
galaxy_map_with_columns = [x for x in galaxy_map]
for i in range(len(galaxy_map)):
	intern_j = 0
	for j in range(len(galaxy_map[i])):
		if(column_to_be_expanded[j]):
			galaxy_map_with_columns[i] = galaxy_map_with_columns[i][:intern_j] + "." + galaxy_map_with_columns[i][intern_j:]
			intern_j += 1
		intern_j += 1

# Expand Rows
new_galaxy = []
for i in range(len(galaxy_map_with_columns)):
	new_galaxy.append(galaxy_map_with_columns[i])
	if rows_to_be_expanded[i]:
		new_galaxy.append(galaxy_map_with_columns[i])

# Find the galaxies
cords_for_galaxies = []
for i in range(len(galaxy_map)):
	for j in range(len(galaxy_map[i])):
		if galaxy_map[i][j] == "#": cords_for_galaxies.append([i,j])


def dist(a, b):
	x = abs(a[0]-b[0])
	y = abs(a[1]-b[1])
	return x + y

def dis(a, b):
	row_mov = 0
	for i in range(a[0], b[0]):
		if rows_to_be_expanded[i]:
			row_mov += 1000000
		else:
			row_mov += 1
	
	column_move = 0
	for i in range(a[1], b[1]):
		if column_to_be_expanded[i]:
			column_move += 1000000
		else:
			column_move += 1
	return row_mov + column_move

def dist2(a, b):
	temp1 = [a[0], b[0]]
	if a[0] > b[0]:
		temp1=[b[0], a[0]]
	temp2 = [a[1], b[1]]
	if a[1] > b[1]:
		temp2=[b[1], a[1]]
	
	return dis([temp1[0], temp2[0]], [temp1[1], temp2[1]])

distance_matrix = []
for i in range(len(cords_for_galaxies)):
	for j in range(len(cords_for_galaxies[:i])):
		distance_matrix.append(dist(cords_for_galaxies[i], cords_for_galaxies[j]))

distance_matrix_2 = []
for i in range(len(cords_for_galaxies)):
	for j in range(len(cords_for_galaxies[:i])):
		distance_matrix_2.append(dist2(cords_for_galaxies[i], cords_for_galaxies[j]))


print(sum(distance_matrix))
print(sum(distance_matrix_2))