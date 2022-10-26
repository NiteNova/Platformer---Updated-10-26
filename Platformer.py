import pygame
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#load images
bg_image = pygame.image.load("space.png")
moon_image = pygame.image.load("Moon.png")
moon_image = pygame.transform.scale(moon_image, (300, 300))

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform
health = 100

#enemy variables
#expos = 200
#eypos = 630
#timer = 0
enemy1=[200, 630, 0]
enemy2=[400, 700, 40]
enemy3=[290, 530, 25]


#------------------------------------------Function Definition-------------------------
def enemyMove(enemyInfo):
    #print(enemyInfo)
    enemyInfo[2] +=1
    if enemyInfo[2] <= 40:
        enemyInfo[0]+=1
    elif enemyInfo[2] <= 80:
        enemyInfo[0]-=1
    else:
         enemyInfo[2] = 0 #reset timer
#---------------------------------------------------------------------------------------


def enemyCollide(enemyInfo, playerX, playerY):
    if playerX+20>enemyInfo[0]: #right side of player
        if playerX < enemyInfo[0]+20: #left side of player
            if playerY < enemyInfo[1]+20:
                if playerY+20 > enemyInfo[1]:
                    return True
    else:
        return False

#SOUND--------------------------------------------------------------------
jump = pygame.mixer.Sound('jump.ogg')#load in sound effect
music = pygame.mixer.music.load('music.ogg')#load in background music
pygame.mixer.music.play(-1)#start background music
#-------------------------------------------------------------------------

while not gameover and health > 0: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
            
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False

            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False
        

    #function call for enemy movement                           
    enemyMove(enemy1)
    enemyMove(enemy2)
    enemyMove(enemy3)
    
    #function calls for enemy collison
    if enemyCollide(enemy1, xpos, ypos) == True:
        print("Hit!")
        health -= 3
    if enemyCollide(enemy2, xpos, ypos) == True:
        print("Hit!")
        health -= 3
    if enemyCollide(enemy3, xpos, ypos) == True:
        print("Hit!")
        health -= 3
       
       
          
    #physics section--------------------------------------------------------------------
    #RIGHT MOVEMENT
    if keys[RIGHT]==True:
        vx=+3
        direction = RIGHT
    
    #LEFT MOVEMENT
    elif keys[LEFT]==True:
        vx=-3
        direction = LEFT

    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
        pygame.mixer.Sound.play(jump) #play the jump sound
    
    

    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>250 and xpos<350 and ypos+40>550 and ypos+40< 570:
        ypos = 550-40
        isOnGround = True
        vy = 0
    elif xpos>320 and xpos<420 and ypos+40>450 and ypos+40<470 :
        ypos = 450-40
        isOnGround = True
        vy = 0
    elif xpos>270 and xpos<370 and ypos+40>340 and ypos+40<360 :
        ypos = 340-40
        isOnGround = True
        vy = 0
    elif xpos>100 and xpos<200 and ypos+40>240 and ypos+40<260 :
        ypos = 240-40
        isOnGround = True
        vy = 0
    elif xpos>50 and xpos<150 and ypos+40>130 and ypos+40<150 :
        ypos = 130-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False


    
    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
    
    screen.blit(bg_image, (0,0)) #draw background image
    
    screen.blit(moon_image, (200, 350))
    
    #draw player
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    
    #draw enemy
    pygame.draw.rect(screen, (255, 255, 255), (enemy1[0], enemy1[1], 20, 40))
    pygame.draw.rect(screen, (255, 255, 255), (enemy2[0], enemy2[1], 20, 40))
    pygame.draw.rect(screen, (255, 255, 255), (enemy3[0], enemy3[1], 20, 40))
    
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (100, 0, 200), (200, 650, 100, 20))
    
    #third platform
    pygame.draw.rect(screen, (150, 0, 255), (250, 550, 100, 20))
    
    #fourth platform
    pygame.draw.rect(screen, (180, 70, 95), (320, 450, 100, 20))
    
    #fifth platform
    pygame.draw.rect(screen, (90, 0, 155), (270, 340, 100, 20))
    
    #sixth platform
    pygame.draw.rect(screen, (50, 155, 230), (100, 240, 100, 20))
    
    #seventh platform
    pygame.draw.rect(screen, (255, 200, 0), (50, 130, 100, 20))
    
    
    
    
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
if health <= 0:
    print("Game over, you died")
pygame.quit()
