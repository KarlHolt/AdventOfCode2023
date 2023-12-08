from functools import cmp_to_key

def count(hand):
	elem = {}
	for char in hand:
		if char in elem:
			elem[char] += 1
		else: elem[char] = 1
	return [elem[x] for x in elem]

def compare(a, b):
	rank = "23456789TJQKA"
	a_best = True
	if a[0] == b[0]:
		for i in range(len(a[1])):
			card_a = a[1][i]
			card_b = b[1][i]
			if card_a != card_b:
				if rank.index(card_a) < rank.index(card_b):
					a_best = False
				break
	# I know that the first index is the highest otherwise I had to use max here
	if a[0][0] < b[0][0]:
		a_best = False
	elif a[0][0] == b[0][0]:
		# I know that the second index will be the second highest
		if(a[0][1] < b[0][1]):
			a_best = False
	return 1 if a_best else -1

def compare2(a, b):
	rank = "J23456789TQKA"
	a_best = True
	if a[0] == b[0]:
		for i in range(len(a[1])):
			card_a = a[1][i]
			card_b = b[1][i]
			if card_a != card_b:
				if rank.index(card_a) < rank.index(card_b):
					a_best = False
				break
	# I know that the first index is the highest otherwise I had to use max here
	else:
		if a[0][0] < b[0][0]:
			a_best = False
		elif a[0][0] == b[0][0]:
			# I know that the second index will be the second highest
			if(a[0][1] < b[0][1]):
				a_best = False
	return 1 if a_best else -1

values = []
with open('day7input.txt') as file:
	for line in file:
		try:
			hand,bet = line.split(" ")
			hand_list = [x for x in hand if x!='J']
			hand_count = count(hand_list)
			hand_count.append(0)
			hand_count.sort(reverse=True)
			hand_count[0]+=5-len(hand_list)
			hand_count = [x for x in hand_count if x != 0]
			values.append([hand_count.copy(), hand, int(bet)])
		except:
			continue

values.sort(key=cmp_to_key(compare2))
tots = 0
for i in range(len(values)):
	tots += values[i][2]*(i+1)
print(tots)