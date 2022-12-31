import slotmachine

money = 20
keepPlay = True

def main():

    global keepPlay

    while keepPlay:
        addMoney()
        rollSlotMachine()

        keepPlay = input("Do you want to keep playing? (Y/N)")
        keepPlay = booleanAnswerConvert(keepPlay)

def addMoney():
    isInsertingMoney = input("Do you want to insert money? (Y/N)")

    isInsertingMoney = booleanAnswerConvert(isInsertingMoney)
    
    if isInsertingMoney == False:
        return

    amountOfMoneyToPlay = input("How much money do you want to add?")
    try:
        amountOfMoneyToPlay = float(amountOfMoneyToPlay)
        slotmachine.deposit(amountOfMoneyToPlay)
    except: 
        print("This was not a number.")

def rollSlotMachine():
    isRolling = input("Do you want to play the slotmachine? (Y/N)")

    isRolling = booleanAnswerConvert(isRolling)

    if isRolling == False:
        return

    slotmachine.rollSlotMachine()

def booleanAnswerConvert(variableInQuestion):
    if variableInQuestion == "N":
        return False
    else:
        return True

main()