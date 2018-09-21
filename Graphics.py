import pygame as pyg
import pygame.color as c
from Graphics.Elements import *



pyg.init()
pyg.font.init()

scn_width = 1024
scn_height = 640

BG1 = Image(['image', (0, 0), 'Images/bg1.jpg', (1024, 640)])

win = pyg.display.set_mode((scn_width, scn_height))

pyg.display.set_caption("A Pirate's Life For Me")

x = 10
y = 430
x1, y1 = 0, 0
width = 40
height = 60
vel = 15

isJump = False
jumpCount = 10
run = True
mouse_down = False

while run:
    pyg.time.delay(100)

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            run = False
        elif event.type == pyg.MOUSEBUTTONDOWN:
            mouse_down = True
        elif event.type == pyg.MOUSEBUTTONUP:
            mouse_down = False

    if mouse_down:
        x1, y1 = pyg.mouse.get_pos()

    keys = pyg.key.get_pressed()

    BG1.draw(win)
    rek1 = Rect(['rect', (x1,y1), (height, width), c.Color('blue')])
    rek1.draw(win)
    string = 'Hello World!'
    myfont = pyg.font.SysFont('Comic Sans MS', 30)
    box1_vars = ['textbox', (x1+width*2, y1), ((30*0.75)*1.25, (30*0.75)*len(string)), c.Color('Red'),
                 string, (myfont, (255, 255, 255))]
    box1 = TextBox(box1_vars)
    box1.rect.width *= 2
    box1.draw(win)
    pyg.display.update()

pyg.quit()

