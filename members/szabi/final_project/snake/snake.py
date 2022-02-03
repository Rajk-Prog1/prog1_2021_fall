import pygame
import time
import random
import sys
import numpy
import math

pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
nokia_green=(128, 228, 17)
 
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')
 
clock = pygame.time.Clock()
 
snake_block = 15
#snake_speed = 8.5
 
font_style = pygame.font.Font("3x5.ttf", 20)
score_font = pygame.font.Font("3x5.ttf", 30)
menu_font = pygame.font.Font("3x5.ttf", 30)

stripeimg=pygame.image.load('stripe.png')

headimg=pygame.image.load('head.png')
headimg_r = pygame.transform.flip(headimg, True, False)
headimg_u1 = pygame.transform.rotate(headimg, 90)
headimg_u = pygame.transform.flip(headimg_u1, False, True)
headimg_d1 = pygame.transform.rotate(headimg, 270)
headimg_d = pygame.transform.flip(headimg_d1, True, True)

tailimg = pygame.image.load('tail.png')
tailimg2 = pygame.transform.rotate(tailimg, 180)
tail2=pygame.image.load('tail2.png')
foodimg=pygame.image.load('food.png')
plusimg=pygame.image.load('plus.png')
direction=1
enter=1

def player_score(score):
    value = score_font.render(str(score), True, black)
    dis.blit(value, [20, 20])

def timer(seconds, timerx, timery):
    countdown=round(seconds)%5
    countdown=abs(countdown-5)
    value = score_font.render(str(countdown), True, black)
    dis.blit(value, [timerx+10, timery])
    dis.blit(plusimg, [timerx-30, timery+8])
    

def print_snake(snake_list):
    if len(snake_list)>2:
        z=0
        for x in snake_list[-1::-2]:
            if x[0] == snake_list[z][0] and x!=snake_list[0]:
                pygame.draw.rect(dis, black, [x[0], x[1], 10, 10])
                pygame.draw.rect(dis, black, [x[0], x[1]-5, 10, 10])
                pygame.draw.rect(dis, black, [x[0], x[1]+5, 10, 10])
            if x[1] == snake_list[z][1] and x!=snake_list[0]:
                pygame.draw.rect(dis, black, [x[0], x[1], 10, 10])
                pygame.draw.rect(dis, black, [x[0]-5, x[1], 10, 10])
                pygame.draw.rect(dis, black, [x[0]+5, x[1], 10, 10])
            z=z-2
        for y in snake_list[-2::-2]:
            dis.blit(stripeimg, [y[0],y[1]])
        if snake_list[0][1]==snake_list[1][1]:
            pygame.draw.rect(dis, nokia_green, [snake_list[0][0], snake_list[0][1], 10, 10])
            dis.blit(tailimg2, [snake_list[0][0], snake_list[0][1]])
        if snake_list[0][0]==snake_list[1][0]:
            pygame.draw.rect(dis, nokia_green, [snake_list[0][0], snake_list[0][1], 10, 10])
            dis.blit(tail2, [snake_list[0][0], snake_list[0][1]])
    if direction==1:
        dis.blit(headimg, [snake_list[-1][0]-10, snake_list[-1][1]-5])
    if direction==2:
        dis.blit(headimg_r, [snake_list[-1][0]-10, snake_list[-1][1]-5])
    if direction==3:
        dis.blit(headimg_u, [snake_list[-1][0]-5, snake_list[-1][1]-5])
    if direction==4:
        dis.blit(headimg_d, [snake_list[-1][0]-5, snake_list[-1][1]-5])
        
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def game():
    game_over = False
    game_close = False
 
    x1 = 600 / 2
    y1 = 390 / 2
 
    x1_change = 0
    y1_change = 0
 
    start_ticks=pygame.time.get_ticks()
    snake_list = [[x1,y1]]
    Length_of_snake = 1
    snake_speed=7.5
 
    foodx = random.randrange(0, 555/15)*15 + 30
    foody = random.randrange(0, 300/15)*15 + 75
    food2x = 1000
    food2y = 1000
    timerx = 1000
    timery = 1000
    seconds=1
    
    while not game_over:
        if game_close == True:
            dis.fill(nokia_green)
            inpt()
            record=[]
            record.append(word)
            record.append(",")
            record.append(str(Length_of_snake-1))
            record.append(",")
            with open ('leaderboards.txt', 'a') as f:
                for x in record:
                    f.write(x)
                    
        while game_close == True:
            dis.fill(nokia_green)
            message("Game over! Press P-Play Again or Q-Quit", black)
            records=str(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                global direction
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                    direction=1
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                    direction=2
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                    direction=3
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                    direction=4
 
        if x1 >= 582 or x1 < 23 or y1 >= 372 or y1 < 68:
            game_close = True
            
        x1 += x1_change
        y1 += y1_change
        dis.fill(nokia_green)
        pygame.draw.rect(dis, black, [20, 65, 565, 310])
        pygame.draw.rect(dis, nokia_green, [23, 68, 559, 304])
        dis.blit(foodimg, [foodx-5,foody-5])
        dis.blit(plusimg, [food2x-5,food2y-5])
        timer(seconds, timerx, timery)
        pygame.draw.line(dis, black, [20, 55], [583, 55], width=3)
        snake_front = []
        snake_front.append(x1)
        snake_front.append(y1)
        snake_list.append(snake_front)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]
            
        for x in snake_list[:-1]:
            if x == snake_front:
                game_close = True
        seconds=round((pygame.time.get_ticks()-start_ticks)/1000,1)+1
        print_snake(snake_list)
        player_score(Length_of_snake - 1)
        pygame.display.update()
        
        if seconds%10 == 0:
            food2x = random.randrange(0, 555/15)*15 + 30
            food2y = random.randrange(0, 300/15)*15 + 75
            timerx = 550
            timery = 20
        if (seconds-5)%10 == 0:
            food2x = 1000
            food2y = 1000
            timerx = 1000
            timery = 1000
        if x1 == foodx and y1 == foody:
            foodx = random.randrange(0, 555/15)*15 + 30
            foody = random.randrange(0, 300/15)*15 + 75
            Length_of_snake += 1
            snake_speed += 1
        if x1 == food2x and y1 ==food2y:
            food2x = 1000
            food2y = 1000
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    sys.exit()
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    surface.blit(textobj, textrect)
    
