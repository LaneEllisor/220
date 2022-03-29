"""
Name: Lane Ellisor
lab9.py
"""


def build_board():
    list = []
    for i in range(9):
        list.append(i+1)
    return list

def print_board(board):
    """ prints the values of board """
    RED = "\033[1;31m"
    BLUE = "\033[1;36m"
    LIGHT_GRAY = "\033[0;37m"
    reset = "\033[0m"
    new_board = []
    for v in board:
        new_board.append(v)
    for i in range(len(board)):
        if str(board[i]).find('x') >= 0:
            new_board[i] = RED + board[i] + LIGHT_GRAY
        elif str(board[i]).find('o') >= 0:
            new_board[i] = BLUE + board[i] + LIGHT_GRAY
    row_format = ' {0} | {1} | {2} '
    row_1 = row_format.format(new_board[0], new_board[1], new_board[2])
    row_2 = row_format.format(new_board[3], new_board[4], new_board[5])
    row_3 = row_format.format(new_board[6], new_board[7], new_board[8])
    row_separator = '-' * 11
    print(LIGHT_GRAY)
    print(row_1)
    print(row_separator)
    print(row_2)
    print(row_separator)
    print(row_3)
    print(reset)


def fill_spot(board, position, character):
    character = board[position]



def is_legal(board, position):
    if type(board[position]) == str:
        return True
    else:
        return False


def game_is_won(board):
    solution_sets = ["1,2,3", "1,4,7", "1,5,9", "2,5,6", "3,6,9", "4,5,6", "7,5,3"]
    for i in range(len(solution_sets)):
        line = solution_sets[i].split(",")
        for j in range(3):
            if board[line[j]=="x"]:
                return True
            if board[line[j] == "o"]:
                return True
        else:
            return False



def game_over(board):
    count = 0
    for i in range(9):
        if board[i] == int:
            count += 1
    if count > 0:
        return winning_game(board)
    else:
        return False


def get_winner(board):
    count_X, count_O = 0,0
    for i in range(9):
        if board[i] == "x":
            count_X += 1
        elif board[i] == "o":
            count_O += 1
    sum_counts = count_X + count_O
    if count_X > 0 and sum < 9:
        return "x"
    elif count_X == count_O:
        return "o"
    else:
        None

def play(board):


def main():
    pass


if __name__ == '__main__':
    main()
