import pyautogui
import pygame
from time import sleep
import pyautogui
from keyboard import press
from tqdm import tqdm
import time
import sys
from colorama import Fore, Back, Style
import webbrowser
import reloadex
import random



url = "https://github.com/dannybanno"

def delay_print(s):
  for c in s:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.000000001)


delay_print(Fore.GREEN + '''


 ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████      ▄████▄   ██▓     ██▓ ▄████▄   ██ ▄█▀▓█████  ██▀███  
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒   ▒██▀ ▀█  ▓██▒    ▓██▒▒██▀ ▀█   ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒   ▒▓█    ▄ ▒██░    ▒██▒▒▓█    ▄ ▓███▄░ ▒███   ▓██ ░▄█ ▒
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░   ▒▓▓▄ ▄██▒▒██░    ░██░▒▓▓▄ ▄██▒▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄  
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░   ▒ ▓███▀ ░░██████▒░██░▒ ▓███▀ ░▒██▒ █▄░▒████▒░██▓ ▒██▒
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░    ░ ░▒ ▒  ░░ ▒░▓  ░░▓  ░ ░▒ ▒  ░▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░      ░  ▒   ░ ░ ▒  ░ ▒ ░  ░  ▒   ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒     ░          ░ ░    ▒ ░░        ░ ░░ ░    ░     ░░   ░ 
      ░  ░   ░                  ░ ░     ░ ░          ░  ░ ░  ░ ░      ░  ░      ░  ░   ░     
                                        ░                    ░                               

Made by dannybanno#1848

''')

ClickA = input('''Which type do you want to use: 
[1] - Double click
[2] - Single click
[3] - Right click
''')

if ClickA == "1":
  ClickB = input("How many clicks do you want to auto click: ")
  for i in tqdm(range(10)):
    sleep(0.5)
  for i in range(0, int(ClickB)):
    pyautogui.doubleClick()
  for i in range(1):
    print("clicking " + ClickB + " times")
if ClickA == "2":
  ClickB = input("How many clicks do you want to auto click: ")
  print("You have 5 seconds to go to the window you want to use the auto clicker on!")
  for i in tqdm(range(10)):
    sleep(0.5)
  for i in range(0, int(ClickB)):
    pyautogui.click()
  for i in range(1):
    print("clicking " + ClickB + " times")
if ClickA == "3":
  ClickB = input("How many clicks do you want to right auto click: ")
  print("You have 5 seconds to go to the window you want to use the auto clicker on!")
  for i in tqdm(range(10)):
    sleep(0.5)
  for i in range(0, int(ClickB)):
    pyautogui.click(button='right')
  for i in range(1):
    print(''''clicking ' + ClickB + ' times
    
    Thanks for downloading also look at my other files on my github - https://github.com/dannybanno 
    
    
    
    ''')

