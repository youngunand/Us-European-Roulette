import random;
import seaborn as sns
import matplotlib.pyplot as plt

def always_red(bankroll):
    bankroll = 100
    pockets = ['Red'] * 18 + ['Black'] * 18 + ['Green'] * 2

    bankroll_history = []
    while bankroll > 0 :
        roll = random.choice(pockets)
        if roll == 'Red':
            bankroll +=1
        else:
            bankroll -=1
        bankroll_history.append(bankroll)
    return bankroll_history


#Martingale-Strategy: always double your bet until you lose (long steady profits, but suddenly ending)
#Us-American Roulette
def martingale_us(bankroll):
    bet = 0.01
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0: 
        if bet > bankroll:
            bet = bankroll
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += bet
            bet = 0.01
        else:
            bankroll -= bet
            bet *=2
        bankroll_history.append(bankroll)
    return bankroll_history
    
    
#takes a Number n (x(n)) and returns the next fibonacci number
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

#Fibonacci-Strategy:
#if we lose, we move 1 n (steps) up the chain of fibonacci numbers
#if we win, we move 2 n (steps) down the sequence

def fibonacci_strategy(bankroll):
    fibonacci_number = 1
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll > 0:
        bet = fibonacci(fibonacci_number) * .01
        if bet > bankroll:
            bet = bankroll
        roll = random.choice(pockets)
        if roll == "Red":
            bankroll += bet
            fibonacci_number = max(fibonacci_number - 2, 1)
        else:
            bankroll -= bet
            fibonacci_number += 1
        bankroll_history.append(bankroll)
    return bankroll_history



#Paroli-System (Reverse Martingale)
#double the bet with every win
def reverse_martingale(bankroll):
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    bet = .01
    previous_win = False

    while bankroll > 0 :
        if(previous_win == True):
            bet = bet*2
        roll = random.choice(pockets)
        if(roll == 'Red'):
            bankroll += bet
            previous_win = True
        else:
            bankroll -=bet
            previous_win = False
        bankroll_history.append(bankroll)
    return bankroll_history


sns.set(rc={'figure.figsize':(13.7,8.27)})

for i in range(20):
    plt.plot(martingale_us(bankroll=100), linewidth=2)
    
    
plt.xlabel("Number of Games", fontsize=18, fontweight="bold")
plt.ylabel("Bankroll", fontsize=18, fontweight="bold")
plt.xticks(fontsize=16, fontweight="bold")
plt.yticks(fontsize=16, fontweight="bold")
plt.title("Us-American Martingale", fontsize=22, fontweight="bold")
plt.show()