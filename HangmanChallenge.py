import random 
print("Welcome to Hangman!")
words = ["hacker", "bounty", "random"]
secret_random_word = random.choice(words)
print("You have 10 tries to guess the word.")
display_word = [] 
for letter in secret_random_word:
    display_word += "_"
print(display_word)    
tries = 10
game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()
    for position in range(len(secret_random_word)):
        letter = secret_random_word[position]
        if letter == guess:
            display_word[position] = letter
            tries -= 1
            print(f"Good guess! The letter {letter} is in the word.")
            print(f"You still have {str(tries)} tries left. Have a try")
            print(display_word)
    if guess not in secret_random_word:
        tries -= 1
        print(f"Tough luck! You have {str(tries)} tries left.")
    if tries == 0:
        print("You lose the Hangman Challenge!")
        game_over = True
    if "_" not in display_word:
            print(f"Your word is {str(display_word)}") 
            game_over = True   
print("WELL DONE! You win the Hangman Challenge!")      
