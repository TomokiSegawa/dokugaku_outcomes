def hangman(word):
    ### Iinitialize
    wrong = 0
    stages = ["",
              "______________",
              "|             ",
              "|       |     ",
              "|       O     ",
              "|      /|\    ",
              "|      / \    ",
              "|             "
              ]
    rletters = list(word)
    board = ["_"]*len(rletters)
    win = False
    print('Welcome to Hangman game!! ')

    ###make loop
    while wrong < len(stages)-1:
        print("\n")
        char = input('guess a letter: ')
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        print("\n".join(stages[0:wrong+1]))
        if "_" not in board:
            print('You Win!!')
            print(" ".join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages))
        print('You Lose!! Answer is {}'.format(word))
        

### Randmize hangman

import random
key = random.randint(0,3)
option = ['cat','dog','wolf','panda']

### Start the game!!

hangman(option[key])



        
