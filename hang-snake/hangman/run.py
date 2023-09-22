import os
import random
import graphics as graph
import words


def create_secret():
    return words.word_list[random.randint(0, len(words.word_list))]


tries = 6
word = create_secret()
word_arr = ['_'] * len(word)
guessed = []            # guessed letters
letter = 0
incorrect = []
print(*word_arr)

while tries > 0:
    # make a move!
    if word_arr.count('_') == 0:
        print('You won!! (^_^)')
        break
    flag = 0
    while flag == 0:
        letter = input('Enter your guess:')
        if letter.isdecimal():
            print('Incorrect input')
        elif len(letter) != 1:
            print('Incorrect input')
        else:
            flag = 1

    if letter in word and letter not in guessed:   # if letter is correct and have not been guessed yet
        print('you are right!')
        guessed.append(letter)
        for i in range(0, len(word)):
            if letter == word[i]:
                word_arr[i] = letter
    elif letter in word_arr:                       # if letter is already guessed
        print('you already guessed this letter :/')
    else:
        print('incorrect letter :(')               # if letter is incorrect
        incorrect.append(letter)
        tries -= 1

    os.system('cls')
    print(graph.img[-tries+6])
    print(*word_arr)
    print('incorrect letters:', *incorrect)
else:
    print('You lost :( Try again')

print('The word was: ' + word)

