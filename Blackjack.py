import time
import os
import random

os.system("title Blackjack By Conner ;)")
os.system("color F0")

global deck
deck=[]
houses=["♠","♣","♥","♦"]
for i in range(4):
    for j in range(13):
        deck.append(str(j+2)+str(houses[i]))


print(deck)

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
                print("══════════════[ Blackjack ]═════════════ \n"
                      " 1 | Player vs Computer [WIP] \n"
                      " 2 | Player vs Player vs Computer [WIP] \n"
                      "════════════════[ Help ]════════════════ \n"
                      " 3 | Rules        [TBD] \n"
                      " 4 | Resources    [TBD]\n"
                      " 5 | Other Notes  [TBD]\n"
                      "════════════════[ EXIT ]════════════════ \n"
                      " 6 | EXIT")
                print("\nEnter a corresponding number\n")
                MenuSelect = int(input("|> "))
                if MenuSelect in range(0, 8):
                    break
                else:
                    print("Invalid Input")
                    Pause(p=1)
            except:
                print("Invalid Input")
                Pause(p=1)

        if MenuSelect == 1: # P Vs C
            clear()
            print("Initiating Game with 1 player")
            Pause(p=1)
            return 1

        if MenuSelect == 2: # P Vs P Vs C
            clear()
            print("Initiating Game with 2 players")
            Pause(p=1)
            return 2

        if MenuSelect == 3: # Rules
            clear()
            print("TBD")
            input("Press [ENTER] to continue")

        if MenuSelect == 4: # resources
            clear()
            print("TBD")
            input("Press [ENTER] to continue")

        if MenuSelect == 5: # other notes
            clear()
            print("TBD")
            input("Press [ENTER] to continue")

        if MenuSelect == 6: # exit
            clear()
            print("Goodbye")
            Pause(p=1)
            quit()

def CardPrint(hand):

    for i in range(hand):
        globals()["line0"].append("\033[0;30;{} {}     ".format(BACKGROUNDCOLOUR, PRINTNUMBER))
        globals()["line1"].append("\033[0;{};{}╔══════╗".format(TEXTCOLOUR, BACKGROUNDCOLOUR))
        globals()["line2"].append("\033[0;{};{}║{}    ║".format(TEXTCOLOUR, BACKGROUNDCOLOUR))
        globals()["line3"].append("\033[0;{};{}║ {} ║"  .format(TEXTCOLOUR, BACKGROUNDCOLOUR, CARDTYPE))
        globals()["line4"].append("\033[0;{};{}║      ║".format(TEXTCOLOUR, BACKGROUNDCOLOUR, CARDCOLOUR))
        globals()["line5"].append("\033[0;{};{}║    {}║".format(TEXTCOLOUR, BACKGROUNDCOLOUR))
        globals()["line6"].append("\033[0;{};{}╚══════╝".format(TEXTCOLOUR, BACKGROUNDCOLOUR))


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

    GameEnded=False
    while GameEnded==False:
        for i in range(Players):
            print("[{}][?]".format(HOUSE[0]))
            for x in range(len(globals()["P"+str(i+1)])):
                print("\r[{}]\r".format(globals()["P"+str(i+1)][x]))
            input()



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

