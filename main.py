from replit import clear

from art import logo

print(logo)
bids = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
	highest_bid = 0
	# bidding_record =  {"Yuri": 150, "D'ette: 23"}
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner}, with a bid of ${highest_bid}")


while not bidding_finished:
	name = input("what's your name?: ")
	price = int(input("What's your bid price? $"))
	bids[name] = price
	should_continue = input("Is there any other bidders? Type 'yes' or 'no'. ")
	if should_continue == "no":
		bidding_finished = True
		find_highest_bidder(bids)
	elif should_continue == "yes":
		clear() 

	


	

