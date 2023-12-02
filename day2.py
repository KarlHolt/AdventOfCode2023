values = 0
valuesb = 0
rounds=1
max_balls = [12, 13, 14]
with open('day2input.txt') as f:
	for line in f:
		current_balls = [0, 0, 0]
		for i, char in enumerate(line):
			if line[i:].startswith(" red"):
				j = i-1
				while(line[j].isnumeric()):
					j-=1
				j+=1
				if int(line[j:i]) > current_balls[0]:
					current_balls[0] = int(line[j:i])
			if line[i:].startswith(" green"):
				j = i-1
				while(line[j].isnumeric()):
					j-=1
				j+=1
				if int(line[j:i]) > current_balls[1]:
					current_balls[1] = int(line[j:i])
			if line[i:].startswith(" blue"):
				j = i-1
				while(line[j].isnumeric()):
					j-=1
				j+=1
				if int(line[j:i]) > current_balls[2]:
					current_balls[2] = int(line[j:i])
		hehe = True
		temp = 1
		for i in range(3):
			if(current_balls[i] > max_balls[i]):
				hehe = False
			temp = temp * current_balls[i]
		if hehe:
			values += rounds
		rounds+=1
		valuesb += temp

print(values)
print(valuesb)
