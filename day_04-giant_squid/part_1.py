from utils import import_boards, import_drawn_number


input_path = "./data/input"

drawn = import_drawn_number(input_path)
boards = import_boards(input_path)

for number in drawn:
    for board in boards:
        board.mark(number)
    
    winner = [board for board in boards if board.is_winning()]

    if winner:
        winner = winner[0]
        break

score = winner.unmarked_sum() * number

print(f"The score of the first winning board is {score}")
