import random as r
import queue as q

r.seed()

def shuffleDeck(deck):
    count = 0
    
    cards = 51

    shuffledDeck = q.Queue()

    while deck:
        randomCard = r.randint(0,cards)
        shuffledDeck.put(deck[randomCard])
        cards = cards - 1
        del deck[randomCard]
        
    return shuffledDeck

suits = ["clubs","hearts","Diamonds","Spades"]

values = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

Deck = []

for i in range(len(values)):
    for y in range(len(suits)):
        Deck.append((values[i],suits[y]))



readyDeck = shuffleDeck(Deck)

while not readyDeck.empty():
    print(readyDeck.get())
