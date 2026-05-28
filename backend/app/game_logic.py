import random

board = [""] * 9

current_player = "X"

winner = ""

draw = False

x_score = 0
o_score = 0
draw_score = 0

difficulty = "hard"


winning_combos = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]


def update_score():

    global x_score
    global o_score

    if winner == "X":
        x_score += 1

    elif winner == "O":
        o_score += 1


def check_winner():

    global winner

    for combo in winning_combos:

        a, b, c = combo

        if (
            board[a] and
            board[a] == board[b] and
            board[a] == board[c]
        ):

            winner = board[a]

            update_score()


def check_draw():

    global draw
    global draw_score

    if "" not in board and not winner:

        draw = True

        draw_score += 1


def get_available_moves():

    moves = []

    for index, cell in enumerate(board):

        if cell == "":
            moves.append(index)

    return moves


def evaluate_board(temp_board):

    for combo in winning_combos:

        a, b, c = combo

        if (
            temp_board[a] and
            temp_board[a] == temp_board[b] and
            temp_board[a] == temp_board[c]
        ):
            return temp_board[a]

    return None


def minimax(temp_board, is_maximizing):

    result = evaluate_board(temp_board)

    if result == "O":
        return 1

    elif result == "X":
        return -1

    elif "" not in temp_board:
        return 0

    if is_maximizing:

        best_score = -100

        for i in range(9):

            if temp_board[i] == "":

                temp_board[i] = "O"

                score = minimax(temp_board, False)

                temp_board[i] = ""

                best_score = max(score, best_score)

        return best_score

    else:

        best_score = 100

        for i in range(9):

            if temp_board[i] == "":

                temp_board[i] = "X"

                score = minimax(temp_board, True)

                temp_board[i] = ""

                best_score = min(score, best_score)

        return best_score

def easy_ai():
    available_moves = get_available_moves()
    if not available_moves:
        return

    move = random.choice(available_moves)

    board[move] = "O"

    check_winner()

    check_draw()

def medium_ai():
    chance = random.randint(1, 10)

    # 50% smart
    if chance <= 5:
        hard_ai()

    else:
        easy_ai()

def hard_ai():

    best_score = -100

    move = None

    for i in range(9):

        if board[i] == "":

            board[i] = "O"

            score = minimax(board, False)

            board[i] = ""

            if score > best_score:

                best_score = score

                move = i

    if move is not None:

        board[move] = "O"

        check_winner()

        check_draw()

def ai_move():

    if difficulty == "easy":
        easy_ai()

    elif difficulty == "medium":
        medium_ai()

    else:
        hard_ai()   

def make_move(position):

    global current_player

    if winner or draw:
        return {
            "error": "Game already finished"
        }

    if board[position] != "":
        return {
            "error": "Cell already occupied"
        }

    board[position] = "X"

    check_winner()

    check_draw()

    if not winner and not draw:
        ai_move()

    return {
        "board": board,
        "current_player": current_player,
        "winner": winner,
        "draw": draw,

        "x_score": x_score,
        "o_score": o_score,
        "draw_score": draw_score
    }


def reset_game():

    global board
    global current_player
    global winner
    global draw

    board = [""] * 9

    current_player = "X"

    winner = ""

    draw = False

    return {
        "message": "Game reset"
    }