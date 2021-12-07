from utils import import_boards, import_drawn_number


input_path = "./data/input"

drawn = import_drawn_number(input_path)
boards = import_boards(input_path)


winning_boards = []

for number in drawn:
    for board in boards:
        board.mark(number)
    
    winner = [board for board in boards if board.is_winning()]
    boards = [board for board in boards if not board.is_winning()]

    if not boards:
        break

winner = winner[0]
score = winner.unmarked_sum() * number

print(f"The score of the latest winning board is {score}")
