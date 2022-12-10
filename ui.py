import math
import random
import sys
import time
from random import choice
import random as r
import pygame
from pygame.event import set_blocked

from game import Isolation

pygame.init()
blue = (0,0,255)
green = (0,125,125)
db = (0,0,70)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)
gold = (218,165,32)
lb = (173,216,230)
orange = (255,165,0)
col = [blue,green,gold,red,orange]
font_style = pygame.font.SysFont(None, 50)
data = []
n = 0
# assigning values to X and Y variable
n1 = 0
 
# create the display surface object
# of specific dimension..e(X, Y).
 
# set the pygame window name
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)
 
print("Welcome to the Isolation Game!!")
b = int(input("Enter size(n) of the board (nXn) : "))
algo = int(input("Enter the Type of Computer Agent (1-Min/Max, 2-Alpha Beta Pruning, 3-Prediction Model(n == 4)) : "))
def message(msg,color):
    mesg = font_style.render(msg, True, color)
  
# basic font for user typed
base_font = pygame.font.Font(None, 32)
user_text = ''
  
# create rectangle
input_rect = pygame.Rect(100, 250+60*(b-4), 100, 32)
  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('darkblue')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('lightblue')
color = color_passive
  
active = False
# create a surface object, image is drawn on it.
if b == 4:    
    chess_board = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\cb4x4-01.png')
elif b == 5:
    chess_board = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\cb5x5-03.png')
elif b == 6:
    chess_board = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\cb6x6-04.png')
elif b == 3:
    chess_board = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\cb3x3-04.png')
elif b == 7:
    chess_board = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\cb7x7-03.png')
elif b == 8:
    chess_board = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\chess_board.png')
image_bn = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\bN.png')
image_wn = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\wN.png')
image_bg = pygame.image.load(r'C:\Users\Shlok\Documents\TY - Semester 5\AI\112003133\Isolation - Copy\images\bg-02.png')
dis_w = 300 + (b-4)*60
dis_h = 300 + (b-4)*60
dis = pygame.display.set_mode((dis_w,dis_h))
pygame.display.update()
pygame.display.set_caption('Isolation Game')
score_font = pygame.font.SysFont("comicsansms", 35)

game_over = False
a = Isolation(b)
m = 0
a3 = 1
text = font.render('Move:', True, white, 'black')
# create a rectangular object for the
# text surface object
textRect = text.get_rect()
# set the center of the rectangular object.
textRect.center = (50, 60*(b-4)+265)
dis.blit(text,textRect)
dis.blit(chess_board, (0,0))
pygame.display.update() 
l = []
#dis.blit(image_bg,(178,2+60))
while not game_over:
      
    # it will set background color of dis
    
    if a3 == 1:
        pass
    #else:
        #print("Computer's Position :",a.c)
        #print("Current Position :", a.u)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()

        # Draws the surface object to the dis.
        # if     user types QUIT then the dis will close
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
        
            # Check for backspace
            if event.key == pygame.K_RETURN and active == True:
                # get text input from 0 to -1 i.e. end.
                #print(user_text)
                a1 = int(user_text[0]) - 1
                a2 = int(user_text[2]) - 1
                if a.game_end(0) == 1:
                        #game_over = True
                        #print("Computer Wins")
                        break
                user_text = ""
                if a.valid_move([a1,a2],m) == False and a3 == 0:
                    print("Enter Valid Move")
                    text = font.render('Enter Valid Move', True, green, blue)

                    # create a rectangular object for the
                    # text surface object
                    textRect = text.get_rect()
                    # set the center of the rectangular object.
                    textRect.center = (240 // 2, 240 // 2)
                    dis.blit(text,textRect)
                    pygame.display.update()
                    #a1 = int(input("Enter x coordinate of your move User : "))
                    #a2 = int(input("Enter y coordinate of your move User : "))
                else:
                    dis.blit(chess_board, (0,0))
                    for i in l:
                        if a.game_end(1) != 0:
                            dis.blit(image_bg,(i[0]*60,i[1]*60))
                        elif a.game_end(1) == 0:
                            if i != l[len(l)-1]:
                                dis.blit(image_bg,(i[0]*60,i[1]*60)) 
                    a.b[a2][a1] = 0
                    l.append([a1,a2])
                    dis.blit(image_wn,(a1*60,a2*60))
                    a.u = [a1,a2]
                    a.u1 = a.u
                    if a.game_end(1) == 0:
                        #game_over = True
                        #print("User Wins")
                        # create a text surface object,
                        # on which text is drawn on it.
                        
                        dis.blit(image_bn,(b1*60,b2*60))
                        text = font.render('User Wins', True, green, blue)

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # set the center of the rectangular object.
                        textRect.center = (240 // 2, 240 // 2)
                        dis.blit(text,textRect)
                        break 
                    if a3 == 1:
                        a3 = 0
                        if b > 6:
                            [b1,b2] = [r.randint(1,b),r.randint(1,b)]
                            #print(b1,b2)
                            while(b1 == a1 and a2 == b2):
                                [b1,b2] = [r.randint(1,b),r.randint(1,b)]
                        else:
                            if algo == 2:
                                (m1, b1, b2) = a.first_move(-2,2)
                            if algo == 1:
                                (m1, b1, b2) = a.first_move_w()
                            if b == 4 and algo == 3:
                                [b1, b2] = a.predict_fm(a1,a2,n1)
                            if b != 4 and algo == 3:
                                text = font.render('Invalid Entry', True, green, blue)

                                # create a rectangular object for the
                                # text surface object
                                textRect = text.get_rect()

                                # set the center of the rectangular object.
                                textRect.center = (240 // 2, 240 // 2)
                                dis.blit(text,textRect)
                                break            
                    else:
                        if algo == 2:
                            (m1, b1, b2) = a.max(-2, 2)
                        if algo == 1:
                            (m1, b1, b2) = a.max_w()
                        if b == 4 and algo == 3:
                            [b1, b2] = a.predict(a1,a2,n1)
                    a.b[b2][b1] = 1
                    n1 += 1
                    l.append([b1,b2])
                    data.append([a1,a2,b1,b2,n])
                    n += 1
                    dis.blit(image_bn,(b1*60,b2*60))
                    a.c = [b1,b2]
                    if a.game_end(0) == 1:
                        #game_over = True
                        #print("Computer Wins")
                        # create a text surface object,
                        # on which text is drawn on it.
                        text = font.render('Computer Wins', True, green, blue)

                        # create a rectangular object for the
                        # text surface object
                        textRect = text.get_rect()

                        # set the center of the rectangular object.
                        textRect.center = (240 // 2, 240 // 2)
                        dis.blit(text,textRect)

                        break

                    #a.display()
                    pygame.display.update() 

            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode  
            #a1 = int(input("Enter x coordinate of your move User : "))
            #a2 = int(input("Enter y coordinate of your move User : "))
            if event.key == pygame.K_BACKSPACE and active == True:
                if len(user_text) == 1 or len(user_text) == 2:
                    user_text = ''
                else:
                    user_text = user_text[:len(user_text)-2]
            
            


    
    if active:
        color = color_active
    else:
        color = color_passive
    #print(data)    
    # draw rectangle and argument passed which should
    # be on dis
    pygame.draw.rect(dis, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    dis.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)
      
    # display.flip() will update only a portion of the
    # dis to updated, not full area
    pygame.display.flip()
      
  
    pygame.display.update() 

