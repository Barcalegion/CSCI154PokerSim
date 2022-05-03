from collections import Counter

def royal_flush(cmbcards,player):
    
    c,h,d,s = [], [], [], []
    A,K,Q,J,T = False,False,False,False,False
        
    for y in range(7):
        if(cmbcards[player][y][0] == "A"):
            A = True
        if(cmbcards[player][y][0] == "K"):
            K = True
        if(cmbcards[player][y][0] == "Q"):
            Q = True
        if(cmbcards[player][y][0] == "J"):
            J = True
        if(cmbcards[player][y][0] == "10"):
            T = True
        
    if (A and K and Q and J and T):
        for y in range(7):
            if(cmbcards[player][y][1] == "clubs"):
                c.append(tuple( cmbcards[player][y]))
                if(len(c) == 5):
                    return True
            if(cmbcards[player][y][1] == "hearts"):
                h.append(tuple( cmbcards[player][y]))
                if(len(h) == 5):
                    return True
            if(cmbcards[player][y][1] == "diamonds"):
                d.append(tuple (cmbcards[player][y]))
                if(len(d) == 5):
                    return True
            if(cmbcards[player][y][1] == "spades"):
                s.append(tuple(cmbcards[player][y]))
                if(len(s) == 5):
                    return True
    return False

def straight_flush(cmbcards, player):
    ccards = cmbcards
    values = []
    sortedcards = []
    ace = False
    c,h,d,s = [], [], [], []
    
    for y in range(7):
        if(ccards[player][y][1] == "clubs"):
            if ccards[player][y][0] == "A":
                values.append(14)
                c.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "K":
                values.append(13)
                c.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "Q":
                values.append(12)
                c.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "J":
                values.append(11)
                c.append(tuple(ccards[player][y]))
            else:
                values.append(int(ccards[player][y][0]))
                c.append(tuple(ccards[player][y]))
                
            
        if(ccards[player][y][1] == "hearts"):
            if ccards[player][y][0] == "A":
                values.append(14)
                h.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "K":
                values.append(13)
                h.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "Q":
                values.append(12)
                h.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "J":
                values.append(11)
                h.append(tuple(ccards[player][y]))
            else:
                values.append(int(ccards[player][y][0]))
                h.append(tuple( ccards[player][y]))
                
            
        if(ccards[player][y][1] == "diamonds"):
            if ccards[player][y][0] == "A":
                values.append(14)
                d.append(tuple (ccards[player][y]))
            elif ccards[player][y][0] == "K":
                values.append(13)
                d.append(tuple (ccards[player][y]))
            elif ccards[player][y][0] == "Q":
                values.append(12)
                d.append(tuple (ccards[player][y]))
            elif ccards[player][y][0] == "J":
                values.append(11)
                d.append(tuple (ccards[player][y]))
            else:
                values.append(int(ccards[player][y][0]))
                d.append(tuple (ccards[player][y]))
                
            
        if(ccards[player][y][1] == "spades"):
            if ccards[player][y][0] == "A":
                values.append(14)
                s.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "K":
                values.append(13)
                s.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "Q":
                values.append(12)
                s.append(tuple(ccards[player][y]))
            elif ccards[player][y][0] == "J":
                values.append(11)
                s.append(tuple(ccards[player][y]))
            else:
                values.append(int(ccards[player][y][0]))
                s.append(tuple(ccards[player][y]))
                
    sortedcards = sorted(values)
    frontlist = []
    backlist = []
    concheck = 0

    for i in range(7):
        if(sortedcards[i] == 14):
            ace = True
            
    if(len(sortedcards) == (len(set(sortedcards)))):
        frontlist = sortedcards[:4]
        backlist = sortedcards[-5:]
    else:
        sortedcards = list(set(sortedcards))
        frontlist = sortedcards[:4]
        backlist = sortedcards[-5:]

    if(len(c) >= 5):
        i = 0
        y = 1
        if(ace):
            if(frontlist == [2,3,4,5]):
                return True
            if(backlist == [10,11,12,13,14]):
                return True
        else:
            while i < (len(sortedcards)-1):
                if(sortedcards[i]-sortedcards[y]) == -1:
                    concheck += 1
                    if(concheck >= 4):
                        return True
                else:
                    concheck = 0
                i +=1
                y +=1
                
    if(len(h) >= 5):
        i = 0
        y = 1
        if(ace):
            if(frontlist == [2,3,4,5]):
                return True
            if(backlist == [10,11,12,13,14]):
                return True
        else:
            while i < (len(sortedcards)-1):
                if(sortedcards[i]-sortedcards[y]) == -1:
                    concheck += 1
                    if(concheck >= 4):
                        return True
                else:
                    concheck = 0
                i +=1
                y +=1
    if(len(d) >= 5):
        i = 0
        y = 1
        if(ace):
            if(frontlist == [2,3,4,5]):
                return True
            if(backlist == [10,11,12,13,14]):
                return True
        else:
            while i < (len(sortedcards)-1):
                if(sortedcards[i]-sortedcards[y]) == -1:
                    concheck += 1
                    if(concheck >= 4):
                        return True
                else:
                    concheck = 0
                i +=1
                y +=1
    if(len(s) >= 5):
        i = 0
        y = 1
        if(ace):
            if(frontlist == [2,3,4,5]):
                return True
            if(backlist == [10,11,12,13,14]):
                return True
        else:
            while i < (len(sortedcards)-1):
                if(sortedcards[i]-sortedcards[y]) == -1:
                    concheck += 1
                    if(concheck >= 4):
                        return True
                else:
                    concheck = 0
                i +=1
                y +=1
                
    return False

