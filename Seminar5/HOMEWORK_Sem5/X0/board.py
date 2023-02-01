board = ['1', '2', '3',
         '4', '5', '6',
         '7', '8', '9']

win_con = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
           (0, 3, 6), (1, 4, 7), (2, 5, 8),
           (0, 4, 8), (2, 4, 6))

# def draw_board():
#     global board
#     print(f'{board[0]} | {board[1]} | {board[2]} |')
#     print('-----------')
#     print(f'{board[3]} | {board[4]} | {board[5]} |')
#     print('-----------')
#     print(f'{board[6]} | {board[7]} | {board[8]} |')
#     print('-----------')
# draw_board() 
  

def draw_board():
    global board
    print('-'*13)
    for i in range(3):
        print(f'| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |')
        print('-'*13)


def get_board():
    global board
    return board


def set_board(position: int, mark: str):
    global board
    board[int(position) - 1] = mark