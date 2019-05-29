print(puzzle_with_spaces)
guess = input("What is your guess? ")
guess = guess.upper()

if guess == chosen_phrase:
    print("That's correct!")
else:
    print("No. The answer is ", chosen_phrase)
