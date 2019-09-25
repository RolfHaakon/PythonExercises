"""
Create a function that takes in two lists and determines whether there exists a flush.

    The first list represents the 5 cards dealt on the table.
    The second list represents the 2 cards in your hand.

Notation: card number and suit (abbreviated as S = Spades, H = Hearts, D = Diamonds, C = Clubs) separated by an underscore.
"""


hand = ['5_D', 'Q_H']
table = ['8_H', '10_H', '10_D', 'J_H', '10_S']



def check_flush(table, hand):
    total =  {"S":0 , "H":0,"D":0,"C":0}
    for i in table:
        suit = i.split('_')
        total[suit[1]] += 1
    print(total)
    for i in hand:
        suit = i.split('_')
        total[suit[1]] += 1
    print(total)
    for i in total:
        if total[i] >= 5:
            return True
    return False


print(check_flush(table,hand))