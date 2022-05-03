import random as r
import queue as q
import hands as h
from collections import Counter
import pandas as pd

r.seed()

NUM_PLAYERS = 9

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
        if i == 0:
            COMBINEDCARDS.update({i: playerCards[i]})
            for y in range(5):
                COMBINEDCARDS[i].append(communityCards[y])
        else:
            COMBINEDCARDS.update({i: playerCards[i]})
            for y in range(5):
                COMBINEDCARDS[i].append(communityCards[y])

def evaluate_hands(cmbcards):
    
    results = {}

    for i in range(NUM_PLAYERS):
        results.update({i : [("royal_flush",h.royal_flush(cmbcards,i)),("straight_flush",h.straight_flush(cmbcards,i)),
                             ("four_of_a_kind",h.four_of_a_kind(cmbcards,i)),("full_house",h.full_house(cmbcards,i)),
                             ("flush",h.flush(cmbcards,i)),("straight",h.straight(cmbcards,i)),
                             ("three_of_a_kind",h.three_of_a_kind(cmbcards,i)),("two_pair",h.two_pair(cmbcards,i)),
                             ("one_pair",h.one_pair(cmbcards,i)),("high_card",h.high_card(cmbcards,i))]})

    return results

def evaluate_results(results):
    winner = 0
    handwon = {}
    
    winningCards = {}
    playerhighesthand = {}
    minimum = 11
    index = 0
    
    for i in range(NUM_PLAYERS):
        for y in range(10):
            if(results[i][y][1]):
                if(results[i][y][0] == "royal_flush"):
                    playerhighesthand[i] = 1
                    break
                elif(results[i][y][0] == "straight_flush"):
                    playerhighesthand[i] = 2
                    break
                elif(results[i][y][0] == "four_of_a_kind"):
                    playerhighesthand[i] = 3
                    break
                elif(results[i][y][0] == "full_house"):
                    playerhighesthand[i] = 4
                    break
                elif(results[i][y][0] == "flush"):
                    playerhighesthand[i] = 5
                    break
                elif(results[i][y][0] == "straight"):
                    playerhighesthand[i] = 6
                    break
                elif(results[i][y][0] == "three_of_a_kind"):
                    playerhighesthand[i] = 7
                    break
                elif(results[i][y][0] == "two_pair"):
                    playerhighesthand[i] = 8
                    break
                elif(results[i][y][0] == "one_pair"):
                    playerhighesthand[i] = 9
                    break
                elif(results[i][y][0] == "high_card"):
                    playerhighesthand[i] = 10
                    break
    winners = []
    
    for i in range(NUM_PLAYERS):
        
        if(playerhighesthand[i] < minimum):
            minimum = playerhighesthand[i]
            winner = i
            winners.clear()
            winners.append(i)
        elif(playerhighesthand[i] == minimum):
            winners.append(i)
            
    if(len(winners) > 1):
        
        for i in range(len(winners)):
            handwon[winners[i]] = PLAYERPOCKETS[winners[i]] 
    else:
            handwon[winner] = PLAYERPOCKETS[winner]

    return handwon, winners, playerhighesthand

    
suits = ["clubs","hearts","diamonds","spades"]

values = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]

count = 0
while True:
    listception = []
    count += 1
    print(count)

    hands = {1: 0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0}

    for z in range(10000):
        
        Deck = []

        for i in range(len(values)):
            for y in range(len(suits)):
                Deck.append((values[i],suits[y]))
                

        readyDeck = shuffleDeck(Deck)

        deal_cards(readyDeck)

        realcards = PLAYERPOCKETS

        combine_cards(PLAYERPOCKETS, COMMUNITYCARDS)

        results = evaluate_hands(COMBINEDCARDS)
        
        handswon = evaluate_results(results)

        for i in handswon[0].keys():
            listception.append((handswon[0][i][0], handswon[0][i][1]))

        
        resultsdic = handswon[2]
        res = resultsdic[handswon[1][0]]

        if(res == 1):
            hands[res] += 1
        if(res == 2):
            hands[res] += 1
        if(res == 3):
            hands[res] += 1
        if(res == 4):
            hands[res] += 1
        if(res == 5):
            hands[res] += 1
        if(res == 6):
            hands[res] += 1
        if(res == 7):
            hands[res] += 1
        if(res == 8):
            hands[res] += 1
        if(res == 9):
            hands[res] += 1
        if(res == 10):
            hands[res] += 1

    print(hands)
    """
    def Reverse(tuples):
        new_tup = ()
        for k in reversed(tuples):
            new_tup = new_tup + (k,)
        return new_tup

    for i in range(len(listception)-1):
        for y in range(1,len(listception)):
            if(listception[i] == Reverse(listception[y])):
                listception[y] = Reverse(listception[y])

    countedlist = Counter(listception)

    sortedcountlist = dict(sorted(countedlist.items(), key=lambda item: item[1]))

    rsortedcountlist = dict(reversed(list(sortedcountlist.items())))
    """
    if(NUM_PLAYERS == 9):
        #df9 = pd.DataFrame([rsortedcountlist])
        #df9_t = df9.transpose()
        df9 = pd.DataFrame([hands])
        df9_t = df9.transpose()
        writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
        df9_t.to_excel(writer, sheet_name='Sheet8', index=[0])
        writer.save()
        NUM_PLAYERS += 1
        break
    break
    """
        df2_t.to_excel(writer, sheet_name='Sheet1', index=[0])
        df3_t.to_excel(writer, sheet_name='Sheet2', index=[0])
        df4_t.to_excel(writer, sheet_name='Sheet3', index=[0])
        df5_t.to_excel(writer, sheet_name='Sheet4', index=[0])
        df6_t.to_excel(writer, sheet_name='Sheet5', index=[0])
        df7_t.to_excel(writer, sheet_name='Sheet6', index=[0])
        df8_t.to_excel(writer, sheet_name='Sheet7', index=[0])
        df9_t.to_excel(writer, sheet_name='Sheet8', index=[0])
    """
"""
    if(NUM_PLAYERS == 2):
        df2 = pd.DataFrame([rsortedcountlist])
        df2_t = df2.transpose()
        NUM_PLAYERS += 1
        break
    elif(NUM_PLAYERS == 3):
        df3 = pd.DataFrame([rsortedcountlist])
        df3_t = df3.transpose()
        
        NUM_PLAYERS += 1
    elif(NUM_PLAYERS == 4):
        
        df4 = pd.DataFrame([rsortedcountlist])
        df4_t = df4.transpose()
        
        NUM_PLAYERS += 1
    elif(NUM_PLAYERS == 5):
        
        df5 = pd.DataFrame([rsortedcountlist])
        df5_t = df5.transpose()
        
        NUM_PLAYERS += 1
    elif(NUM_PLAYERS == 6):
        
        df6 = pd.DataFrame([rsortedcountlist])
        df6_t = df6.transpose()
        
        NUM_PLAYERS += 1
    elif(NUM_PLAYERS == 7):
        
        df7 = pd.DataFrame([rsortedcountlist])
        df7_t = df7.transpose()
        
        NUM_PLAYERS += 1
    elif(NUM_PLAYERS == 8):
        
        df8 = pd.DataFrame([rsortedcountlist])
        df8_t = df8.transpose()

        NUM_PLAYERS += 1
"""
    
    #print(countedlist)
