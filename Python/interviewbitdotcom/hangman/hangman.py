import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly chooses   something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letter used
        # ' '.join(['a', 'b', 'cd']) --> 'a  b cd'
        print('Kamu punya', lives, 'lives tersisa dan kamu telah menggunakan huruf ini:  ',  ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for  letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Tebak huruf: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1 # takes away a life if wrong
                print('\nHuruf kamu,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\Kamu sudah menggunakan huruf itu. Tebak huruf lain.')

        else:
            print('\nItu bukan huruf yang valid')


    # gets here when len(word_letters) == 0 OR when lives === 0
    if lives == 0:
        print('Kamu kalah, maaf. Kata itu adalah', word)
    else:
        print('YAY!, Kamu menebak kata itu', word)

    if __name__ == '__main__':
        hangman()
