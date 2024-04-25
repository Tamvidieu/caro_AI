import math

# Hằng số định nghĩa
EMPTY = 0
PLAYER_X = 1
PLAYER_O = 2
WIN = 1000000
LOSE = -1000000
DRAW = 0

# Kích thước bàn cờ
BOARD_SIZE = 10

# Hàm kiểm tra xem có thắng không
def check_win(board, player):
    # Kiểm tra hàng và cột
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE - 4):
            if all(board[i][j + k] == player for k in range(5)):
                return True
            if all(board[j + k][i] == player for k in range(5)):
                return True
    # Kiểm tra đường chéo chính và phụ
    for i in range(BOARD_SIZE - 4):
        for j in range(BOARD_SIZE - 4):
            if all(board[i + k][j + k] == player for k in range(5)):
                return True
            if all(board[i + k][j + 4 - k] == player for k in range(5)):
                return True
    return False

# Hàm đánh giá chủ động
def evaluate(board, player):
    score = 0
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == player:
                score += 1
    return score

# Minimax với Alpha-Beta Pruning
def minimax(board, depth, alpha, beta, maximizing_player):
    if depth == 0 or check_win(board, PLAYER_X) or check_win(board, PLAYER_O):
        return evaluate(board, PLAYER_X) - evaluate(board, PLAYER_O)
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth - 1, alpha, beta, False)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(BOARD_SIZE):
            for j in range(BOARD_SIZE):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth - 1, alpha, beta, True)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Hàm chọn nước đi tốt nhất
def find_best_move(board):
    best_move = None
    best_eval = -math.inf
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                eval = minimax(board, 3, -math.inf, math.inf, False)
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Hàm in bàn cờ
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Hàm main
def main():
    # Khởi tạo bàn cờ
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Vòng lặp chơi
    while True:
        print_board(board)
        row, col = map(int, input("Nhập nước đi của bạn (dòng cột): ").split())
        if board[row][col] != EMPTY:
            print("Ô đã được đánh, hãy chọn ô khác!")
            continue
        board[row][col] = PLAYER_O
        if check_win(board, PLAYER_O):
            print("Bạn thắng!")
            break
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = PLAYER_X
        if check_win(board, PLAYER_X):
            print("Máy thắng!")
            break

if __name__ == "__main__":
    main()
