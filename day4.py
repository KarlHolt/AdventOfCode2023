values = 0
valuesb = 0
rounds=1
max_balls = [12, 13, 14]
cards = {}
my_cards = []
with open('day4input.txt') as f:
	for line in f:
		card,numbers_ = line.split(":")
		card = card.split(" ")[-1]
		winning,numbers = numbers_[:-1].split("|")
		winning = winning.split(" ")
		numbers = numbers.split(" ")
		numbers = [i for i in numbers if i != ""]
		winning = [i for i in winning if i != ""]
		temp = 0
		tempest = 0
		for num in numbers:
			if num in winning:
				tempest += 1
				if(temp == 0):
					temp = 1
				else:
					temp *= 2
		cards[card] = tempest
		my_cards.append(card)
		values += temp

copies = [1 for card in cards]
for card in cards:
	number_value = int(card)
	for c in range(cards[card]):
		copies[number_value + c] += copies[number_value-1]

print(values)
print(sum(copies))