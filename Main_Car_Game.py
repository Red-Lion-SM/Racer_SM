#!/usr/bin/env python3
import pygame
from pygame import mixer
import time
import sys
import random
pygame.init()
pygame.display.set_caption('Racer_SM')

# Colors ---------------------
gray=(119,118,110)
white=(255,255,255)
black=(0,0,0)
red=(200,0,0)
green=(0,200,0)
blue=(0,0,255)
bright_red=(255,0,0)
light_blue=(102, 255, 255)
yo=[]
clock=pygame.time.Clock()
scores=[0]
user_name=[]
mixer.music.load('back_music.wav')
mixer.music.play(-1)

# Window Size ----------------
height=702
width=1375
display_=pygame.display.set_mode((width,height))

def load(name,x_pos,y_pos):
    img = pygame.image.load(name)
    display_.blit(img,(x_pos, y_pos))
    pygame.display.update()

def message(mess, colour, size, x, y):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(mess, True, colour)
    display_.blit(screen_text, (x, y))
    pygame.display.update()

car_name=""

def funn(x,val):
    global car_name
    car_name=x
    play_game(x)

def print_user(s,val):
    print("YES")
    message(s,white,25,val+450,100)

def button1(x,y,w,h,mess,mess_color,actc,noc,size,tx,ty,func,car_type,val):
    mouse = pygame.mouse.get_pos()
    click=  pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display_,actc,[x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
        if click==(1,0,0):
            func(car_type,val)
    else:
        pygame.draw.rect(display_, noc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
    pygame.display.update()

def button(x,y,w,h,mess,mess_color,actc,noc,size,tx,ty,func):
    mouse = pygame.mouse.get_pos()
    click=  pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display_,actc,[x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
        if click==(1,0,0):
            func()
    else:
        pygame.draw.rect(display_, noc, [x, y, w, h])
        message(mess, mess_color, size, tx, ty)
        pygame.display.update()
    pygame.display.update()

def crash1(x):
    if 70>x  or x>500:
        font = pygame.font.SysFont(None, 100)
        screen_text = font.render("Came Out of your zone", True,white)
        display_.blit(screen_text, (250, 280))
        pygame.display.update()
        mixer.music.load('explosion.wav')
        mixer.music.play(1)
        time.sleep(2)
        welcome_page()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def crash2(x):
    if 700>x  or x>1300:
        font = pygame.font.SysFont(None, 100)
        screen_text = font.render("Came Out of your zone", True,white)
        display_.blit(screen_text, (250, 280))
        pygame.display.update()
        mixer.music.load('explosion.wav')
        mixer.music.play(1)
        time.sleep(2)
        welcome_page()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def crashy(x):
    if 10>x  or x+5>702:
        font = pygame.font.SysFont(None, 100)
        screen_text = font.render('Game Over! Out of the road', True,white)
        display_.blit(screen_text, (250, 280))
        pygame.display.update()
        mixer.music.load('explosion.wav')
        mixer.music.play(1)
        time.sleep(2)
        welcome_page()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()

def car_crash(x,y,y_en,x_en,fl):
    if ((x<x_en<x+130 and y<y_en<y+130) or (x<x_en+100<x+130 and y<y_en+100<y+130)):
        if fl==0:
            message(' Player 1 Won!!! ', white, 100, 450, 280)
        else:
            message(' Player 2 Won!!! ', white, 100, 450, 280)
        mixer.music.load('explosion.wav')
        mixer.music.play(1)
        time.sleep(2)
        mixer.music.load('back_music.wav')
        mixer.music.play(-1)
        welcome_page()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.update()

def score(count):
    scores.sort(reverse=True)
    x=scores[0]
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('Score :' + str(count), True, white)
    display_.blit(screen_text, (85, 0))
    screen_text = font.render('High Score :' + str(x), True, white)
    display_.blit(screen_text, (85, 45))
    if(count<=x):
        screen_text = font.render('Score Needed :' + str(abs(count-x)), True, white)
        display_.blit(screen_text, (85, 90))
    scores.append(count)
    pygame.display.update()

def score1(count):
    scores.sort(reverse=True)
    x=scores[0]
    font = pygame.font.SysFont(None, 30)
    screen_text = font.render('Score :' + str(count), True, white)
    display_.blit(screen_text, (785, 0))
    screen_text = font.render('High Score :' + str(x), True, white)
    display_.blit(screen_text, (785, 45))
    if(count<=x):
        screen_text = font.render('Score Needed :' + str(abs(count-x)), True, white)
        display_.blit(screen_text, (785, 90))
    scores.append(count)
    pygame.display.update()

def other_car(y_en,othercar):
    enmy1=pygame.image.load(othercar)
    enmy=pygame.transform.scale(enmy1,(150,150))
    global x_en
    if y_en==0:
      x_en=random.randrange(50,455)
      yo.clear()
      yo.append(x_en)
    else:
      x_en=yo[0]
    display_.blit(enmy,(x_en,y_en))
    pygame.display.update()

def other_car1(y1_en,othercar):
    enmy1 = pygame.image.load(othercar)
    enmy = pygame.transform.scale(enmy1, (150, 150))
    global x1_en
    if y1_en == 0:
        x1_en = random.randrange(745, width - 200)
        yo.clear()
        yo.append(x1_en)
    else:
        x1_en = yo[0]
    display_.blit(enmy, (x1_en, y1_en))
    pygame.display.update()

def play_game(x):
    carimg = pygame.image.load(x)
    carimg1 = pygame.image.load('wide_road.jpg')
    car1 = pygame.transform.scale(carimg, (150, 150))
    car2 = pygame.transform.scale(carimg, (150, 150))
    backk = pygame.transform.scale(carimg1,(1375,1000))
    loop=False
    x = 300
    x1=750
    y = 500
    y1=500
    x_change = 0
    y_change = 0
    x1_change = 0
    y1_change = 0
    global game_over
    game_over = False
    count = 0
    count1 = 0
    y_en = 0
    y1_en = 0
    f=15
    fl=0
    road=0
    othercar = random.choice(['scorpio.png', 'elite.png', 'harrier.png'])
    while game_over == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x1_change = -f
                elif event.key == pygame.K_d:
                    x1_change = +f
                elif event.key == pygame.K_s:
                    y1_change = +f
                elif event.key == pygame.K_w:
                    y1_change = -f
                if event.key == pygame.K_LEFT:
                    x_change = -f
                elif event.key == pygame.K_RIGHT:
                    x_change = +f
                elif event.key == pygame.K_UP:
                    y_change = -f
                elif event.key == pygame.K_DOWN:
                    y_change = +f
            if event.type == pygame.KEYUP:
                x1_change = 0
                y1_change = 0
                x_change = 0
                y_change = 0
        x += x1_change
        y += y1_change
        x1+= x_change
        y1+=y_change
        # x1_change=0
        # y1_change=0
        # x_change=0
        # y_change=0
        crashy(y)
        crashy(y1)
        road+=40
        display_.blit(backk, (0, 0))
        if(road>=50):
            road=0
        display_.blit(backk, (0, road))
        display_.blit(car1, (x, y))
        display_.blit(car2, (x1, y1))
        if y_en > 600 and fl==1:
            y_en = 0
            othercar=random.choice(['scorpio.png','elite.png',
                                    'harrier.png'])
            fl=0
            count += 1
        if y1_en > 600 and fl==0:
            y1_en = 0
            othercar = random.choice(['scorpio.png', 'elite.png',
                                      'harrier.png'])
            fl=1
            count1 += 1
        if fl==1:
            other_car(y_en,othercar)
        else:
            other_car1(y1_en,othercar)
        if fl==1:
            y_en += 25
            y1_en=0
        else:
            y1_en+=25
            y_en=0
        if fl==1:
            crash1(x)
        else:
            crash2(x1)
        if fl==1:
            car_crash(x, y, y_en, x_en,fl)
        else:
            car_crash(x1, y1, y1_en, x1_en,fl)
        score(count)
        score1(count1)
        clock.tick(30)
        pygame.display.update()

def choose_car():
    carimg = pygame.image.load('chose_car.jpg')
    car1 = pygame.transform.scale(carimg, (1375,702))
    display_.blit(car1, (0, 0))
    message("Choose Your Car", black, 60, (width / 2 - 470),30)
    message("Type Your UserName", black, 60, (width / 2 + 140),30)
    load('baleno.png', 80, 100)
    load('creta.png', 100, 400)
    load('i10.png', 500, 100)
    load('special.png', 530, 400)
    xcor=(width / 2 + 140)
    ycor=70
    val=0
    for _ in range(1,27):
        if(_%4==1):
            xcor+=80
            ycor=740
        button1(xcor, ycor, 40, 40, 'A', white, black, black,25,110,275,funn,"A",val)
        val+=40

    loopp=False
    while loopp==False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loopp = True
        button1(105, 270, 123, 30, 'Baleno Alpha', white, blue,black,25,110,275,funn,"baleno.png",0)
        button1(139, 540, 70, 30, 'Creta', white, blue,black,25,146,543,funn,"creta.png",0)
        button1(516, 270, 120, 30, 'Grand i10', white, blue,black,25,535,275,funn,"i10.png",0)
        button1(505, 540, 157, 30, 'Special Car', white, blue,black,25,525,543,funn,"special.png",0)
        pygame.display.update()
    pygame.display.update()

def welcome_page():
    carimg = pygame.image.load('final_welcome.jpg')
    car1 = pygame.transform.scale(carimg, (1375,702))
    display_.blit(car1, (0, 0))
    high=0
    loopp=False
    s="--Choose Your Car--"
    f="|"
    for _ in range(88):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loopp = True
        button(320, 665, 450, 25, f, white,black,black, 25, 322, 668, choose_car)
        pygame.display.update()
        time.sleep(0.03)
        f+="|"
    pygame.display.update()
    while loopp==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                loopp=True
        button(320, 665, 180, 25, '--Choose Your Car--', white,red,black,25,327,670,choose_car)
        pygame.display.update()
    pygame.display.update()

def most_welcome():
    carimg = pygame.image.load('final_welcome.jpg')
    car1 = pygame.transform.scale(carimg, (1375, 702))
    display_.blit(car1, (0, 0))
    pygame.display.update()
    welcome_page()

most_welcome()
play_game()