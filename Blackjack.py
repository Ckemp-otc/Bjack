import time
import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def clear():
    os.system("cls")

def Pause(p):
    print("PAUSE",p)
    #time.sleep(p)

def Menu():
    global players
    while True:
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

        while True:
            try:
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

def Game():
    clear()
    print("TBD")

def Score():
    clear()
    print("TBD")

while True:
    Players = Menu()
    Game(Players=Players)
    Score()
    input("END")

