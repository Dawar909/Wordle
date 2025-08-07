import random
is_running = True
words = ["apple", "bread", "chair", "dance", "eagle",
    "flame", "grape", "heart", "ivory", "jelly",
    "knife", "lemon", "magic", "night", "ocean",
    "plant", "quiet", "river", "stone", "trust"]
answer = random.choice(words)
def word_exists():
    global guess
    guesses = 0 
    with open("words.txt", "r") as file:
        content = file.read()
        if guess in content:
            guesses += 1
            display_results(guesses)
        else:
            print("Enter a valid word")
def main():
    while is_running:
        global guess
        guess = input("Guess the five-letter word: ")
        while len(guess) == 5:
            guess = input("Guess the five-letter word: ")
            word_exists()
        print("Enter valid length")
def display_results(num_guesses):
    global guess
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
    if green == 5:
        display_answer()
        print("You win")
        is_running = False
    if num_guesses == 5:
        display_answer()
        print("You lose") 
        is_running = False     
def display_answer():
    print(answer)
if __name__ == "__main__":
    main()