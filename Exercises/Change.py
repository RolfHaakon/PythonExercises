# Write a simple program that takes the input change and delivers the minimum amout of coins needed to give back change

def min_coins(change):
    numcoin = 0
    coins = [25, 10, 5, 1]
    for coin in coins:
        if change // coin > 0:
            numcoin += change // coin
            change -= coin * (change // coin)
    print(numcoin)


min_coins(50)
min_coins(76)
min_coins(77)