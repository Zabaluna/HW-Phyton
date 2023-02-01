# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#   Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""
# оставляем для 2 ишрока 1 конфетуБ чтоб 1 выиграл

# со второго хода^
# m + 1 = 28 +1 =29

import random


def take_sweet( player ):
    global sweets
    taken_sweets = int( input( f'{ list_players[player] } take your sweets: '))
    while taken_sweets < 1 or taken_sweets > 28 or taken_sweets > sweets:
        print('Try agan')
        taken_sweets = int( input( f'{ list_players[player] } take your sweets: '))
    else:
        sweets -= taken_sweets


sweets = 100

print('Welcome to our SWEETS game!')

first_player = input('Print 1st player name:')
second_player = input('Print 2d player name:')

list_players = [first_player, second_player]
# list_players[0] = random.choice(list_players)
# if list_players[0] == first_player:
#     list_players[1] == second_player
# else: list_players[1] == first_player
# print(f'The first turn is given to the player by name {list_players[0]}')


print(f'The first turn is given to the player by name { random.choice(list_players) }')

while sweets > 0:
    for player in range(len(list_players)):
        take_sweet( player )
        if sweets == 0:
            print(f'The winner is { list_players[player] }')
            break
        print(f'Left on the table: {sweets}')

print('The game is over!')        

exit()
import random

# Функция random.choice() модуля random 
# возвращает один случайный элемент из непустой последовательности seq.
# Пример выбор случайного элемента из списка:
# >>> import random
# >>> lst = [1, 'a', 2, 'b', 3, 'c']
# # выбор случайного элемента из списка `lst`
# >>> random.choice(lst)
# # '3'

# # def bigchoice():
# list_players = [first_player, second_player]
# list_players[0] = random.choice(list_players)
# # if list_players[0] == first_player:
# #     list_players[1] == second_player
# # else: list_players[1] == first_player
# print(f'The first turn is given to the player by name {list_players[0]}')
# return list_players

# list_players = bigchoice()

print('Welcome to our SWEETS game!')
first_player = input('Print 1st player name:')
second_player = input('Print 2d player name:')

list_players = [first_player, second_player]
print(f'The first turn is given to the player by name {random.choice(list_players)}')

sweets = 100
taken_sweets = 0


while sweets > 0:
    taken_sweets = int( input( f'{ list_players[0] } take your sweets: '))
    while taken_sweets < 1 or taken_sweets > 28 or taken_sweets > sweets:
        print('Try agan')
        taken_sweets = int( input( f'{ list_players[0] } take your sweets: '))
    sweets -= taken_sweets
    if sweets == 0:
        print(f'The winner is {first_player}')
        break
    else: 
        print(f'Left on the table: {sweets}')
    
    taken_sweets = int(input(f'{list_players[1]} take your sweets: '))
    while taken_sweets < 0 or taken_sweets > 28 or taken_sweets > sweets:
        print('Try agan')
        taken_sweets = int(input(f'{list_players[1]} take your sweets: '))
    sweets -= taken_sweets
    if sweets == 0:
        print(f'The winner is {first_player}')
        break
    else: 
        print(f'Left on the table: {sweets}')

print('The game is over!')







