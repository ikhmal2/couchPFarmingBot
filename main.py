import pyautogui as auto
import time
import keyboard
import numpy as np
from random import randint

print("Couch Potato Bot Starting in 5 seconds...\nSwitch Tabs Now")
time.sleep(5)
debug = True
nakExit = False
if keyboard.is_pressed('q'):
    nakExit = True
    print("mencuba stop")
    
counter = 0

def CheckIfBattle():
    global counter
    if nakExit == True:
        exit("berhenti dah")
    find = auto.locateOnScreen(
        "Images/book.jpg", confidence=0.7, grayscale=False)
    time.sleep(np.random.uniform(0.1, 0.5))
    if find:
        if debug == True:
            print("Not in battle")
        CheckIfBattle()
    else:
        time.sleep(0.5)
        if debug == True:
            print("Entered Battle...")
        counter =+ 1
        SelectPowerUp()


def SelectPowerUp():
    auto.move(0, 300, duration=1)
    find = auto.locateOnScreen("Images/1.jpg", confidence=0.5, grayscale=False)
    if debug == True:
        print("Looking for Enchantment...")
    if find:
        if debug == True:
            print("Selecting Enchantment...")
        button = auto.center(find)

        auto.click(button)
        auto.click(button)
        time.sleep(np.random.uniform(0.1, 0.3))
        MoveMouseOutWay()
        SelectAOE()
    else:
        # Avoid Overload
        time.sleep(np.random.uniform(0.1, 0.5))
        SelectPowerUp()


def WanderAbout():

    def Walk(button, time):
        if debug == True:
            print(button)
        with auto.hold(button):
            auto.time.sleep(time)

    def Input(input):
        num = randint(1, 2)
        if input == 0:
            Walk("Space", num)
        if input == 1:
            Walk("W", num)
            Walk("S", num)
        if input == 2:
            Walk("S", num)
            Walk("W", num)
        if input == 3:
            Walk("A", num)
            Walk("D", num)
        if input == 4:
            Walk("D", num)
            Walk("A", num)

    def GenerateInput():
        if debug == True:
            print("Generating Randomised Walkabouts...")
        num = randint(0, 4)
        Input(num)
        num = randint(0, 4)
        Input(num)
        num = randint(0, 4)
        Input(num)
        num = randint(0, 4)
        Input(num)
        if debug == True:
            print(f"Completed walkabout")
        CheckIfBattle()

    find = auto.locateOnScreen(
        "Images/book.jpg", confidence=0.7, grayscale=False)
    if find:
        time.sleep(0.5)
        if debug == True:
            print("Battle has ended...")
        GenerateInput()
    else:
        if debug == True:
            print("Waiting for battle to end...")
        time.sleep(1)
        WanderAbout()


def SelectAOE():
    find = auto.locateOnScreen("Images/2.png", confidence=0.6, grayscale=False)
    notEnoughPips = auto.locateOnScreen("Images/piptakcukup.png", confidence=0.6, grayscale=False)
    passBtn = auto.locateOnScreen("Images/pass.png", confidence=0.6, grayscale=False)
    
    # if debug == True:
    #     print("Not enough pips, need to pass")
    # if notEnoughPips:
    #     button = auto.center(passBtn)
    #     auto.click(button)
    
    if debug == True:
        print("Looking for AOE...")
    if find:
        if debug == True:
            print("Selecting Enchantment...")
        button = auto.center(find)

        time.sleep(np.random.uniform(0.1, 0.3))
        auto.click(button)
        time.sleep(np.random.uniform(0.1, 0.3))
        auto.click(button)

        def CastAOE():
            MoveMouseOutWay()
            if debug == True:
                print("Looking for AOE")
            find = auto.locateOnScreen(
                "Images/3.png", confidence=0.9, grayscale=False)
            if find:
                button = auto.center(find)
                time.sleep(np.random.uniform(0.1, 0.3))
                auto.click(button)
                time.sleep(np.random.uniform(0.1, 0.4))
                auto.click(button)
                if debug == True:
                    print("Completed")
                WanderAbout()
            else:
                CastAOE()

        CastAOE()
    else:
        # Avoid Overload
        time.sleep(np.random.uniform(1, 2))
        SelectAOE()


def MoveMouseOutWay():
    auto.move(0, 200)

# CheckIfBattle()
try:
    CheckIfBattle()
except KeyboardInterrupt:
	#Statements to execute upon that exception
    print("this is how many times the the program ran: ", counter)
else:
	#Statements when no exception occurs
	CheckIfBattle()