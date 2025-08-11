import os
import time
from art import logo
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.YELLOW + "Welcome to the secret auction program.\n")

other_bidders = True
bidders = {}

while other_bidders:
    name = input(Fore.GREEN + "What is your name?: " + Style.RESET_ALL)
    bid = int(input(Fore.MAGENTA + "What's your bid?: $" + Style.RESET_ALL))
    bidders[name] = bid

    competitors = input(Fore.BLUE + "Are there any other bidders? Type 'yes' or 'no': " + Style.RESET_ALL).lower()
    if competitors == "yes":
        time.sleep(1)
        clear()
    elif competitors == "no":
        other_bidders = False
    else:
        print(Fore.RED + "Please type a valid choice for competitors.")

# Find the highest bidder
highest_item = max(bidders, key=bidders.get)
print(Fore.CYAN + Style.BRIGHT + f"\nThe winner is {highest_item} with a bid of ${bidders[highest_item]}")
