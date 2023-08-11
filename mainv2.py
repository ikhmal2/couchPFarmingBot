import pyautogui as auto
import time
import keyboard
import numpy as np
from random import randint

print("Couch Potato Bot Starting in 5 seconds...\nSwitch Tabs Now")
time.sleep(5)

# setting up global variables
debug = True
exiting = False
counter = 0

# utility def starts here
def MoveMouseOutWay(): # nak jauhkan mouse dari spell sekejap
    auto.move(0, 200)

# tekan echanent punya spell
def CastAOE():
	MoveMouseOutWay()
	if debug == True:
		print("Looking for AOE")
	humangofrogEnchanted = auto.locateOnScreen(
		"Images/3.png", confidence=0.9, grayscale=False)
	if humangofrogEnchanted:
		button = auto.center(humangofrogEnchanted)
		time.sleep(np.random.uniform(0.1, 0.3))
		auto.click(button)
		time.sleep(np.random.uniform(0.1, 0.4))
		auto.click(button)
		if debug == True:
			print("Completed")
		WanderAbout()
	else:
		CastAOE()

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

def checkPips():
      notEnoughPipsFrog = auto.locateOnScreen("Images/4.png", confidence=0.9, grayscale=False)
      passBtn = auto.locateOnScreen("Images/pass.png", confidence=0.9, grayscale=False)
      if notEnoughPipsFrog:
            time.sleep(np.random.uniform(0.1, 0.4))
            if debug == True:
                  print("Not enough pips need to pass")
                  time.sleep(np.random.uniform(0.1, 0.4))
                  button = auto.center(passBtn)
                  time.sleep(np.random.uniform(0.1, 0.2))
                  auto.click(button)
                  time.sleep(np.random.uniform(0.1, 0.2))
                  auto.click(button)
                  MoveMouseOutWay()
                  return True
                  
def WanderAbout():
    buku = auto.locateOnScreen(
        "Images/book.jpg", confidence=0.7, grayscale=False)
    if buku:
        time.sleep(0.5)
        if debug == True:
            print("Battle has ended...")
        GenerateInput()
    else:
        if debug == True:
            print("Waiting for battle to end...")
        time.sleep(1)
        checkPips()
        if checkPips():
              battle()
        WanderAbout()



# check if dah masuk battle ke belum
def CheckIfBattle():
    global counter
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

# pick echant
def SelectPowerUp():
    auto.move(0, 300, duration=1)
    epic = auto.locateOnScreen("Images/1.jpg", confidence=0.5, grayscale=False)
    if debug == True:
        print("Looking for Enchantment...")
    if epic:
        if debug == True:
            print("Selecting Enchantment...")
        button = auto.center(epic)

        auto.click(button)
        auto.click(button)
        time.sleep(np.random.uniform(0.1, 0.3))
        MoveMouseOutWay()
    else:
        # Avoid Overload
        time.sleep(np.random.uniform(0.1, 0.5))
        SelectPowerUp()

def SelectAOE():
    humangofrogEnchanted = auto.locateOnScreen("Images/2.png", confidence=0.6, grayscale=False)    
    if debug == True:
        print("Looking for AOE...")
    if humangofrogEnchanted:
        if debug == True:
            print("Selecting Enchantment...")
        button = auto.center(humangofrogEnchanted)

        time.sleep(np.random.uniform(0.1, 0.3))
        auto.click(button)
        time.sleep(np.random.uniform(0.1, 0.3))
        auto.click(button)
    else:
        # Avoid Overload
        time.sleep(np.random.uniform(1, 2))
        SelectAOE()

def battle():
      CheckIfBattle()
      SelectPowerUp()
      SelectAOE()
      CastAOE()

CheckIfBattle()
SelectPowerUp()
SelectAOE()
CastAOE()
WanderAbout()