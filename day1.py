values = []
with open('day1input.txt') as f:
	for line in f:
		first = False
		last = ""
		temp = ""
		digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
		for i,digit in enumerate(digits):
			line = line.replace(digit, digit+str(i+1)+digit)
		for char in line:
			if char.isnumeric():
				if not first:
					temp += char
					first = True
				last = char
		temp += last
		values.append(int(temp))

print(sum(values))
