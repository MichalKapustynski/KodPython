import math
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

kolor1 = (1,0,0)
kolor2 = (0,1,0)
kolor3 = (0,0,1)
kolor4 = (1,1,1)
punkty = [
    [-7,2,-6,1],
    [-7,-2,-6,1],
    [-3, 2, -6,1],
    [-3,-2, -6,1],
    [-7, 2, -2,1],
    [-7, -2, -2,1],
    [-3, 2, -2,1],
    [-3, -2, -2,1],
    [7, 2, -6,1],
    [7, -2, -6,1],
    [3, 2, -6,1],
    [3, -2, -6,1],
    [7, 2, -2,1],
    [7, -2, -2,1],
    [3, 2, -2,1],
    [3, -2, -2,1],

    [-7, 2, -12, 1],
    [-7, -2, -12, 1],
    [-3, 2, -12, 1],
    [-3, -2, -12, 1],
    [-7, 2, -8, 1],
    [-7, -2, -8, 1],
    [-3, 2, -8, 1],
    [-3, -2, -8, 1],
    [7, 2, -12, 1],
    [7, -2, -12, 1],
    [3, 2, -12, 1],
    [3, -2, -12, 1],
    [7, 2, -8, 1],
    [7, -2, -8, 1],
    [3, 2, -8, 1],
    [3, -2, -8, 1]

    ]

sciany= [
    (0,2,3,1),
    (2,6,7,3),
    (1,3,7,5),
    (4,0,1,5),
    (4,6,2,0),
    (4,6,7,5),

    (8,10,11,9),
    (10,14,15,11),
    (9,11,15,13),
    (12,8,9,13),
    (12,14,10,8),
    (12,14,15,13),

    (16,18,19,17),
    (18,22,23,19),
    (17,19,23,21),
    (20,16,17,21),
    (20,22,18,16),
    (20,22,23,21),

    (24,26,27,25),
    (26,30,31,27),
    (25,27,31,29),
    (28,24,25,29),
    (28,30,26,24),
    (28,30,31,29)
    ]

def Rysuj():
    scianyOdleglosc = []
    i = 0
    for sciana in sciany:
        wektor1 = (punkty[sciana[0]])
        a = wektor1[2]
        wektor2 = (punkty[sciana[1]])
        b = wektor2[2]
        odleglosc = (a + b) / 2
        scianyOdleglosc.append([odleglosc, i])
        i += 1
    posortowane = sorted(scianyOdleglosc)
    glBegin(GL_QUADS)
    for sciana in posortowane:
        idSciany = sciana[1]


        for punkt in sciany[idSciany]:
             if(punkt<=7):
                glColor3fv(kolor1)
                glVertex4fv(punkty[punkt])
             elif(punkt>7 and punkt<=15):
                glColor3fv(kolor2)
                glVertex4fv(punkty[punkt])
             elif (punkt > 14 and punkt <=23):
                glColor3fv(kolor3)
                glVertex4fv(punkty[punkt])
             elif (punkt > 23 and punkt <= 31):
                glColor3fv(kolor4)
                glVertex4fv(punkty[punkt])
    glEnd()

