from string import digits
import random

start = "         "
line = "---------"
mat = [list(start[:3]), list(start[3:6]), list(start[6:])]

def print_mat(field):
    print(line)
    print("|", mat[0][0], mat[0][1], mat[0][2], "|")
    print("|", mat[1][0], mat[1][1], mat[1][2], "|")
    print("|", mat[2][0], mat[2][1], mat[2][2], "|")
    print(line)

print_mat(mat)

win_x = 0
win_o = 0
def win_state():
    global win_x
    global win_o
    if (mat[0][0] == mat[0][1] == mat[0][2] == "X" or
       mat[1][0] == mat[1][1] == mat[1][2] == "X" or
       mat[2][0] == mat[2][1] == mat[2][2] == "X" or
       mat[0][0] == mat[1][0] == mat[2][0] == "X" or
       mat[0][1] == mat[1][1] == mat[2][1] == "X" or
       mat[0][2] == mat[1][2] == mat[2][2] == "X" or
       mat[0][0] == mat[1][1] == mat[2][2] == "X" or
       mat[2][0] == mat[1][1] == mat[0][2] == "X"):
       win_x = 1
    if (mat[0][0] == mat[0][1] == mat[0][2] == "O" or
       mat[1][0] == mat[1][1] == mat[1][2] == "O" or
       mat[2][0] == mat[2][1] == mat[2][2] == "O" or
       mat[0][0] == mat[1][0] == mat[2][0] == "O" or
       mat[0][1] == mat[1][1] == mat[2][1] == "O" or
       mat[0][2] == mat[1][2] == mat[2][2] == "O" or
       mat[0][0] == mat[1][1] == mat[2][2] == "O" or
       mat[2][0] == mat[1][1] == mat[0][2] == "O"):
       win_o = 2
    return win_o + win_x

def check_coord(coord):
    global coord_list
    global j
    global i
    if len(coord) != 3 or coord[1] != " ":
        return "You should enter numbers!"
    coord_list_string = coord.split()
    if coord_list_string[0] not in digits or coord_list_string[1] not in digits:
        return "You should enter numbers!"
    coord_list = [int(x) for x in coord_list_string]
    j = 3 - coord_list[1]
    i = coord_list[0] - 1
    if coord_list[0] > 3 or coord_list[1] > 3:
        return "Coordinates should be from 1 to 3!"
    if mat[j][i] in ["X", "O"]:
        return "This cell is occupied! Choose another one!"     

def game_state():
    if win == 1:
        return "X wins"
    elif win == 2:
        return "O wins"
    elif any(" " in part for part in mat):
        return "Game not finished"
    else:
        return "Draw"
        
def user_player(turn):
    global x_turn
    user_move = input("Enter the coordinates: ")      
    while True:
        check = check_coord(user_move)
        if check:
            print(check_coord(user_move))
            user_move = input("Enter the coordinates: ")   
        else:
            mat[j][i] = turn
            print_mat(mat)
            if x_turn == 0:
                x_turn = 1
            elif x_turn == 1:
                x_turn = 0
            break


def win_moves(mat):
    
    tmat = [[mat[0][0], mat[1][0], mat[2][0]], [mat[0][1], mat[1][1], mat[2][1]], [mat[0][2], mat[1][2], mat[2][2]]]
    dmat = [[mat[0][0], mat[1][1], mat[2][2]], [mat[0][2], mat[1][1], mat[2][0]]]

    win_moves = []
    
    for i in mat:
        if (i.count('X') == 2 or i.count('O') == 2) and i.count(' ') > 0:
            ii = 3 - mat.index(i) 
            jj = i.index(' ') + 1
            win_moves.append(f'{mat[3 - ii][jj - 2]} {jj} {ii}')

    for j in tmat:
        if (j.count('X') == 2 or j.count('O') == 2) and j.count(' ') > 0:
            jj = tmat.index(j) + 1 
            ii = 3 - j.index(' ')
            win_moves.append(f'{mat[2 - ii][jj - 1]} {jj} {ii}')

    if dmat[0].count(' ') == 1:
        if dmat[0].count('X') == 2:
            if dmat[0].index(' ') == 0:
                win_moves.append(f'X 1 3')
            elif dmat[0].index(' ') == 1:
                win_moves.append(f'X 2 2')
            else:
                win_moves.append(f'X 3 1')
        elif dmat[0].count('O') == 2:
            if dmat[0].index(' ') == 0:
                win_moves.append(f'O 1 3')
            elif dmat[0].index(' ') == 1:
                win_moves.append(f'O 2 2')
            else:
                win_moves.append(f'O 3 1')
    if dmat[1].count(' ') == 1:
        if dmat[1].count('X') == 2:
            if dmat[1].index(' ') == 0:
                win_moves.append(f'X 3 3')
            elif dmat[1].index(' ') == 1:
                win_moves.append(f'X 2 2')
            else:
                win_moves.append(f'X 1 1')
        elif dmat[1].count('O') == 2:
            if dmat[1].index(' ') == 0:
                win_moves.append(f'O 3 3')
            elif dmat[1].index(' ') == 1:
                win_moves.append(f'O 2 2')
            else:
                win_moves.append(f'O 1 1')
    return win_moves 

