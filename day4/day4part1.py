def read_input(filename):
    with open(filename, 'r') as file:
        content = file.read().strip().split('\n\n')
    drawn_numbers = list(map(int, content[0].split(',')))
    boards = []
    for board in content[1:]:
        boards.append([[int(num) for num in line.split()] for line in board.split('\n')])
    return drawn_numbers, boards

def mark_number(board, number):
    for row in board:
        for i in range(len(row)):
            if row[i] == number:
                row[i] = -1

def is_winner(board):
    for row in board:
        if all(num == -1 for num in row):
            return True
    for col in range(len(board[0])):
        if all(row[col] == -1 for row in board):
            return True
    return False

def calculate_score(board, last_number):
    unmarked_sum = sum(num for row in board for num in row if num != -1)
    return unmarked_sum * last_number

def find_first_winning_board(drawn_numbers, boards):
    for number in drawn_numbers:
        for board in boards:
            mark_number(board, number)
            if is_winner(board):
                return calculate_score(board, number)
    return None

def main():
    drawn_numbers, boards = read_input('input.txt')
    score = find_first_winning_board(drawn_numbers, boards)
    print(f"The final score of the first winning board is: {score}")

if __name__ == "__main__":
    main()
