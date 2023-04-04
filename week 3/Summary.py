#ord(char) convert char value to number
def myhash(value : str):
    hash = 1
    i = 0
    
    while i < len(value):
        a = hash * ord(value[i])
        b = a * (i + 1)
        c = b % 397643
        hash = c
        i += 1
    hash %= 100297
    return hash

def tic_tac_toe():
    board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
    turn = 'O'

    def check_row(board, row_index):
        if board[row_index][0] == board[row_index][1] and board[row_index][1] == board[row_index][2]:
            return board[row_index][0]
        return '-'

    def check_col(board, col_index):
        if board[0][col_index] == board[1][col_index] and board[1][col_index] == board[2][col_index]:
            return board[0][col_index]
        return '-'

    def check_board(board):
        winner = '-'
        for i in range(0, 3):
            row = check_row(board, i)
            col = check_col(board, i)
            if row != '-':
                winner = row
            if col != '-':
                winner = col
            
        diag1 = board[0][0] == board[1][1] and board[1][1] == board[2][2]
        diag2 = board[0][2] == board[1][1] and board[1][1] == board[2][0]
        if (diag1 or diag2) and board[1][1] != '-':
            winner = board[1][1]

        return winner

    def is_valid_input(board, row : str, col : str):
        if (not row.isnumeric()) or (not col.isnumeric()):
            return False
        row = int(row)
        col = int(col)
        if not (row >= 0 and row < 3 and col >= 0 and col < 3):
            return False
        return board[row][col] == '-'

    def handle_input(board, turn):
        valid_inp = False
        inp = []
        while not valid_inp:
            inp = input(f"Player {turn}, choose cell : ").strip().split(' ')
            valid_inp = is_valid_input(board, inp[0], inp[1])
        
        row = int(inp[0])
        col = int(inp[1])
        board[row][col] = turn

        
    def print_board():
        for i in range(0, 3):
            print(board[i])

    prev_turn = '-'
    while check_board(board) == '-':
        print_board()
        handle_input(board, turn)
        prev_turn = turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    print_board()
    print(f"THE WINNER IS {prev_turn}")
        
def bank():
    users = [[], []]
    def read_users():
        lines = []
        with open("users.txt", "r") as file:
            lines = file.readlines()
        
        for line in lines:
            data = line.split(':')
            users[0].append(data[0])
            users[1].append(data[1].strip("\n"))
        
    def register_to_bank(username : str, password : str):
        if not is_registered(username):
            hashed = myhash(password)
            users[0].append(username)
            users[1].append(hashed)
            with open("users.txt", "a") as file:
                file.write(f"{username}:{hashed}\n")
            return True
        else:
            print("Username taken.")
            return False

    def is_registered(username : str):
        return username in users[0]

    def validate_user_pass(username : str, password : str):
        i = users[0].index(username)
        hashed = myhash(password)
        return users[1][i] == hashed

    def login_to_bank(username : str, password : str):
        if not is_registered(username):
            print("user not registered")
        elif validate_user_pass(username, password):
            print("incorrect password")
        else:
            print(f"welcode {username}")
            

    read_users()
    print("sign in to bank")
    flag = False

    while not flag:
        username = input("enter username : ")
        password = input("enter password : ")
        flag = register_to_bank(username, password)

    print("\nlogin into to bank")
    username = input("enter username : ")
    password = input("enter password : ")
    login_to_bank(username, password)
 
print("pick a program :")
print("1.Tic tac toe")
print("2.Bank system")

inp = int(input("option : "))
if inp == 1:
    tic_tac_toe()
elif inp == 2: 
    bank()
else:
    print("invalid")