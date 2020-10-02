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

class Dealer:
    def __init__(self):
        self.cards = []

    def build(self,card):
          self.cards.append (card)

dealercard = Dealer()
print('Start of Dealers Hand')
print("")
for i in range (6):
    card = deck.dealcard()
    dealercard.build(card)
    card.printcards()
    

class Player ():

    def __init__( self):
        self.cards = []
        self.chips = 100
        self.bet = 0
# updateChips is a function which takes the players bet and returns how much money they have after the bet        
    def updateChips (self,bet):        
        return str(self.chips-bet) 
# printBet returns the amount of chips the player has left           
    def printBet (self):
        return str(self.chips)    
# clearHand returns an empty hand so the player has no more cards
    def clearHand (self):
        self.cards = []
# build takes the drawn card and adds it to the players hand
    def build(self,card):
          self.cards.append (card)
 # placeBet determines if the player has enough chips in order to place their desired bet
 # If they do not have enough chips the player is prompted to enter a smaller number
 # eventually need to update this so that the player cannot make a bet that is smaller than the minimum          
    def placeBet (self,bet):
        if (self.chips-bet<0):
            print ("You do not have sufficient funds to place this bet")
        else:
            return (self.bet -bet)      


def check_hand(self):
    if check_four_of_a_kind(self):
        return 9
    if check_straight_flush(self):
        return 8
    if check_three_of_a_kind(self):
        return 7
    if check_flush(self):
        return 6
    if check_straight(self):
        return 5
    if check_two_pair(self):
        return 4
    if check_aces(self):
        return 3
    if check_pair(self):
        return 2
    if check_high_card(self):
        return 1




minimumBet = 10
print("")
p1 = Player()
print('Start of Player 1s Hand')
print("")
print ("Player 1 has "+p1.printBet()+" dollars to bet")   
print ("Please enter your bet, the mimimum is $10: ") 
p1bet = int(input())
if (p1bet <minimumBet):
    print ("The minimum Bet at this table is "+ str(minimumBet)+ ", your bet has been updated to the minimum")
    p1bet = minimumBet
    p1Chips = p1.placeBet(p1bet)
else:
    p1Chips = p1.placeBet(p1bet)
for i in range (5):
    card = deck.dealcard()
    p1.build(card)
    card.printcards()
print ("Player 1 has "+ p1.updateChips(p1bet)+" left after this bet")

print("")
p2 = Player()
print('Start of Player 2s Hand')
print("")
print ("Player 2 has "+p2.printBet()+" dollars to bet")  
print ("Please enter your bet, the mimimum is $10: ") 
p2bet = int(input())


for i in range (5):
    card = deck.dealcard()
    p2.build(card)
    card.printcards()
print ("Player 2 has "+ p2.updateChips(p2bet)+" left after this bet.")




