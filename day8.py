###############################################################
############# Taken from the net because I'm lazy #############
def calculate_prime_factors(N):
	prime_factors = []
	while N % 2 == 0:
		prime_factors.append(2)
		N = N // 2
		if N == 1:
			return prime_factors
	for factor in range(3, N + 1, 2):
		if N % factor == 0:
			while N % factor == 0:
				prime_factors.append(factor)
				N = N // factor
				if N == 1:
					return prime_factors

###############################################################


file = open('day8input.txt')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines if line.strip() != '']

sequence = [0 if char == 'L' else 1 for char in lines[0].strip()]
directions = {}
for direction in lines[1:]:
	spot1 = len('XXX = (')
	a = direction[spot1: spot1+3]
	spot2 = len('XXX = (XXX, ')
	b = direction[spot2: spot2+3]
	directions[direction[:3]] = [a, b]

# For part 1
# currents = ['AAA']
# end = 'ZZZ'

# For part 2
currents = [position for position in directions if position.endswith('A')]
end = 'Z'
steps_needed = []
prime_factors_of_each = []
for current in currents:
	i=0
	steps = 0
	while(not current.endswith(end)):
		current = directions[current][sequence[i]]
		steps += 1
		i = steps % len(sequence)
	steps_needed.append(steps)
	prime_factors_of_each.append(calculate_prime_factors(steps))

start = prime_factors_of_each[0].copy()
for primes in prime_factors_of_each[1:]:
	exits = start.copy()
	for prime in primes:
		if prime in exits:
			exits.remove(prime)
		else:
			start.append(prime)

tots = 1
for i in start:
	tots *= i

print(tots)