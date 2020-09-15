#This program is a python implementation of the casino "carnival syle" poker card games  
#This game is being implemented by Tennisha Martin of BlackGirlsHack

print ('Hello World')

import random


class Card:
# This is the cards class, the purose of this class is to initialize a card and to print its value.
    def __repr__ (self):
        return self.__str__
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def printcards(self):
        print( "{} of {}".format(self.rank,self.suit)    )

# Test the printing of a Card
#card = Card("Clubs","Ace")
#card.printcards()
class Deck:
# This is the deck class, the purpose of this class is to initialize the deck and to preint its value.
    def __init__(self):
        self.cards = []
        self.build()
    def __repr__ (self):
        return self.__str__
    def build (self):
        for s in  ['Clubs','Diamonds','Hearts','Spades']:
            for r in ['Ace','2','3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']:
               # print (Card(s,r))
                self.cards.append (Card(s,r))
            
  # The purpose of this def is to show all the cards in the deck. This will be later modified to shuffle the deck  
    def showcards (self):
        for c in self.cards:
            c.printcards()
 # The purpose of this def is to shuffle the cards so they will be in a randomized order.
    def shuffle (self):
        for i in range (len (self.cards) -1, 0, -1):
            r =rando = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
# Ther purpose of this is to deal a certain number of cards, 5 for the players and 6 for the dealers 

    def dealcard (self):
        return self.cards.pop()
#Deal Dealers Cards
    def dealn (self, n):
        for i in range (n):
            deal(self,6)
# The purpose of this is to test the creation and the display of the deck of the cards.             
deck = Deck()
deck.shuffle()
deck.shuffle()
deck.showcards()

print('Start of Dealers Hand')
print("")
for i in range (6):
    card = deck.dealcard()
    card.printcards()

print('Start of Player 1s Hand')
print("")
for i in range (5):
    card = deck.dealcard()
    card.printcards()



    

class Player (object):

    def __init__( self):
        self._cards = []
        self._chips = 100
        self._bet = 0

    def clearHand (self):
        self._cards = []

    def dealCard (self, card):
        self._cards.append(card)


