import random

def print_board(board):
    for i, row in enumerate(board):
        row_str = " "
        for j, value in enumerate(row):
            row_str += value
            if j != len(row) - 1:
                row_str += " | "
        print(row_str)
        if i != len(board) - 1:
            print("------------")

def get_move(turn, board):
    while True:
        row = int(input("Enter row (1-3): "))
        col = int(input("Enter column (1-3): "))

        if row < 1 or row > 3:
            print("Invalid row. Please try again.")
        elif col < 1 or col > 3:
            print("Invalid column. Please try again.")
        elif board[row - 1][col - 1] != " ":
            print("That spot is already taken. Please try again.")
        else:
            board[row - 1][col - 1] = turn
            break

def computer_move(board):
    print("Computer's turn:")
    empty_positions = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    if empty_positions:
        row, col = random.choice(empty_positions)
        board[row][col] = "O"

def check_win(board, turn):
    lines = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for line in lines:
        if all(board[row][col] == turn for row, col in line):
            return True
    return False

# Initialize the board
board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

turn = "X"
turn_number = 0

print_board(board)
while turn_number < 9:
    print()
    print(f"It is {turn}'s turn. Please select your move.")
    if turn == "O":
        computer_move(board)
    else:
        get_move(turn, board)

    print_board(board)

    if check_win(board, turn):
        print(f"The winner is {turn}!")
        break

    turn = "O" if turn == "X" else "X"
    turn_number += 1

if turn_number == 9 and not check_win(board, turn):
    print("It's a tie!")
