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
    print() # Este print() function hace que pasemos a una nueva linea

update()
parts(len(incorrect))

while True:

    print('================')

    guess = input("Guess a letter: ")

# Way 1: Esta parte es para saber si la letra elegida es correcta y en que posicion

    # if guess in picked:
    #     index = 0
    #     for i in picked:
    #         if i == guess:
    #             correct[index] = guess
    #         index += 1
    #     # correct.append(guess)
    #     # print('Correct letters: ', correct)
    #     update() # We have to call the function 'update()` porque esta unida a la funcion definida 'update()´mas arriba. Si no llamamos a la funcion
                 # no apareceria nada del codigo arriba escrito. En otras palabras, no apareceria la opcion de ver que letras hemos acertado y su
                 # orden en la palabra.

# Way 2: Para saber si la letra elegida es correcta y en que posicion. (Para mi, mas facil de entender)

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