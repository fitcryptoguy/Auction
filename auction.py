dict = {}
from replit import clear

def highest():
    highest_amount = 0
    for bidder, bid in dict.items():
        if bid > highest_amount:
            highest_amount = bid
            highest_bidder = bidder
    print(f"highest biddes is {highest_bidder} and bid amount is {highest_amount}")


while True:
    name = input("Enter your name: ")
    amount = int(input("enter your bidding amount: "))
    dict[name] = amount

    user = input("Are there any other bidders: ")


    if user.lower() == "n":
        highest()
        break

    elif user.lower() == "y":
        clear()