def easy(turn):
    global x_turn
    print('Making move level "easy"')
    easy_move = '4 4'      
    while True:
        check_easy = check_coord(easy_move)
        if check_easy:
            easy_move = random.choice(['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3'])   
        else:
            mat[j][i] = turn
            print_mat(mat)
            if x_turn == 0:
                x_turn = 1
            elif x_turn == 1:
                x_turn = 0
            break
            
def medium(turn):
    global x_turn
    print('Making move level "medium"')
    medium_move = '4 4'      
    while True:
        win_move = win_moves(mat)
        wininig = 0
        if win_move:
            for move in win_move:
                if turn in move:
                    medium_move = move[2:]
                    wininig = 1
                    break
            if wininig == 0:    
                medium_move = win_move[0][2:]
        check_medium = check_coord(medium_move)     
        if check_medium:
            medium_move = random.choice(['1 1', '1 2', '1 3', '2 1', '2 2', '2 3', '3 1', '3 2', '3 3'])   
        else:
            mat[j][i] = turn
            print_mat(mat)
            if x_turn == 0:
                x_turn = 1
            elif x_turn == 1:
                x_turn = 0
            break
            
def hard(turn):
    global x_turn
    print('Making move level "hard"')
    hard_move = '2 2'     
    while True:
        win_move = win_moves(mat)
        wininig = 0
        if win_move:
            for move in win_move:
                if turn in move:
                    hard_move = move[2:]
                    wininig = 1
                    break
            if wininig == 0:    
                hard_move = win_move[0][2:]
        else:
            if mat[1][1] == ' ':
                hard_move = '2 2'
            elif mat[0][0] == ' ':
                hard_move = '1 3'
            elif mat[0][2] == ' ':
                hard_move = '3 3'
            elif mat[2][0] == ' ':
                hard_move = '1 1'
            elif mat[2][2] == ' ':
                hard_move = '3 1'
        check_hard = check_coord(hard_move)     
        if check_hard:
            hard_move = random.choice(['1 2', '2 1', '2 2', '2 3', '3 2'])   
        else:
            mat[j][i] = turn
            print_mat(mat)
            if x_turn == 0:
                x_turn = 1
            elif x_turn == 1:
                x_turn = 0
            break

while True:
    commands = ['user', 'easy', 'medium', 'hard']
    command = input('Input command: ')
    command_list = command.split()
    x_turn = 1
    if command_list:
        if len(command_list) == 1:
            if command_list[0] == 'exit':
                break
            else:
                print('Bad parameters!')
                continue
        elif len(command_list) == 3:
            if command_list[0] == 'start':
                if command_list[1] in commands and command_list[2] in commands:
                    player_1 = command_list[1]
                    player_2 = command_list[2]
                    
                    
                    while True:
                        win = win_state()
                        state = game_state()
                        if state == "Game not finished":
                                
                            if x_turn == 1:
                                turn = 'X'
                                if player_1 == 'easy':
                                    easy(turn)
                                elif player_1 == 'user':
                                    user_player(turn)
                                elif player_1 == 'medium':
                                    medium(turn)
                                elif player_1 == 'hard':
                                    hard(turn)  
                            else:
                                turn = 'O'
                                if player_2 == 'easy':
                                    easy(turn)
                                elif player_2 == 'user':
                                    user_player(turn)
                                elif player_2 == 'medium':
                                    medium(turn)
                                elif player_2 == 'hard':
                                    hard(turn)       
                        else:
                            break
                    print(state)
                    mat = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
                    win_x = 0
                    win_o = 0
                
                else:
                    print('Bad parameters!')
                    continue
            else:
                print('Bad parameters!')
                continue
        else:
            print('Bad parameters!')
            continue