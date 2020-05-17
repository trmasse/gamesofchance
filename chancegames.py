#Codecademy Games of Chance Project
#Started 5/17/2020

import random

money = 100

#generates a random number between 1 & 10 (inclusive)
#num = random.randint(1, 10)

def coin_flip(balance):
    bet = setbet(balance)
    guess = int(input("Heads(1) or Tails(2)? "))
    coin = random.randint(1, 2)
    if coin == 1:
        print("The coin came up Heads.")
    else:
        print("The coin came up Tails.")
    if guess == coin:
        balance += bet
        print("You won {} dollars!".format(bet))
    else:
        balance -= bet
        print("You lost {} dollars!".format(bet))
    #Heads = 1, Tails = 2
    print("Now you have ${}.\n".format(balance))
    return balance
 
def chohan(balance):
    bet = setbet(balance)
    guess = int(input("Odd(1) or Even(2)? "))
    dicea = random.randint(1, 6)
    diceb = random.randint(1, 6)
    print("The dice rolled {0} and {1}, summing to {2}.".format(dicea, diceb, dicea+diceb))
    check = 2 if (dicea + diceb) % 2 == 0 else 1
    if guess == check:
        print("You won {} dollars!".format(bet))
        balance += bet
    else:
        print("You lost {} dollars.".format(bet))
        balance -= bet
    print("Now you have ${} dollars.\n".format(balance))
    return balance
    
def carddraw(balance):
    bet = setbet(balance)
    cards = []
    #2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14
    for count1 in range(4):
        for count2 in range(2, 15):
            cards.append(count2)
    playeridx = random.randint(0, 51)
    playerdraw = cards.pop(playeridx)
    compidx = random.randint(0, 50)
    compdraw = cards.pop(compidx)
    print("You drew a {0}. The dealer drew a {1}.".format(cardc(playerdraw), cardc(compdraw)))
    if playerdraw > compdraw:
        print("You won {} dollars!.".format(bet))
        balance += bet
    elif compdraw > playerdraw:
        print("You lost {} dollars.".format(bet))
        balance -= bet
    else:
        print("It's a tie.")
    print("Now you have ${} dollars.\n".format(balance))
    return balance

def cardc(card):
    if card == 11:
        return "J"
    elif card == 12:
        return "Q"
    elif card == 13:
        return "K"
    elif card == 14:
        return "A"
    else:
        return card
        
def roulette(balance):
    bet = setbet(balance)
    guess = input("Enter a number 0-36, 00, Even, or Odd: ")
    if guess == "Even" or guess == "Odd":
        guess = guess.lower()
    elif guess == "00":
        pass
    else:
        guess = int(guess)
    pocket = random.randint(0, 37) - 1
    if pocket == -1:
        print("The ball landed on 00.")
    else:
        print("The ball landed on {}.".format(pocket))
    if type(guess) == int:
        if guess == pocket:
            print("You won {} dollars!.".format(bet * 35))
            balance += (bet * 35)
        else:
            print("You lost {} dollars.".format(bet))
            balance -= bet
    else:
        if guess == "00" and pocket == -1:
            print("You won {} dollars!.".format(bet * 35))
            balance += (bet * 35)
        elif guess == "even" and pocket % 2 == 0:
            print("You won {} dollars!.".format(bet))
            balance += bet
        elif guess == "odd" and pocket % 2 != 0:
            print("You won {} dollars!.".format(bet))
            balance += bet
        else:
            print("You lost {} dollars.".format(bet))
            balance -= bet
    print("Now you have {} dollars.\n".format(balance))
    return balance

#testing
#coin_flip(money)
#chohan(money)
#carddraw(money)
#roulette(money)

def printgames(games):
    for game in games:
        print(game)
        
def setbet(balance):
    bet = int(input("How much do you want to bet? You have ${}: ".format(balance)))
    if bet <= 0:
        print("You have to bet at least $1.")
        return setbet(balance)
    elif bet > balance:
        print("You can't bet more than your current balance.")
        return setbet(balance)
    else:
        return bet

#game
gamelist = ["1: Coin Flip", "2: Cho-Han", "3: Card Draw", "4: Roulette", "5: Leave"]
print("Welcome to the Casino! You start with $100!")

while(True):
    if money <= 0:
        print("You're all out of money and have to leave. Come again soon!")
        break
    else:
        print("Which game would you like to play?")
        printgames(gamelist)
        while(True):
            try:
                choice = int(input("Enter 1-5: "))
                break
            except ValueError:
                print("You must enter 1-5.")
        if choice == 1:
            money = coin_flip(money)
        elif choice == 2:
            money = chohan(money)
        elif choice == 3:
            money = carddraw(money)
        elif choice == 4:
            money = roulette(money)
        elif choice == 5:
            print("You leave the casino with {} dollars. Come again soon!".format(money))
            break
        