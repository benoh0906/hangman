#file name: hangman.py
#description: Starter hangmang for rusty skills

import pygame
import random

pygame.init()
winHeight = 480
winWirdth = 700
win = pygame.display.set_mode((winWidth,winHeight))

#initialise global variable/constants

BLACK = (0,0, 0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,244,0)
BLUE = (0,0,255)
LIGHT_BLUE = (102,255,255)

btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace",24)
lost_font = pygame.font.SysFont("arial",45)
word=''
buttons = []
guessed = []
hangmanPics = [pygame.image.load('hangman0.png'),pygame.image.load('hangman1.png'),pygame.image.load('hangman2.png'),pygame.image.load('hangman3.png'),pygame.image.load('hangman4.png'),pygame.image.load('hangman5.png'),pygame.image.load('hangman6.png')]

limbs = 0

def = redraw_game_window():
    global guessed
    global hangmanPics
    global limbs
    win.fill(GREEN)
    # Buttons
    for i in range (len(buttons)):
        if buttons[i][4]:
            pygame.draw.circle(win, BLACK, (buttons[i][1],buttons[i][2]),buttons[i][3])
            pygame.draw.circle(win, buttons[i][0], (buttons[i][1],buttons[i][2]),buttons[i][3] - 2)
            label=btn_font.render(chr(buttons[i][5]), 1, BLACK)
            win.blit(label, (buttons[i][1] - (labels.get_width() / 2), buttons[i][2] - (label.get_height() / 2)))

            spaced = spacedOut(word,guessed)
            label1 = guess_font.render(spaced, 1, BLACK)
            rect = label1.get_rect()
            length = rect[2]

            win.blit(label1,(winWidth/2 - length/2. 400))

            pic = hangmanPics[limbs]
            win.blit(pic, (winWidth/2 - pic.get_width()/2 + 20, 150))
            pygame.display.update()
            