click=False

def main_menu():
    while True:
        dis.fill(nokia_green)
        draw_text('Main menu', menu_font, black, dis, 230, 20)
        
        mx, my = pygame.mouse.get_pos()
        
        button_1 = pygame.Rect(dis_width/3, dis_height/4, dis_width/3, dis_height/8)
        button_2 = pygame.Rect(dis_width/3, dis_height/2, dis_width/3, dis_height/8)
        button_1_inner = pygame.Rect(dis_width/3+1, dis_height/4+1, dis_width/3-2, dis_height/8-2)
        button_2_inner = pygame.Rect(dis_width/3+1, dis_height/2+1, dis_width/3-2, dis_height/8-2)
        if button_1.collidepoint((mx,my)):
            if click:
                game()
        if button_2.collidepoint((mx,my)):
            if click:
                leaderboard()
        pygame.draw.rect(dis, black, button_1)
        pygame.draw.rect(dis, white, button_1_inner)
        draw_text('Play game', font_style, black, dis, 252, 114)
        pygame.draw.rect(dis, black, button_2)
        pygame.draw.rect(dis, white, button_2_inner)
        draw_text('Leaderboards', font_style, black, dis, 233, 214)
        click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()
        clock.tick(60)
        
def inpt():
    global word
    word=""
    draw_text("Please enter your name then press enter: ", font_style, black, dis, 50,150)
    pygame.display.update()
    done = True
    name_pos_x=460
    name_pos_y=150
    text_pos_x=50
    text_pos_y=150
    while done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                mods = pygame.key.get_mods()
                if event.key == pygame.K_a:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="A"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="a"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_b:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="B"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="b"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_c:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="C"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="c"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_d:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="D"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="d"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_e:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="E"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="e"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_f:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="F"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="f"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_g:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="G"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="g"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_h:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="H"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="h"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_i:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="I"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="i"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_j:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="J"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="j"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_k:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="K"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="k"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_l:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="L"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="l"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_m:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="M"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="m"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_n:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="N"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="n"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_o:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="O"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="o"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_p:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="P"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="p"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_q:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="Q"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="q"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_r:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="R"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="r"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_s:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="S"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="s"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_t:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="T"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="t"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_u:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="U"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="u"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_v:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="V"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="v"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_w:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="W"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="w"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_x:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="X"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="x"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_y:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="Y"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="y"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_z:
                    if mods & pygame.KMOD_LSHIFT or mods & pygame.KMOD_CAPS:
                        word+="Z"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                    else:
                        word+="z"
                        dis.fill(nokia_green)
                        draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                        draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                        pygame.display.update()
                if event.key == pygame.K_BACKSPACE:
                    word=word[:-1]
                    dis.fill(nokia_green)
                    draw_text("Please enter your name then press enter: ", font_style, black, dis, text_pos_x, text_pos_y)
                    draw_text(word, font_style, black, dis, name_pos_x, name_pos_y)
                    pygame.display.update()
                if event.key == pygame.K_RETURN:
                    done=False
