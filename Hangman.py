import random

words = ['python', 'java', 'kotlin', 'javascript']
guess = random.choice(words)
hint = ('-' * len(guess))

print('H A N G M A N\n')

# Main game
def play():
    life = 8
    guesses = []
    wrong_guess = []
    while life > 0:
        dis_word: str = ''
        letter = input('Input a letter: ')

        # checking user inputs
        if letter in guesses or letter in wrong_guess:
            print("You've already guessed this letter")
        else:
            if letter in guess:
                guesses.append(letter)
            else:
                if len(letter) > 1:
                    print("You should input a single letter")
                elif not letter.isalpha() or not letter.islower():
                    print("Please enter a lowercase English letter")
                else:
                    print("That letter doesn't appear in the word")
                    wrong_guess.append(letter)
                    life -= 1
                    
       
        # Displaying hint without the enumerate method
        for char in guess:
            if char in guesses:
                dis_word += char
            else:
                dis_word += "-"

        if life > 0 and dis_word != guess:
            print('\n', dis_word)
        if dis_word == guess:
            print(f"You guessed the word {guess}!")
            print("You survived!")
            break
    else:
        print("You lost!")
        exit()

# Do you really want to play this boring game :)
def main():
    while True:
        decision = input("Type \"play\" to play the game, \"exit\" to quit: ")
        if decision == "play":
            print(hint)
            play()
        elif decision == "exit":
            break


main()