def four_of_a_kind(cmbcards,player):
    ccards = cmbcards
    values = []
    sortedcards = []
    
    for y in range(7):
        if(ccards[player][y][1] == "clubs"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "hearts"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "diamonds"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "spades"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))

    sortedcards = sorted(values)
    concheck = 0
    
    i = 0
    y = 1
    while i < (len(sortedcards)-1):
        if(sortedcards[i] == sortedcards[y]):
            concheck += 1
            if(concheck >= 3):
                return True
        else:
            concheck = 0
        i +=1
        y +=1
                
    return False

def full_house(cmbcards,player):
    ccards = cmbcards
    values = []
    sortedcards = []
    
    for y in range(7):
        if(ccards[player][y][1] == "clubs"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "hearts"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "diamonds"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "spades"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))

    sortedcards = sorted(values)
    
    pr = []
    tr = []
    for x, y in Counter(sortedcards).items():
        pr.extend([x] * (y // 2))
        
    for x, y in Counter(sortedcards).items():
        tr.extend([x] * (y // 3))
    
    if((len(pr) == 3 or len(pr) == 2) and len(tr) == 1):
        return True
    
    return False

def flush(cmbcards,player):
    c,h,d,s = [], [], [], []
    
    for y in range(7):
        if(cmbcards[player][y][1] == "clubs"):
            c.append(tuple( cmbcards[player][y]))
            if(len(c) == 5):
                return True
        if(cmbcards[player][y][1] == "hearts"):
            h.append(tuple( cmbcards[player][y]))
            if(len(h) == 5):
                return True
        if(cmbcards[player][y][1] == "diamonds"):
            d.append(tuple (cmbcards[player][y]))
            if(len(d) == 5):
                return True
        if(cmbcards[player][y][1] == "spades"):
            s.append(tuple(cmbcards[player][y]))
            if(len(s) == 5):
                return True

    return False

def straight(cmbcards,player):
    ccards = cmbcards
    values = []
    sortedcards = []
    
    for y in range(7):
        if(ccards[player][y][1] == "clubs"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "hearts"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "diamonds"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "spades"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))

    sortedcards = sorted(values)

    frontlist = []
    backlist = []
    concheck = 0
    ace = False
    
    for i in range(7):
        if(sortedcards[i] == 14):
            ace = True

    if(len(sortedcards) == (len(set(sortedcards)))):
        frontlist = sortedcards[:4]
        backlist = sortedcards[-5:]
    else:
        sortedcards = list(set(sortedcards))
        frontlist = sortedcards[:4]
        backlist = sortedcards[-5:]

    i = 0
    y = 1
    if(ace):
        if(frontlist == [2,3,4,5]):
            return True
        if(backlist == [10,11,12,13,14]):
            return True
    else:
        while i < (len(sortedcards)-1):
            if(sortedcards[i]-sortedcards[y]) == -1:
                concheck += 1
                if(concheck >= 4):
                    return True
            else:
                concheck = 0
            i +=1
            y +=1
    return False

def three_of_a_kind(cmbcards,player):
    ccards = cmbcards
    values = []
    sortedcards = []
    
    for y in range(7):
        if(ccards[player][y][1] == "clubs"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "hearts"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "diamonds"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "spades"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))

    sortedcards = sorted(values)

    tr = []
    for x, y in Counter(sortedcards).items():
        tr.extend([x] * (y // 3))
        
    if(len(tr) > 0):
        return True

    return False

def two_pair(cmbcards,player):
    ccards = cmbcards
    values = []
    sortedcards = []
    
    for y in range(7):
        if(ccards[player][y][1] == "clubs"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "hearts"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "diamonds"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "spades"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))

    sortedcards = sorted(values)

    pr = []
    for x, y in Counter(sortedcards).items():
        pr.extend([x] * (y // 2))
        
    if(len(pr) >= 2):
        return True

    return False

def one_pair(cmbcards,player):
    ccards = cmbcards
    values = []
    sortedcards = []
    
    for y in range(7):
        if(ccards[player][y][1] == "clubs"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "hearts"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "diamonds"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "spades"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))

    sortedcards = sorted(values)
    
    pr = []
    for x, y in Counter(sortedcards).items():
        pr.extend([x] * (y // 2))
        
    if(len(pr) == 1):
        return True

    return False

def high_card(cmbcards,player):
    ccards = cmbcards
    values = []
    sortedcards = []
    
    for y in range(7):
        if(ccards[player][y][1] == "clubs"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "hearts"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "diamonds"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))
                
        if(ccards[player][y][1] == "spades"):
            if ccards[player][y][0] == "A":
                values.append(14)
            elif ccards[player][y][0] == "K":
                values.append(13)
            elif ccards[player][y][0] == "Q":
                values.append(12)
            elif ccards[player][y][0] == "J":
                values.append(11)
            else:
                values.append(int(ccards[player][y][0]))

    sortedcards = sorted(values)
    
    pr = []
    for x, y in Counter(sortedcards).items():
        pr.extend([x] * (y // 2))
        
    if((len(pr) <= 1) or (len(sortedcards) == len(set(sortedcards)))):
        return True

    return False