def leaderboard():
    while True:
        dis.fill(nokia_green)
        draw_text('Leaderboards - Top 5', font_style, black, dis, dis_width/3, dis_height/20)
        
        mx, my = pygame.mouse.get_pos()
        
        button_back = pygame.Rect(dis_width/3, dis_height/1.2, dis_width/3, dis_height/8)
        button_back_inner = pygame.Rect(dis_width/3+1, dis_height/1.2+1, dis_width/3-2, dis_height/8-2)
        if button_back.collidepoint((mx,my)):
            if click:
                main_menu()
        pygame.draw.rect(dis, black, button_back)
        pygame.draw.rect(dis, white, button_back_inner)
        draw_text('Back', font_style, black, dis, dis_width/2.1428, dis_height/1.147)
        with open ('leaderboards.txt', 'r') as f:
            scores=f.read().split(',')
            scores_num=[]
            scores_names=[]
            for i in scores[1::2]:
                scores_num.append(int(i))
            for i in scores[0::2]:
                scores_names.append(i)
            scores_names = numpy.array(scores_names)
            scores_num = numpy.array(scores_num)
            inds = scores_num.argsort()
            sortedPeople = scores_names[inds]
            rect_backgr =pygame.Rect(dis_width/3, 70, dis_width/3, dis_height/8*5)
            rect_first_inner = pygame.Rect(dis_width/3+1, 70+1, dis_width/3-2, dis_height/8-2)
            rect_second_inner = pygame.Rect(dis_width/3+1, 120+1, dis_width/3-2, dis_height/8-2)
            rect_third_inner = pygame.Rect(dis_width/3+1, 170+1, dis_width/3-2, dis_height/8-2)
            rect_fourth_inner = pygame.Rect(dis_width/3+1, 220+1, dis_width/3-2, dis_height/8-2)
            rect_fifth_inner = pygame.Rect(dis_width/3+1, 270+1, dis_width/3-2, dis_height/8-2)
            pygame.draw.rect(dis, black, rect_backgr)
            pygame.draw.rect(dis, white, rect_first_inner)
            pygame.draw.rect(dis, white, rect_second_inner)
            pygame.draw.rect(dis, white, rect_third_inner)
            pygame.draw.rect(dis, white, rect_fourth_inner)
            pygame.draw.rect(dis, white, rect_fifth_inner)
            draw_text(str(sortedPeople[-1]), font_style, black, dis, 210, 85)
            draw_text(str(sorted(scores_num)[-1]), font_style, black, dis, 370, 85)
            draw_text(str(sortedPeople[-2]), font_style, black, dis, 210, 135)
            draw_text(str(sorted(scores_num)[-2]), font_style, black, dis, 370, 135)
            draw_text(str(sortedPeople[-3]), font_style, black, dis, 210, 185)
            draw_text(str(sorted(scores_num)[-3]), font_style, black, dis, 370, 185)
            draw_text(str(sortedPeople[-4]), font_style, black, dis, 210, 235)
            draw_text(str(sorted(scores_num)[-4]), font_style, black, dis, 370, 235)
            draw_text(str(sortedPeople[-5]), font_style, black, dis, 210, 285)
            draw_text(str(sorted(scores_num)[-5]), font_style, black, dis, 370, 285)
            click=False
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1:
                    click=True
        pygame.display.update()
        clock.tick(60)
main_menu()