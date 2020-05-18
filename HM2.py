def score_board(raund, players_score):
    print(f"=====Round №{raund}====")
    print("======SCORE======")
    print(f"Player || Player2\n"
          f"{players_score['Player']}      || {players_score['Player2']}")

def board(gameboard, raund, players_score):
    score_board(raund, players_score)
    print("=================")
    for i in range(3):
        print("|", gameboard[0+i*3], "|", gameboard[1+i*3], "|", gameboard[2+i*3], "|")
        print("-------------")


def tic_toc_turn(move):
    if move % 2 == 0:
        return "X"
    else:
        return "O"


def chk_board_place(place):
    if place in (set(gameboard) - {"X", "O"}) and (gameboard[place-1] != "X" or gameboard[place-1] != "O"):
        return True


def game_board_cell(gameboard, players, move):
    place = int(input(f'{players[tic_toc_turn(move)]} enter a number of place {tic_toc_turn(move)} :'))
    while not chk_board_place(place):
        print('This cell is filled')
        place = int(input('Please enter a empty number of cell : '))
    gameboard[place-1] = tic_toc_turn(move)


def chk_winner(gameboard, tic_toc):
    if gameboard[0] == gameboard[4] == gameboard[8] or gameboard[6] == gameboard[4] == gameboard[2] \
            or gameboard[0] == gameboard[1] == gameboard[2] or gameboard[3] == gameboard[4] == gameboard[5]\
            or gameboard[6] == gameboard[7] == gameboard[8] or gameboard[0] == gameboard[3] == gameboard[6]\
            or gameboard[1] == gameboard[4] == gameboard[7] or gameboard[2] == gameboard[5] == gameboard[8]:
        return True, players[tic_toc],  1
    else:
        return False, players[tic_toc],  0


gameboard = list(range(1, 10))

if input('Choose X or O for player ') == 'X':
    players = {'X': 'Player', 'O': 'Player2'}
else:
    players = {'X': 'Player2', 'O': 'Player'}

game_score = {players['X']: 0, players['O']: 0}
round_move = 1
game_round = 1
board(gameboard, game_round, game_score)

while True:
    move = round_move + game_round
    game_board_cell(gameboard, players, move)
    board(gameboard, game_round, game_score)
    if chk_winner(gameboard, tic_toc_turn(move))[0]:
        print(f"{players[tic_toc_turn(move)]} won a round")
        game_score[players[tic_toc_turn(move)]] += 1
        score_board(game_round, game_score)
        if input('Would you like to continue press Y, else any other key: ') == 'Y':
            game_round += +1
            round_move = 1
            gameboard = list(range(1, 10))
            board(gameboard, game_round, game_score)
            continue
        else:
            print("====The End====")
            break
    if round_move == 9:
        print("======DRAW=======")
        score_board(game_round, game_score)
        if input('Would you like to continue press Y, else any other key: ') == 'Y':
            game_round += +1
            round_move = 1
            gameboard = list(range(1, 10))
            board(gameboard, game_round, game_score)
            continue
        else:
            print("====The End====")
            break
    round_move += 1
