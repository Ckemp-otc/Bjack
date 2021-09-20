import time
import os
import random

os.system("Blackjack By Conner ;)")
os.system("color 70")

global deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def clear():
    os.system("cls")

def Pause(p):
    print("PAUSE",p)
    #time.sleep(p)

def Menu():
    global players
    while True:
        while True:
            try:
                clear()
                print("Game: \n"
                      " 1. Rules [WIP] \n"
                      " 2. Tutorial [WIP] \n"
                      " 3. Player vs Computer [WIP] \n"
                      " 4. Player vs Player vs Computer [WIP] \n"
                    "\nCode: [WIP] \n"
                      " 5. Resources [WIP]\n"
                      " 6. Other Notes [WIP]\n"
                    "\n 7. EXIT")
                MenuSelect = int(input("Please input a corresponding number: "))
                if MenuSelect in range(0, 8):
                    break
                else:
                    print("Invalid Input")
                    Pause(p=1)
            except:
                print("Invalid Input")
                Pause(p=1)

        if MenuSelect == 1: # Rules
            clear()
            print("TBD")
            input("Press [ENTER] to continue")

        if MenuSelect == 2: # Tutorial
            clear()
            print("TBD")
            input("Press [ENTER] to continue")

        if MenuSelect == 3: # P Vs C
            clear()
            print("Initiating Game with 1 player")
            Pause(p=1)
            return 1

        if MenuSelect == 4: # P Vs P Vs C
            clear()
            print("Initiating Game with 2 players")
            Pause(p=1)
            return 2

        if MenuSelect == 5: # resources
            clear()
            print("TBD")
            input("Press [ENTER] to continue")

        if MenuSelect == 6: # other notes
            clear()
            print("TBD")
            input("Press [ENTER] to continue")

        if MenuSelect == 7: # exit
            clear()
            print("Goodbye")
            Pause(p=1)
            quit()


def Game(Players):
    (globals()["P1"])=[]
    (globals()["P2"])=[]
    HOUSE=[]
    clear()

    # Shuffle Deck
    GameDeck = deck.copy()
    print("Shuffling Deck")
    for i in range(random.randint(10,200)):
        random.shuffle(GameDeck)
    print(deck)         # Debug
    print(GameDeck)     # Debug
    Pause(p=1.5)

    # Deal first hands
    for i in range(0,2):
        HOUSE.append(GameDeck[random.randint(0,len(GameDeck))])
        GameDeck.pop(HOUSE[-1])
        for x in range(0,Players):
            (globals()["P"+str(x+1)]).append(GameDeck[random.randint(0,len(GameDeck))])
            GameDeck.pop((globals()["P"+str(x+1)])[-1])

    print("HOUSE",HOUSE)
    print("P1",(globals()["P1"]))
    print("P2",(globals()["P2"]))



    print(GameDeck)
    print("Dif:",sum(deck)-sum(GameDeck))

def Score():
    clear()
    print("SCORE TBD")

while True:
    Players = Menu()
    Game(Players=Players)
    Score()
    input("END OF CODE")

