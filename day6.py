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

def calc_time(time_for_race, distance_to_beat):
	low = time_for_race
	high = 0
	for i in range(time_for_race):
		distance_for_time = i*(time_for_race - i)
		if distance_for_time > distance_to_beat:
			if i < low:
				low = i
			if i > high:
				high = i
	return max(high - low + 1, 0)

result = 1
for i in range(len(times)):
	result *= calc_time(times[i], distance[i])

print(result)
print(calc_time(true_time, true_distance))