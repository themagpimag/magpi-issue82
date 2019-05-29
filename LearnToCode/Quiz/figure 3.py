vowels = ["A", "E", "I", "O", "U", " ", "'"]
puzzle = ""

for letter in chosen_phrase:
    if not letter in vowels:
        puzzle += letter
