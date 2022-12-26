import random
from words import word_list
from hangman_art import logo
from hangman_art import stages
want_to_play = "y"

#HangMan GameLoop
while want_to_play == "y":
    lifes_left = 7
    correct_letters = 0
    print(logo)

    #Pick a random word from list
    chosen_word = random.choice(word_list)
    number_of_chars = len(chosen_word)
    #print(chosen_word)
    #print(number_of_chars)

    #Generate Blankspace Word
    blankspace_word = []
    iteration = 0
    while iteration < number_of_chars:
        blankspace_word.append("_")
        iteration += 1
    print(*blankspace_word, sep='')

    #Hangman Game
    while lifes_left > 0:
        char_position = -1
        correct_guess = False
        guess = input("Guess a letter: ").lower()

        for char in chosen_word:
            char_position += 1
            if guess == char:
                correct_guess = True
                correct_letters += 1
                blankspace_word[char_position] = guess
                print("\n")
                print(*blankspace_word, sep='')
        if correct_guess == False:
            lifes_left -= 1
            print(stages[lifes_left])
            print(f"Wrong guess. Lifes left: {lifes_left}\n")
            print(*blankspace_word, sep='')
        if correct_letters == number_of_chars:
            print(f"You have won!")
            lifes_left = 0
    print(f"The correct word was {chosen_word}.")
    want_to_play = input("Wanna play again?: y/n\n").lower()

print("Exiting Game..")
exit()