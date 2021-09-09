import time
import os
import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def clear():
    os.system("cls")

def Pause(p):
    time.sleep(p)

def Menu():
    print("Main Menu \n"
          "\n"
          "Game: \n"
          " 1. Rules [WIP]\n"
          " 2. Tutorial [WIP] \n"
          " 3. Player vs Computer [WIP]\n"
          " 4. Player vs Player vs Computer [WIP] \n"
        "\nCode: [WIP]\n"
          " 5. Resources [WIP]\n"
          " 6. Other Notes [WIP]\n"
        "\n 7. EXIT")





while True:
    Menu()
    input("END")


while True:
    try:
        MenuSelect = int(input("Please input a corresponding number: "))

        if MenuSelect < 1:
            print("Invalid Input")
            time.sleep(1)
            continue
        if MenuSelect >= 7:
            print("Invalid Input")
            time.sleep(1)
            continue
        if MenuSelect <= 6:
            break
    except ValueError:
        print("Invalid Input")
        time.sleep(1)
        continue


#____________________________________Main Menu____________________________________

if MenuSelect == 1:
    clear()
    time.sleep(1)
    print("Welcome to Blackjack, the rules are simple: \n"
          "Rules... \n")


elif MenuSelect == 2:
    print(MenuSelect)

elif MenuSelect == 3:
    print(MenuSelect)

elif MenuSelect == 4:
    print(MenuSelect)

elif MenuSelect == 5:
    print(MenuSelect)

elif MenuSelect == 6:
    print(MenuSelect)


input()
