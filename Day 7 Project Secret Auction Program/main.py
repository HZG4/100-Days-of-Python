import os

def clear():
     os.system('clear')

def bid_query():
    name = input("Enter your name:")
    bid = int(input("Enter your bid amount: "))
    bidder_list[name] = bid

bidder_list = {}
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

condition = True
while condition is True:
    bid_query()
    bool = input("Are there anymore bidders? yes or no ")
    if bool == "yes":
        clear()
    elif bool == "no":
        break

highest_biddder = ""
highest_amount = 0
for bidder in bidder_list:
    if bidder_list[bidder] > highest_amount:
        highest_biddder = bidder
        highest_amount  = bidder_list[bidder]

print(f"Sold to {highest_biddder} for {highest_amount}")