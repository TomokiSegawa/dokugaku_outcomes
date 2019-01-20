### War Game ###

### imports ###

from random import shuffle

### Define cards###

class Card:

    suits = ['spades','hearts','diamonds','clubs']
    values = [None,None,'2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

    def __init__(self,v,s):
        self.value = v
        self.suit = s

    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < self.suit:
                return True
            else:
                return False
        return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        v = self.values[self.value] + ' of ' + self.suits[self.suit]
        return v


### Define deck###
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(0,4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


### Make Players ###

class Player:
    def __init__(self,name):
        self.win = 0
        self.card = None
        self.name = name


### Define game ###

class Game:
    def __init__(self):
        name1 = input('Player1 name?: ')
        name2 = input('Player2 name?: ')
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        print('{} wins at this round'.format(winner))

    def draw (self,p1n,p1c,p2n,p2c):
        print('{} draws {}, {} draws {}'.format(p1n,p1c,p2n,p2c))

    def play_game(self):
        cards = self.deck.cards
        print('War Starts!!!')
        while len(cards) >= 2:
            m = input('Press Q if you want to quit. Or press C.: ')
            if m == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.win += 1
                self.wins(p1n)
            else:
                self.p2.win += 1
                self.wins(p2n)
        win = self.winner(self.p1,self.p2)
        print('Finish! {} wins!!'.format(win))

    def winner(self,p1,p2):
        if p1.win > p2.win:
            return p1.name
        if p1.win < p2.win:
            return p2.name
        return 'Draw'

game = Game()
game.play_game()
