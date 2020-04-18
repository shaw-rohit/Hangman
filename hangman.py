import random
from words import cities

def hangman_pick_word():
    """
    Randomly picks a word from the words.py file and converts to upper case.
    """
    word = random.choice(cities).upper()
    return word


def hangman_print_dashes(word):
    """
    Generates a standard hint and the number of dashes based on the word
    previously selected 
    """
    hangman_clear_screen()
    no_of_dashes = len(word)
    print_dashes = "_" * no_of_dashes 
    print("Word: {0} ".format(" ".join(print_dashes)))
    return print_dashes


def hangman_get_letter():
    """
    Requests user to input a letter and converts it to upper case
    """
    user_guess = input("Please guess a letter: ").upper()
    hangman_clear_screen()
    return user_guess

def hangman_clear_screen():
    """
    Clears screen based on the range specifed.
    """
    for i in range(1):
        print("\n")

def hangman_win_lose(word, guessed):
    """
    Checks if the player won or lost and prints the information
    """
    if guessed:
        print("Congratulations! You won the game!")
    else:
        print("Sorry you ran out of lives! The correct answer is {0} ".format(word))
    return 

def hangman_algorithm(word):
    """
    Sets user attemps and initial state of the game. Obtains user guesses and
    checks for validity. If user guess is correct, displays the appropriate
    letters corresponding to the guess. If the user guess is invalid, decreases
    attempts and informs user. If user guessed a previously guessed letter, no
    penealty for the user. The user if informed if they won or lost the game at
    the end.
    """
    user_guess_list = []
    attempts = 9
    guessed = False
    valid_indices = []

    print_dashes = hangman_print_dashes(word)
    print("(It\'s a city with {0} letters!) \n".format(len(word)))

    print_dashes_list = list(print_dashes)
    word_list = list(word)

    while not guessed and attempts > 0:
        print("Remaining Lives: {0} ".format(attempts))
        print("Letters Guessed: {0} ".format(user_guess_list))
        user_guess = hangman_get_letter()

        if (len(user_guess) == 1 and user_guess.isalpha()):
            if user_guess in user_guess_list:
                print("You've already guessed this letter! Try again!")
                print("Word: {0}".format(" ".join(print_dashes)))
            elif user_guess not in word:
                print("Sorry! {0} is not in the word. Try again!".format(user_guess))
                user_guess_list.append(user_guess)
                attempts -= 1
                print("Word: {0}".format(" ".join(print_dashes)))
                print("(It\'s a city with {0} letters!) \n".format(len(word)))
            else:
                print("This letter is in the word!")
                user_guess_list.append(user_guess)

                valid_indices = [index for index, letter in enumerate(word) if 
                        letter == user_guess]

                for index in valid_indices:
                    print_dashes_list[index] = user_guess

                print_dashes = "".join(print_dashes_list)
                print("Word: {0}".format(" ".join(print_dashes)))
                print("(It\'s a city with {0} letters!) \n".format(len(word)))

                if "_" not in print_dashes:
                    guessed = True

        else:
            print("Please enter a valid, single letter.")
            print("Word: {0}".format(" ".join(print_dashes)))
            print("(It\'s a city with {0} letters!) \n".format(len(word)))

    hangman_win_lose(word, guessed)


def main():
    word = hangman_pick_word()
    hangman_algorithm(word)

    replay_question = input("Press Y to continue or any press any other key to exit.")

    while replay_question.upper() == "Y":
        word = hangman_pick_word()
        hangman_algorithm(word)

if __name__ == "__main__":
    main()
