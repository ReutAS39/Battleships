'''
all_sticks = 10
while all_sticks > 0:
    player_1 = int(input('Первый:  '))
    if player_1 < 4:
        all_sticks -= player_1
    else:
        print('Неверное значение')
        continue
    print(all_sticks)
    if all_sticks <= 0:
        print('player 1 has lost')
    player_2 = int(input('Второй:  '))
    if player_2 < 4:
        all_sticks -= player_2
    else:
        print('Неверное значение')
        continue
    print(all_sticks)
    if all_sticks <= 0:
        print('player 2 has lost')
'''
'''
number_of_sticks = 10
player_turn = 1
def can_take(sticks):
    return sticks >= 1 and sticks <= 3
def switch_player_turn(turn):
    return 1 if player_turn == 2 else 2
def end_of_game(sticks):
    return number_of_sticks <= 0
while (not end_of_game(number_of_sticks)):
    print(f'How many sticks you take? Remaining {number_of_sticks}')
    taken = int(input())

    if not can_take(taken):
        print(f'You tried to take {taken}. Allowed to take 1, 2, 3 sticks.')
        continue

    number_of_sticks -= taken
    print(f'Sticks taken: {taken}\n')

    if end_of_game(number_of_sticks):
        print(f'No more sticks in the game. \nPlayer {player_turn} has lost.')
        break

    player_turn = switch_player_turn(player_turn)

'''
board = [ ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]

def print_state(state):
    for i, c in enumerate(state):
        if (i + 1)%3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')

winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

def get_winner(state, combinations):
    for x, y, z in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
            return state[x]
    return ''

def play_game(board):
    current_sign = 'X'
    while (get_winner(board, winning_combinations)==''):
        index = int(input(f'Where do you want to draw {current_sign}?'))
        board[index] = current_sign

        print_state(board)

        winner_sign = get_winner(board, winning_combinations)
        if winner_sign != '':
            print(f'We have a winner {winner_sign}')

        current_sign = 'X' if current_sign == 'O' else 'O'

play_game(board)