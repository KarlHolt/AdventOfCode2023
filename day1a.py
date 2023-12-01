values = []
with open('day1ainput.txt') as f:
	for line in f:
		first = False
		last = ""
		temp = ""
		line = line.replace("one", "one1one")
		line = line.replace("two", "two2two")
		line = line.replace("three", "three3three")
		line = line.replace("four", "four4four")
		line = line.replace("five", "five5five")
		line = line.replace("six", "six6six")
		line = line.replace("seven", "seven7seven")
		line = line.replace("eight", "eight8eight")
		line = line.replace("nine", "nine9nine")
		for char in line:
			if char.isnumeric():
				if not first:
					temp += char
					first = True
				last = char
		temp += last
		print(temp)
		values.append(int(temp))

print(sum(values))