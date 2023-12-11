looping = {}
starting_idex = []
with open('day10input.txt') as file:
	i = 0
	for line in file:
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
				looping[str([i,j])] = [str([i-1,j]), str([i,j+1])]
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
print(length//2)

maxi = 140
water_flush    =   [[x, 0] for x in range(maxi+1)]
water_flush.append([[0, x] for x in range(maxi+1)])
water_flush.append([[0, x] for x in range(maxi+1)])
water_flush.append([[x, maxi] for x in range(maxi+1)])
water = []
while(len(water_flush) > 0):
	current = water_flush.pop(0)
	if water_can_penetrate(current):
		water.append(current)