def Przod():
    m=[1,0,0,0,0,1,0,0,0,0,1,1,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Tyl():
    m=[1,0,0,0,0,1,0,0,0,0,1,-1,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Prawo():
    m=[1,0,0,-1,0,1,0,0,0,0,1,0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Lewo():
    m=[1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Dol():
    m=[1,0,0,0,0,1,0,1,0,0,1,0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Gora():
    m=[1,0,0,0,0,1,0,-1,0,0,1,0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Obrot_x1():
    m=[1,0,0,0,0,math.cos(0.087),-(math.sin(0.087)),0,0,math.sin(0.087),math.cos(0.087),0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Obrot_x2():
    m=[1,0,0,0,0,math.cos(-0.087),-(math.sin(-0.087)),0,0,math.sin(-0.087),math.cos(-0.087),0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Obrot_y1():
    m=[math.cos(0.087),0,math.sin(0.087),0,0,1,0,0,-(math.sin(0.087)),0,math.cos(0.087),0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Obrot_y2():
    m=[math.cos(-0.087),0,math.sin(-0.087),0,0,1,0,0,-(math.sin(-0.087)),0,math.cos(-0.087),0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Obrot_z1():
    m=[math.cos(0.087),-(math.sin(0.087)),0,0,math.sin(0.087),math.cos(0.087),0,0,0,0,1,0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Obrot_z2():
    m=[math.cos(-0.087),-(math.sin(-0.087)),0,0,math.sin(-0.087),math.cos(-0.087),0,0,0,0,1,0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Obrot_z2():
    m=[math.cos(-0.087),-(math.sin(-0.087)),0,0,math.sin(-0.087),math.cos(-0.087),0,0,0,0,1,0,0,0,0,1]
    i=0
    for punkt in punkty:
        a=punkt[0]*m[0]+punkt[1]*m[1]+punkt[2]*m[2]+punkt[3]*m[3]
        b = punkt[0]*m[4]+punkt[1]*m[5]+punkt[2]*m[6]+punkt[3]*m[7]
        c = punkt[0]*m[8]+punkt[1]*m[9]+punkt[2]*m[10]+punkt[3]*m[11]
        d = punkt[0]*m[12]+punkt[1]*m[13]+punkt[2]*m[14]+punkt[3]*m[15]
        punkty[i]=[a,b,c,d]
        i=i+1

def Zoom1():
    n = 1.3
    m=[1,0,0,7,0,1,0,-2,0,0,1,2,0,0,0,1]
    m1 = [-1, 0, 0, -7, 0, -1, 0, 2, 0, 0, -1, -2, 0, 0, 0, -1]
    i=0
    s = [n, 0, 0, 0, 0, n, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    i = 0

    for punkt in punkty:
        a = punkt[0] * s[0] + punkt[1] * s[1] + punkt[2] * s[2] + punkt[3] * s[3]
        b = punkt[0] * s[4] + punkt[1] * s[5] + punkt[2] * s[6] + punkt[3] * s[7]
        c = punkt[0] * s[8] + punkt[1] * s[9] + punkt[2] * s[10] + punkt[3] * s[11]
        d = punkt[0] * s[12] + punkt[1] * s[13] + punkt[2] * s[14] + punkt[3] * s[15]
        punkty[i] = [a, b, c, d]
        i = i + 1


def Zoom2():
    n = 0.7
    m=[1,0,0,7,0,1,0,-2,0,0,1,2,0,0,0,1]
    m1=[-1,0,0,-7,0,-1,0,2,0,0,-1,-2,0,0,0,-1]
    s = [n, 0, 0, 0, 0, n, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]
    i=0

    for punkt in punkty:
        a = punkt[0] * s[0] + punkt[1] * s[1] + punkt[2] * s[2] + punkt[3] * s[3]
        b = punkt[0] * s[4] + punkt[1] * s[5] + punkt[2] * s[6] + punkt[3] * s[7]
        c = punkt[0] * s[8] + punkt[1] * s[9] + punkt[2] * s[10] + punkt[3] * s[11]
        d = punkt[0] * s[12] + punkt[1] * s[13] + punkt[2] * s[14] + punkt[3] * s[15]
        punkty[i] = [a, b, c, d]
        i = i + 1



def main():

    wymiary = (1000,500)
    pygame.display.set_mode(wymiary, DOUBLEBUF|OPENGL)

    gluPerspective(50, (wymiary[0]/wymiary[1]), 0.01, 100.0)




    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    Przod()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    Tyl()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_d:
                    Prawo()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    Lewo()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    Gora()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    Dol()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Obrot_x1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_2:
                    Obrot_x2()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    Obrot_y1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Obrot_y2()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    Obrot_z1()
            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_e:
                     Obrot_z2()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    Zoom1()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_9:
                    Zoom2()

        glClear(GL_COLOR_BUFFER_BIT)
        Rysuj()
        pygame.display.flip()
        pygame.time.wait(10)


main()