puzzle_with_spaces = ""

while len(puzzle) > 0:
    group_length = random.randint(1,5)
    puzzle_with_spaces += puzzle[:group_length] + " "
    puzzle = puzzle[group_length:]
