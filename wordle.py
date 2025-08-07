import random
words = ["apple", "bread", "chair", "dance", "eagle",
        "flame", "grape", "heart", "ivory", "jelly",
        "knife", "lemon", "magic", "night", "ocean",
        "plant", "quiet", "river", "stone", "trust""about", "actor", "adobe", "agile", "agent", "angel", "anger", "apple", "arena", "armor", 
        "award", "aware", "badge", "basic", "beach", "begin", "belly", "blade", "blend", "bless", 
        "block", "board", "boast", "brave", "brick", "bride", "bring", "broad", "brush", "build", 
        "burst", "cable", "campy", "chain", "chalk", "charm", "chest", "chief", "choir", "claim", 
        "clear", "climb", "cloud", "coach", "color", "coral", "craft", "crash", "cream", "crime", 
        "crush", "curve", "dance", "death", "delay", "devil", "diary", "doubt", "dream", "drive", 
        "drunk", "eager", "earth", "elbow", "elder", "empty", "enemy", "enjoy", "entry", "equal", 
        "faith", "fancy", "fault", "feast", "fiber", "field", "flame", "floor", "flour", "force", 
        "frame", "fraud", "fresh", "front", "fruit", "giant", "glory", "grace", "graph" 
        "green", "grief", "grind", "group","great"
]
answer = random.choice(words)
global green 
green = 0
def word_exists():
    with open("words.txt", "r") as file:
        content = file.read()
        if guess in content:
            display_results()
        else:
            print("Enter a valid word")
def main():
    global guess
    global guesses
    guesses = 0
    while guesses < 5:
        guess = input("Guess the five-letter word: ")
        if  len(guess) == 5:
            word_exists()
            guesse += 1
        elif not len(guess) == 5:
            print("Enter valid length")
def display_results():
    global green 
    green = 0
    guess_characters = list(guess)
    answer_characters = list(answer)
    if guess_characters[0] == answer_characters[0]:
        print("1 is green")
        green += 1
    elif guess_characters[0] in answer_characters:
        print("1 is yellow")
    if guess_characters[1] == answer_characters[1]:
        print("2 is green")
        green += 1
    elif guess_characters[1] in answer_characters:
        print("2 is yellow")
    if guess_characters[2] == answer_characters[2]:
        print("3 is green")
        green += 1
    elif guess_characters[2] in answer_characters:
        print("3 is yellow")
    if guess_characters[3] == answer_characters[3]:
        print("4 is green")
        green += 1
    elif guess_characters[3] in answer_characters:
        print("4 is yellow")
    if guess_characters[4] == answer_characters[4]:
        print("5 is green")
        green += 1
    elif guess_characters[4] in answer_characters:
        print("5 is yellow")
    win_lose()
def win_lose():
    if green == 5:
        display_answer()
        print("You win")
        print("Thank you for using wordle") 
        quit()
    if guesses == 5:
        display_answer()
        print("You lose")
        print("Thank you for using wordle")
        quit()
def display_answer():
    print(f"The answer was {answer}")
if __name__ == "__main__":
    main()
