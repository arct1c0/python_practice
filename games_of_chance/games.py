import random

money = 100
numbers_drawn = [0,0]

#Write your game of chance functions here
print('---------------')

def check_money(moneyAmount):
    global money
    
    if moneyAmount < 0:
        print('''You don't have enough money''')
        exit()

def coinflip(bet_amount, heads_or_tails):
    global money
    money -= bet_amount

    check_money(money)

    if random.randint(0,1) == 1:
        winner = "Heads"
    else:
        winner = 'Tails'    
    
    if heads_or_tails == winner:
        money += bet_amount * 2
        return print('You won ' + str(bet_amount*2))
    else:
        return print('You lost -' + str(bet_amount*2))

def cho_han(bet, prediction):
    global money
    money -= bet

    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    odd_even = ''

    if (dice1+dice2) % 2 == 0:
        odd_even == 'Even'
    else:
        odd_even == 'Odd'

    if prediction == odd_even:
        money += bet*2
        return print('You won ' + str(bet*2))
    else:
        return print('You lost -' + str(bet*2))

def higher_wins(bet):
    global money
    money -= bet

    check_money(money)

    card1 = random.randint(1,10)
    card2 = random.randint(1,10)

    if numbers_drawn[-2] == card1:
        card1 = random.randint(1,10)
    elif numbers_drawn[-1] == card2:
        card2 = random.randint(1,10)

    numbers_drawn.append(card1)
    numbers_drawn.append(card2)


    if card1 > card2:
        money += bet*2
        return print('You won ' + str(bet))
    elif card2 > card1:
        return print('You lost ' + str(bet))
    else:
        money += bet
        return print('It was a tie!')

def roulette(bet, prediction):
    global money
    money -= bet
    even_odd = ''

    check_money(money)

    roulette_ball = random.randint(0,36)
    if roulette_ball == prediction:
        money += bet*5
        return print('You won ' + str(bet*5))
    elif roulette_ball == 0:
        money += bet * 10
        return print('You won ' + str(bet*10))
    elif roulette_ball % 2 == 0:
        even_odd = 'Even'
    else:
        even_odd = 'Odd'

    if even_odd == prediction:
        money += bet*2
        return print('You won ' + str(bet))
    else:
        return print('You lost ' + str(bet))

#Call your game of chance functions here

coinflip(20,'Heads')
cho_han(20, 12)
higher_wins(20)
roulette(20,'Even')
print('---------------')