import time
import os

def clear():
    os.system("cls")

print("Main Menu \n"
      "\n"
      "Game: \n"
      " 1. Introduction \n"
      " 2. Tutorial [WIP] \n"
      " 3. One Player \n"
      " 4. Player vs Player [WIP] \n"
      "\n"
      "Code: \n"
      " 5. Resources \n"
      " 6. Other Notes \n")

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
