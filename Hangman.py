import random

# A play again command
def playAgain():
    flag = True
    while flag:
        dec = input('Do you want to play again(y or n): ')
        if dec == 'y':
            hangman()
            flag == False
        elif dec == 'n':
            exit()
    
# Main Game Code    
def hangman():
    # For Random Scolding
    quote = ("So You Have Great Memmory Power...\nYou Have Entered The Letter Already, Idiot...", "Do You Heard of Alzheimer's Disease\nYou Have Entered The Letter Already, Mr. Big Brain...")
    # More words added
    words = ('python', 'java', 'javascript', 'kotlin', 'bash', 'git', 'flutter', 'php', 'node', 'react', 'html', 'css', 'sass', 'express', 'sql', 'objectivec', 'scala', 'ruby', 'vue')
    choice = random.choice(words)
    # The Valid Letter variable. Greater then the previous complex loops
    validLetters = 'abcdefghijklmnopqrstuvwxyz'
    turns = 10
    guesses = []
    wrong_gusses = []
    show = '-'*len(choice)
    print("H A N G M A N")
    print(show)

    while turns > 0:
        # Name will be added to a file called name. Replaced in every restart. Go To line 67 for more details.
        f1 = open("name.txt", "r")
        n = f1.read()
        hint = ''
        guess = input('Input a letter: ')

        if guess not in guesses and guess not in wrong_gusses:
            if guess in choice:
                guesses.append(guess)
            elif guess not in validLetters:
                print('Please Enter A Valid English Small Letter')
            else:
                # Here {n} is the name from the file.
                print(f"OOPS! {n} You Are Gonna Kill Me!")
                turns -= 1
                wrong_gusses.append(guess)
            # For showing the hint
            for letter in choice:
                if letter in guesses:
                    hint += letter
                else:
                    hint += '-'
        else:
            # Random Scolding :)
            random_quote = random.choice(quote)
            print(random_quote)

        if hint == choice:
            print(choice,'\n')
            print('Coongratulations For Winning...\n And Thanks For Saving Me :)')
            # Do you want to save me again?
            playAgain()

        print(hint)

    else:
        print("You Failed...\n And I Dead :(")
        # Do you want to kill me again :)
        playAgain()

def main():
    name = input("Enter Your Name: ")
    # The name will be added to the file called name.txt.
    # and replaced in every restart
    f = open("name.txt","w+")
    f.write(name)
    f.close()
    print("Welcome", name)
    print("##########################")
    print("Try to guess the word in less than 10 attempts.\n")
    
    hangman()


if __name__=='__main__':
    main()

