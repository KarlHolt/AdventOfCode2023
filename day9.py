def main():
	readings = []
	with open('day9input.txt') as file:
		for line in file:
			readings.append([int(number) for number in line.split(" ") if line != ""])

	next_values = []
	previuos_values = []
	for reading in readings:
		next_values.append(predict_next_value(reading))
		previuos_values.append(predict_next_value(reading[::-1]))
	print(sum(next_values))
	print(sum(previuos_values))

def predict_next_value(reading):
	history = [reading]
	while(not only_zeros(history[-1])):
		history.append(predict_next_row(history[-1]))

	new_values = [0]
	for i in range(2,len(history)+1):
		new_values.append(history[-i][-1]+new_values[-1])
	
	return new_values[-1]

def only_zeros(list):
	for elem in list:
		if elem != 0:
			return False
	return True

def predict_next_row(current_row):
	next_row = []
	for i in range(1, len(current_row)):
		next_row.append(current_row[i] - current_row[i-1])
	return next_row

main()