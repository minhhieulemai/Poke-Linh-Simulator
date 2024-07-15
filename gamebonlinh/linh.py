import random
import pygame
import time
pygame.init()
from PIL import Image
from pygame import mixer

enenum=3
losecount=5
mixer.music.load('to-the-death-159171.mp3')
mixer.music.play(-1)
pspeed=1.5
bptp=time.time()-10

def resize(pic, name,base_width):
  img = Image.open(pic)
  wpercent = (base_width / float(img.size[0]))
  hsize = int((float(img.size[1]) * float(wpercent)))
  img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
  img.save(name)
for i in range (1,16):
 resize('linh'+str(i)+'.jpg','linh'+str(i)+'resize.jpg',120)
resize('chou.jpg','chouresize.jpg',120)
#create a window
screen = pygame.display.set_mode((1500,800))
pygame.image.load('wire.jpg')
resize('wire.jpg','wiresize.jpg',1500)
background=pygame.image.load('wiresize.jpg')
playerimage = pygame.image.load('chouresize.jpg')
px=650
py=650
enemies=['linh'+str(i)+'resize.jpg'for i in range(1,16)]
norpoke=pygame.image.load('poke (3).png')
bigpoke=pygame.image.load('poke.png')

def bullet(cor,by,type):
    screen.blit(type,(cor,by))
fire=False
def eref():
  global eim
  global ex
  global ey
  global ed
  global espeed
  global enehealth
  global enestatedead
  ex = [random.randint(0, 1400) for i in range(enenum)]
  ey = [random.randint(0, 100) for i in range(enenum)]
  eim= [pygame.image.load(random.choice(enemies)) for i in range(enenum)]
  ed = [random.choice([1,-1]) for i in range(enenum)]
  espeed = [random.choice([x*0.1 + 1 for x in range(10)])for x in range(enenum)]
  enehealth = [100 for i in range(enenum)]
  enestatedead = [False for i in range(enenum)]
eref()

edc=0
def enemy(pic,x,y):
    screen.blit(pic,(x,y))

lfont=pygame.font.Font('freesansbold.ttf',120)
losenot1=lfont.render('Linh Win' ,True,(255,0,0))
losenot2=lfont.render('You Lose',True,(255,0,0))
#set score
scorep=0
sfont=pygame.font.Font('freesansbold.ttf',63)
hfont=pygame.font.Font('freesansbold.ttf',63)
def showhealth():
    health=hfont.render('Health: '+str(losecount), True,(0,255,0))
    screen.blit(health,(12,730))
def showscore():
    score =sfont.render('Score:'+str(scorep),True, (255,0,0))
    screen.blit(score,(12,12))

#cd
cdfont=pygame.font.Font('freesansbold.ttf',50)

def enemiesspawn(it):
    for a in range (it):
        i=a
        if enehealth[a]>0 and ey[i]<800:
            enemy(eim[i],ex[i],ey[i])
            ex[i]=ex[i] + ed[i] * espeed[i]
            if ex[i]<=0 or ex[i]>=1400:
                ed[i] *=-1
                if espeed[i]>=1.5:
                    ey[i]+=45
                else:
                    ey[i]+=90
        elif enehealth[a]>0 and ey[i]>=800 and enestatedead[a]==False:
            global losecount
            enestatedead[a]=True
            losecount-=1
        else:

            ex[i]=ey[i]=-500

            if enehealth[a] <=0 and enestatedead[a]==False:
                enestatedead[a] = True
                eds=mixer.Sound('lego-yoda-death-sound-effect.mp3')
                eds.play()
                global scorep
                scorep += 1



bx=[]
by=[620]
bspeed=0.8
bpspeed=0.4
hit=[]
def shoot(int):
    for i in range(int):
        hit.append(False)
        if hit[i]==False and by[i]>= -50:
            for a in range(enenum):
                if bx[i]+18>= ex[a]  and bx[i] +18<= ex[a]+100 :
                    if by[i]>= ey[a]  and by[i] <= ey[a]+120:
                        hit[i]=True
                        enehealth[a] -=25
                        if enehealth[a]!=0:
                            pokes=mixer.Sound('anime-ahh.mp3')
                            pokes.play()


                    else:
                        by.append(620)
                        bullet(bx[i], by[i], norpoke)
                        if by[i]==620:
                            firesound=mixer.Sound('pew-pew-lame-sound-effect.mp3')
                            firesound.play()
                        by[i] -= bspeed
                else:
                    by.append(620)
                    bullet(bx[i], by[i], norpoke)
                    if by[i] == 620:
                        firesound = mixer.Sound('pew-pew-lame-sound-effect.mp3')
                        firesound.play()
                    by[i] -= bspeed

        else:
            pass

bpcomming = False
bpx = 0
bpy = 0
bpready=True
cd=0
def cdready():
    if bpready == False:
        cdown=cdfont.render('Big Poke Cooldown:'+str(round(cd)),True,(255,0,0))
        screen.blit(cdown,(950,12))
    else:
        bpread=cdfont.render('Big Poke Ready', True,(0,255,0))
        screen.blit(bpread,(1115,12))

def shootbig():
    global bpcomming
    global bpy
    if bpy <= -100:
        bpcomming = False
    if bpcomming==True:
        bullet(bpx, bpy, bigpoke)
    if bpy == 620:
        bfiresound = mixer.Sound('atomic_bomb-sound_explorer-897730679-1 (mp3cut.net).mp3')
        bfiresound.play()
    bpy -= bpspeed
    hitboxX=(bpx+34,bpx+60,bpx+4)
    hitboxY=(bpy+32,bpy+64,bpy)
    for a in range(enenum):
        for bpxx in hitboxX:
            for bpyy in hitboxY:
                if bpxx>= ex[a]  and bpxx +34<= ex[a]+100 :
                    if bpyy>= ey[a]  and bpyy <= ey[a]+120:
                        enehealth[a] -=1
                        if enehealth[a]!=0:
                            pokes=mixer.Sound('anime-ahh.mp3')
                            pokes.play()

numbbu=0
lsp=False
def player(x,y):
    screen.blit(playerimage,(x,y))

pygame.display.set_caption('Poke Linh Simulator')
icon=pygame.image.load('linh1.jpg')
pygame.display.set_icon(icon)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                bx.append(px+25)
                numbbu+=1
            if event.key == pygame.K_DOWN and time.time()-bptp>=10:
                bpx=px+25
                bpy=620
                bpcomming=True
                bptp=time.time()
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    if losecount >0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            px -= pspeed
        if keys[pygame.K_RIGHT]:
            px += pspeed
        if px <= 0:
            px=0
        if px>=1400:
            px=1400


        player(px,py)
        enemiesspawn(enenum)
        shoot(numbbu)
        shootbig()
        showscore()
        cdready()
        showhealth()
        cd=10-time.time()+bptp
        if cd<=0:
            bpready=True
        else:
            bpready=False
        if False in enestatedead:
            pass
        else:
            enenum += 2
            pspeed +=0.1
            eref()
        pygame.display.update()
    else:
        if lsp==False:
            losound=mixer.Sound('downer_noise.mp3')
            losound.play()
            lsp=True
        screen.blit(losenot1,(490,280))
        screen.blit(losenot2,(485,430))
        lscore=lfont.render('Your Score:'+str(scorep),True, (0,0,255))
        screen.blit(lscore,(375,20))
        pygame.display.update()


