import time; import os; import random

os.system("title Blackjack By Conner")
os.system("color F0")  # white on black cmd

global deck
deck = []
houses = ["♠", "♣", "♥", "♦"]
for i in range(4):
    for j in range(13):
        deck.append(str(j + 2) + str(houses[i]))
# 2, 3, 4, 5, 6, 7, 8, 9, 10, J(11), Q(12), K(13), A(14)
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,    10,    10,    11/1
print(deck)


def clear():  # Clear Screen
    os.system("cls")

def Pause(p):  # pause
    print("PAUSE", p)
    # time.sleep(p)

def Menu():  # main menu
    global players
    while True:
        while True:
            try:
                clear()
                print("\n══════════════[ Blackjack ]═════════════"
                      "\n 1 | Player vs Computer [WIP]"
                      "\n 2 | Player vs Player vs Computer [WIP]"
                      "\n════════════════[ Help ]════════════════"
                      "\n 3 | Rules        [TBD]"
                      "\n 4 | Resources    [TBD]"
                      "\n 5 | Other Notes  [TBD]"
                      "\n════════════════[ EXIT ]════════════════"
                      "\n 6 | EXIT")
                print("\nEnter a corresponding number")
                MenuSelect = int(input("|> "))
                if MenuSelect in range(8): break
                else:   print("Invalid Input"); Pause(p=1)
            except:     print("Invalid Input"); Pause(p=1)

        if MenuSelect == 1:  # P Vs C
            clear()
            print("Initiating Game with 1 player")
            Pause(p=0.5)
            players = 1
            return 1
        elif MenuSelect == 2:  # P Vs P Vs C
            clear()
            print("Initiating Game with 2 players")
            Pause(p=0.5)
            players = 2
            return 2

        elif MenuSelect == 3:  # Rules
            clear()
            print("TBD")
            input("Press [ENTER] to continue")
        elif MenuSelect == 4:  # resources
            clear()
            print("TBD")
            input("Press [ENTER] to continue")
        elif MenuSelect == 5:  # other notes
            clear()
            print("TBD")
            input("Press [ENTER] to continue")

        elif MenuSelect == 6:  # exit
            clear()
            print("Goodbye")
            Pause(p=1)
            quit()

def CardPrint(hand, all):
    for i in range(6):
        globals()["line" + str(i)] = []
    for i in range(len(hand)):

        CARDHOUSE = (hand[i][-1])
        if CARDHOUSE in ("♠", "♣"):
            TEXTCOLOUR = 30  # Black
        if CARDHOUSE in ("♥", "♦"):
            TEXTCOLOUR = 31  # Red

        if   int(hand[i][0:-1]) == 11: CARD = "J "
        elif int(hand[i][0:-1]) == 12: CARD = "Q "
        elif int(hand[i][0:-1]) == 13: CARD = "K "
        elif int(hand[i][0:-1]) == 14: CARD = "A "
        else:                          CARD = hand[i][0:-1]

        if hand[i][0:-1] == hand[i][-2]: CARD = CARD + " "

        if all == False and i == 0: CARDHOUSE = "?"; TEXTCOLOUR = 35; CARD = "??"

        globals()["line0"].append("\033[1;{}m╔══════╗".format(TEXTCOLOUR))
        globals()["line1"].append("\033[1;{}m║{}     ║".format(TEXTCOLOUR, CARDHOUSE))
        globals()["line2"].append("\033[1;{}m║  {}  ║".format(TEXTCOLOUR, CARD))
        globals()["line3"].append("\033[1;{}m║      ║".format(TEXTCOLOUR))
        globals()["line4"].append("\033[1;{}m║     {}║".format(TEXTCOLOUR, CARDHOUSE))
        globals()["line5"].append("\033[1;{}m╚══════╝".format(TEXTCOLOUR))

    for i in range(6):
        globals()["CLEANline" + str(i)] = ""
    for x in range(6):
        for z in range(0, len(globals()["line" + str(x)])):
            globals()["CLEANline" + str(x)] = globals()["CLEANline" + str(x)] + globals()["line" + str(x)][z]
        print(globals()["CLEANline" + str(x)])

def Game(Players):
    (globals()["P1"]) = []
    (globals()["P2"]) = []
    (globals()["P1score"]) = []
    (globals()["P2score"]) = []
    HOUSE = []
    HOUSEscore = []
    clear()

    # Shuffle Deck
    GameDeck = deck.copy()
    print("Shuffling Deck")
    for i in range(random.randint(10, 200)): random.shuffle(GameDeck)
    print(deck)  # Debug
    print(GameDeck)  # Debug
    Pause(p=0.5)

    # Deal first hands
    for i in range(0, 2):
        HOUSE.append(GameDeck[0])
        GameDeck.pop(0)
        for x in range(0, Players):
            (globals()["P"+str(x + 1)]).append(GameDeck[0])
            GameDeck.pop(0)

            # SCORE
            # if card is a J, Q, or K, add 10 to score
            if   int(globals()["P" + str(x + 1)][i][0:-1]) == 11: (globals()["P"+str(x + 1)+"score"]).append(10)
            elif int(globals()["P" + str(x + 1)][i][0:-1]) == 12: (globals()["P"+str(x + 1)+"score"]).append(10)
            elif int(globals()["P" + str(x + 1)][i][0:-1]) == 13: (globals()["P"+str(x + 1)+"score"]).append(10)
            elif int(globals()["P" + str(x + 1)][i][0:-1]) == 14:
                # If no other aces, add (11) to score
                if 14 not in (globals()["P" + str(x + 1)]): (globals()["P"+str(x + 1)+"score"]).append(11)
                # else (there is an ace), add (1) to score
                else: (globals()["P" + str(x + 1) + "score"]).append(1)
            # otherwise add regular card's value to score
            else: (globals()["P" + str(x + 1)+"score"]).append(int(globals()["P" + str(x + 1)][i][0:-1]))



    # game
    while True:
        # player turn
        for x in range(players):
            print("House's Hand"); CardPrint(hand=HOUSE, all=False)
            print("Your Hand:  Score: {}".format(globals()["P" + str(x + 1) + "score"])); CardPrint(hand=globals()["P" + str(x + 1)], all=True)
            print("[1]Hit or [2]stand")
            while True:
                input("|> ")

    print("HOUSE", HOUSE)
    print("P1", (globals()["P1"]))
    print("P2", (globals()["P2"]))


def Score():
    clear()
    print("SCORE TBD")


while True: # Program loops endlessly
    Players = Menu()
    Game(Players=Players)
    Score()
    input("END OF CODE")

