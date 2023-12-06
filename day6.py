import re

times=[]
distance = []
with open('day6input.txt') as f:
	for line in f:
		if line.startswith("Time"):
			times = [int(num) for num in re.findall(r'\d+', line)]
			true_time = re.findall(r'\d+', line)
			temp = ""
			for num in true_time:
				temp+=num
			true_time = int(temp)
		if line.startswith("Distance"):
			distance = [int(num) for num in re.findall(r'\d+', line)]
			true_distance = re.findall(r'\d+', line)
			temp = ""
			for num in true_distance:
				temp+=num
			true_distance = int(temp)

def dist_time(time_for_race, charge_time):
	return charge_time*(time_for_race - charge_time)

def calc_time(time_for_race, distance_to_beat):
	lowering_range = [0, time_for_race]
	while(lowering_range[0] != lowering_range[1]-1):
		temp = (lowering_range[0]+lowering_range[1])//2
		if dist_time(time_for_race, temp) > distance_to_beat:
			lowering_range[1] = temp
		else:
			lowering_range[0] = temp

	increasing_range = [0, time_for_race]
	while(increasing_range[0] != increasing_range[1]-1):
		temp = (increasing_range[0]+increasing_range[1])//2
		if dist_time(time_for_race, temp) < distance_to_beat:
			increasing_range[1] = temp
		else:
			increasing_range[0] = temp

	return max(increasing_range[0] - lowering_range[1] + 1, 0)

result = 1
for i in range(len(times)):
	result *= calc_time(times[i], distance[i])

print(result)
print(calc_time(true_time, true_distance))