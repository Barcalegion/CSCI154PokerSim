import random as r
import queue as q

r.seed()

NUM_PLAYERS = 2

PLAYERPOCKETS = {}

COMMUNITYCARDS = []

COMBINEDCARDS = {}

WINNINGPLAYERS = []

def shuffleDeck(deck):  
    
    cards = 51

    shuffledDeck = q.Queue()

    while deck:
        randomCard = r.randint(0,cards)
        shuffledDeck.put(deck[randomCard])
        cards = cards - 1
        del deck[randomCard]

    return shuffledDeck

def deal_cards(deck):    
    for i in range(NUM_PLAYERS):
        PLAYERPOCKETS.update({i : [deck.get(),deck.get()]})

    for i in range(5):
        COMMUNITYCARDS.append(deck.get())

def combine_cards(playerCards, communityCards):
    for i in range(NUM_PLAYERS):
        for y in range(7):
            if y < 2:
                COMBINEDCARDS.update({i: [playerCards.pop(i)]})
            else:
                COMBINEDCARDS.update({i: [communityCards.pop(i - 2)]})
        
        
            
suits = ["clubs","hearts","Diamonds","Spades"]

values = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

Deck = []

for i in range(len(values)):
    for y in range(len(suits)):
        Deck.append((values[i],suits[y]))



readyDeck = shuffleDeck(Deck)

deal_cards(readyDeck)

combine_cards(PLAYERPOCKETS, COMMUNITYCARDS)

print("Player pocket cards: ",PLAYERPOCKETS)

print("Community cards: ", COMMUNITYCARDS)

print("Combined cards: ", COMBINEDCARDS)
