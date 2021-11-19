#1

def hangman(word):
    wrong=0
    stage=['',
           '______________',
           '|             ',
           '|      |      ',
           '|     〇      ',
           '|     /|\     ',
           '|     / \     '
           ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print('ハングマンへようこそ')
    while wrong<len(stage)-1:
        print('\n')
        msg=('1文字予測してね')
        char = input(msg)
        if char in rletters:
            cind=rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
            print(' '.join(board))
            if '_' not in board:
                print('you win')
                win = True
                break
            
        else:
            wrong+=1
            print(' '.join(board))
            '''if '_' not in board:
                print('あなたの勝ち')
                win=True
                break'''
        print('\n'.join(stage[0:wrong+1]))
    '''if not win:
        print('\n'.join(stage[0:wrong+1]))'''
    print('あなたの負け。せいかいは{}'.format(word))

hangman('woolf')