conversion = []
seeds = []
seedsb = []
with open('day5input.txt') as f:
	for line in f:
		if "map" in line:
			conversion.append([])
		elif line.startswith("seeds"):
			split_line = line.split(" ")[1:]
			seeds = [int(seed) for seed in split_line]
			i = 0
			temp = 0
			for seed in seeds:
				if i % 2 == 0:
					temp = seed
				else:
					seedsb.append([temp, seed])
				i+=1
		elif len(line) <= 2:
			continue
		else:
			split_line = line.split(" ")
			numbers = [int(number) for number in split_line]
			# My conversions are of the format [start index, range, change]
			conversion[-1].append([numbers[1], numbers[2], numbers[0] - numbers[1]])

#Part1
result_location = []
for seed in seeds:
	print("seed:", seed, end="")
	# Somithing is wrong don't know... It gave me the right answer, so don't care
	for mapping in conversion:
		curr_seed=seed
		for single_map in mapping:
			temp = seed - single_map[0]
			if temp < 0:continue
			elif temp < single_map[1]: 
				curr_seed = seed + single_map[2]
		print(",",seed, end="")
		seed = curr_seed
	print()
	result_location.append(seed)


#Part2 (If you had to split the seeds up into )
result_locationb = []
for mapping in conversion:
	#print(seedsb)
	#print(mapping)
	#print("#"*60)
	next_seed = []
	while(len(seedsb) > 0):
		seed = seedsb.pop(0)
		change = False
		for single_map in mapping:
			temp_begin = seed[0] - single_map[0]
			temp_end = temp_begin + seed[1]
			if temp_end <= 0:continue
			elif temp_begin < 0:
				change = True 
				seedsb.append([seed[0], abs(temp_begin)])
				if temp_end < single_map[1]:
					next_seed.append([single_map[0]+single_map[2], temp_end+1])
				else:
					next_seed.append([single_map[0]+single_map[2], single_map[1]])
					seedsb.append([single_map[0]+single_map[1], seed[1]-(single_map[1]+abs(temp_begin))])
			elif temp_end <= single_map[1]:
				change = True
				next_seed.append([seed[0]+single_map[2], seed[1]])
			elif temp_begin < single_map[1]:
				change = True
				amount_in = single_map[1] - temp_begin
				#print(seed,temp_begin, single_map, amount_in)
				next_seed.append([seed[0]+single_map[2], amount_in])
				seedsb.append([seed[0]+(amount_in), seed[1]-amount_in])
		if not change:
			next_seed.append(seed)
	seedsb = next_seed.copy()

print(min(result_location))
mini = max(result_location)
for i in range(len(seedsb)):
	if seedsb[i][0] < mini:
		mini = seedsb[i][0]
print(mini)