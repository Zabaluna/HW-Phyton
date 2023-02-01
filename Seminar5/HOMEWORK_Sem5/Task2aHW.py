import random 


def realsweets(text):
    taken_sweets = input(f'{text}')
    while(not taken_sweets.isdigit()):
        taken_sweets = input(f'Try again. Print a number: ')
    return int(taken_sweets)

print('Welcome to our SWEETS game!')

first_player = input('Print 1st player name:')
print('You will play with "~\_(`.`)_/~" ')
bot =  "~\_(`.`)_/~"

flag = random.randint(0,1)
if flag:
    print(f'The first turn is given to the player by name: {first_player}')
else:
    print(f'The first turn is given to the player by name: {bot}')

sweets = 100


def main():
    print('Welcome to our SWEETS game!')

    first_player = input('Print 1st player name:')
    print('You will play with "~\_(`.`)_/~" ')
    bot =  "~\_(`.`)_/~"

    flag = random.randint(0,1)
    if flag:
        print(f'The first turn is given to the player by name: {first_player}')
    else:
        print(f'The first turn is given to the player by name: {bot}')

    sweets = 100
    while sweets > 0:
        
        if flag:
            taken_sweets = realsweets(f'{first_player} take your sweets: ')
            while taken_sweets < 0 or taken_sweets > 28 or taken_sweets > sweets:
                print('Try again')
                taken_sweets = realsweets(f'{first_player} take your sweets: ')
            sweets -= taken_sweets
            if sweets == 0:
                print(f'The winner is {first_player}')
                break
            else: 
                print(f'Left on the table: {sweets}')
        else:      
            taken_sweets = random.randint(1,28)
            while taken_sweets > sweets:
                taken_sweets = sweets
            print(f'"~\_(`.`)_/~" take sweets: {taken_sweets}')
            sweets -= taken_sweets
            if sweets == 0:
                print(f'The winner is {bot}')
            else:
                print(f'Left on the table: {sweets}')
        flag = not flag
    print('The game is over!')

if __name__ == "__main__":
    main()  
