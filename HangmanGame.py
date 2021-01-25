import random
from HangmanParts import parts

words_spanish = ["lampara", "pantalla", "escritorio"]
words_english = ["picnic", "table", "garden"]

language = input("Which language do you prefer: spanish/english? ")

if language.lower() == "spanish":
    picked = random.choice(words_spanish)
else:
    picked = random.choice(words_english)


print('The word has', len(picked), 'letters')

correct = ['_'] * len(picked)
incorrect = []

def update():
    for i in correct:
        print(i, end = ' ') # end = make that the letters will be printed next to each other
    print() 

update()
parts(len(incorrect))

while True:

    print('================')

    guess = input("Guess a letter: ")

# Way 1: Here we find out if the chosen letter is correct and in what index

    # if guess in picked:
    #     index = 0
    #     for i in picked:
    #         if i == guess:
    #             correct[index] = guess
    #         index += 1
    #     # correct.append(guess)
    #     # print('Correct letters: ', correct)
    #     update() 

# Way 2: To know if the chosen letter is correct and in what index.

    if guess in picked:
        for i in range(len(picked)): 
            index = picked[i]
            # print(picked[i])
            if index == guess:
                correct[i] = picked[i]
    #     correct.append(guess)
    #     print('Correct words: ', correct)
        update()
    else:
        if guess not in incorrect:
            incorrect.append(guess)
            parts(len(incorrect))  # this is to call the fuction

        else:
            print('You already guess that letter')
        print('Incorrect words: ', incorrect)

    if len(incorrect) == 4:
        print('You lose')
        print('I picked', picked)
        break
    if '_' not in correct:
        print('You win')
        break
