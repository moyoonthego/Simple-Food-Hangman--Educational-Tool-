"""
# Copyright Muhammad Ali, Mustafa Ali, etc. 2018
# Distributed under the terms of the GNU General Public License.
#
# The following game is a simple hangman module, based on the open forum game.
# This is an educational tool for elementary students, feel free to find the
# flaws and debug/modify it as needed.
#
# see <http://www.gnu.org/licenses/> for the General Public License.
"""
# This program is a joint collaboration with elementary students...
# The random value python library
import random

# A megalist of all the foods we want to play hangman with
words = ['pizza', 'cheeseburger', 'spaghetti', 'corn', 'lambchops', 'drumsticks'
         'sandwich', 'fish', 'mushrooms', 'chicken wings', 'ice cream',
         'noodles', 'pasta', 'apples', 'strawberries', 'lollipop', 'lasagna']

def hangman(word):
    ''' (str) -> None
    This function replicates a game of hangman, where we keep running until the
    word is found.
    '''
    guess_word = ''
    guess_letter = ''
    # String outputting the correct guesses
    correct_guesses = "\n\nCorrect Guessed letters: "
    # string outputting the wrong guesses
    wrong_guesses = "\nWrong Guessed letters:"
    # loop as long as word is not guessed correctly
    while(guess_word != word):
        # ask user if they want to guess a letter, store it if they do
        print("Would you like to guess a letter?")
        guess_letter = input("Letter:")
        # splits guesses into two sections, wrong and correct
        # by seeing if the guess letter is in the word or not
        if (guess_letter in word):
            correct_guesses += guess_letter + " "
        else:
            wrong_guesses += guess_letter + " "
        # ask user if they wwant to guess a word and store it
        print("Would you like to guess the word?")
        guess_word = input("Word:")
        print(correct_guesses + wrong_guesses +'\n')
    # congratulates user for guessing correctly
    print("Congratulations! You got the word!")

if __name__ == '__main__':
    # choose a random word
    word = random.choice(words)
    print("~~~FOOD HANGMAN~~~")
    # run hangman
    hangman(word)