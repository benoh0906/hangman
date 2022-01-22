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

def randomWorld():
    file = open('wordss.txt')
    f = file.readlines()
    i = random.randrange(0, len(f) - 1)

    return f[i][:-1]

def hang(guess):
    global world
    if guess.lower() not in word.lower():
        return True
    else:
        return False

def spacedOut(word, guessed=[]):
    spacedWord = ''
    guessedLetters = guessed
    for x in range(len(word)):
        if word[x] != ' ':
            spacedWorld += '_ '
            for i in range(len(guessedLetters)):
                if word[x].upper() == guessedLetters[i]:
                    spacedWord = spacedWord[:-2]
                    spacedWorld += world[x].upper() = ' '
        elif word[x] == ' ':
            spacedWorld += ' '
    return spacedWord

def buttonHit(x, y):
    for i in range(len(buttons)):
        if x < buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y> buttons[i][2] - 20:
                return buttons [i][5]
    return None 

def buttonHit(x,y):
    for i in range(len(buttons)):
        if x< buttons[i][1] + 20 and x > buttons[i][1] - 20:
            if y < buttons[i][2] + 20 and y > buttons[i][2]-20:
                return buttons[i][5]
    return None 

def end(winner=False):
    global limbs
    lostTxt = 'You Lost, press any key to play again...'
    winTxt = 'WINNER!, press any key to play again...'
    redraw_game_window()
    pygame.time.delay(1000)
    win.fill(Green)

    if winner == True:
        label = lost_front.render(winTxt, 1, BLACK)
    else:
        label = lost_font.render(lostTxt,1,BLACK)
    
    wordTxt = lost_font.render(word.upper(),1,BLACK)
    wordWas = lost_font.render('The phrase was: ', 1, BLACK)

    win.blit(wordTxt, (winWidth/2 - wordTxt.get_width()/2, 295))
    win.blit(wordWas, (winWidth/2 - wordWas.get_width()/2, 245))
    win.blit(label, (winWidth / 2 - label.get_width() / 2, 140))
    pyhame.display.update()
    again = True
    while again:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type = pygame.KEYDOWN:
                again=False
    reset()

def reset():
    global limbs
    global guessed
    global buttons
    global word
    for i in range(len(buttons)):
        buttons[i][4]= True

    limbs = 0
    guessed = []
    word = randomWord()

#MAINLINE

#setup buttons
increase = round(winWidth / 13)
for i in range (26):
    if i < 13:
        y = 40
        x = 25 + (increase * i)
    else:
        x = 25 + (increase * (i-13))
        y = 85
    buttons.append([LIGHT_BLUE, x, y, 20,True, 65+i])

word = randomWord()
inPlay = True

while 


    