import time
import random

print("Welcome to JT-team's game palace! Now, you're start the game call 'Bills'. Press 'S' for start, or 'Q'for quit.")
choose = input()                          # TODO: Choose start or exit.
if choose == 'S':
    print("Ready？'H' for help, 'E' for exit.Nothing for start.")
    chose = input()
    if chose == 'H':
        print("S' for shop.You can buy something practical there.")
        print("Input things I tell you.")
        print("If you input right, you will get point.If the input is wrong, you lose one point.")
    elif chose == '':
        pass
    elif chose == 'E':
        print("Welcome to back again!")
elif choose == 'Q':
    print("Welcome to back again!")       # TODO: Break game.
