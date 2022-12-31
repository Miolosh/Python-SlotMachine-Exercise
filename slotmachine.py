import random


possibleValues = ["Heart", "Coin", "Bomb"]

costOfPlay = 1
currentPlayMoney = 10.0

def deposit(money):

    global currentPlayMoney

    currentPlayMoney += money
    return currentPlayMoney

def rollSlotMachine():
    global currentPlayMoney 
    if currentPlayMoney < costOfPlay:
        return print("There was not enough money in this machine.")

    currentPlayMoney -= costOfPlay
    rolledItems = [None, None, None]
    index = 0

    for item in rolledItems:
        rolledItems[index] = random.choice(possibleValues)
        index += 1
    
    print(rolledItems)

    index = 0
    while index < len(rolledItems):
        if index == 0:
            index += 1
            continue

        if rolledItems[index -1] != rolledItems[index]:
            print("You did not win this roll. You still have ", currentPlayMoney, " left.")
            return False
        index += 1
    
    currentPlayMoney += 5
    print("Congrats you won. You have now ", currentPlayMoney , "euro")
    

