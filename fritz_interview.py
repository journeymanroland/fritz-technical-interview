# Lucky Dollar Store Coding Challenge
import random
names = ["Eric", "Chris", "Dan", "Jameson"]
		

def record_customer_purchase(customer):
     # Fill this in
     print("- Added new raffle ticket for \"%s\"" % customer)
     return customer


def can_win(customer, pool):
	if not pool:  
		return True
	elif customer in pool.keys():
		if pool[customer] == 0:
			return True
	elif customer not in pool.keys():
		return True
	return False


def run_weekly_raffle(num_winners, num_purchases):
	# pick winner(s)
	pool = []
	winning_customer = []
	for n in range(0, num_purchases):
		customer_index = random.randrange(0, len(names))
		pool.append(record_customer_purchase(names[customer_index]))
	
	for i in range(0, num_winners):
		winner_index = random.randrange(0, len(pool))
		winner = pool[winner_index]
		winning_customer.append(winner)
	return winning_customer

def main():
	pool = []
	num_drawings = 6
	cant_win_again = {}
	for i in range(1, num_drawings + 1):	
		print("Raffle Drawing %d" % i)
		num_purchases = random.randrange(1,5)
		winners = list(set(run_weekly_raffle(2, num_purchases))) # same winner can't win in same drawing
		print("- Picking the weekly winner….", end = " ")
		# how many winners to print
		if len(winners) == 1 and can_win(winners[0], cant_win_again):
			print(winners[0])
			cant_win_again.update({winners[0]:3})
		elif len(winners) > 1:
			# for j in range(0, len(winners)-1):
			# 	if can_win(winners[j]):
			# 		pass
			# 	print(winners[j], end = " & ")
			# 	#winners[j].win()
			# print(winners[len(winners) - 1])
			for winner in winners:
				if can_win(winner, cant_win_again):
					print(winner)
					cant_win_again.update({winner:3})
		else:
			print("No one :(")
		# decrement number of raffles left until winner can win again
		for c in cant_win_again:
			if cant_win_again[c] == 0:
				cant_win_again[c] = 3
			else:
				cant_win_again[c] = cant_win_again[c] - 1
if __name__ == '__main__':
	main()
