import os,sys,pygame,time
from pygame.locals import*
screen = pygame.display.set_mode((640,580))
pygame.init()

def exit():
    pygame.quit()
    sys.exit()
    pygame.display.update()

def cont():
    screen = pygame.display.set_mode((640,580))
    pygame.init()
    screen_color = pygame.color.Color("white")
    myfont = pygame.font.SysFont(None, 30,)
    myfont2 = pygame.font.SysFont(None, 40)
    labelx = myfont.render("W, Moves player 1 paddle up.",1,(0,0,0))
    labely = myfont.render("S, Moves player 1 paddle down.",1,(0,0,0))
    labelz = myfont.render("Up Arrow, Moves player 2 paddle up.",1,(0,0,0))
    labelo = myfont.render("Down Arrow, Moves player 2 paddle down.",1,(0,0,0))
    labelp = myfont.render("Press backspace to return to the main menu.",1,(0,0,0))
    labelE = myfont2.render("Controls",1,(0,0,0))

    while True:
        screen.fill(screen_color)
        screen.blit(labelE, (260,50))
        screen.blit(labelx,(200, 120))
        screen.blit(labely,(190,180))
        screen.blit(labelz,(165,240))
        screen.blit(labelo,(140,300))
        screen.blit(labelp,(100,400))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()

        keys = pygame.key.get_pressed()

        if keys[K_BACKSPACE]:
            Home()

        
        pygame.display.flip()
        
        
def soloDolo():
    screen = pygame.display.set_mode((640,580))
    pygame.init()
    import random
    
    paddle_width = 10
    paddle_height = 50
    pole = 20
    pole2 = 480
    cent = 80
    cent2 = 40
    sfw = 640
    sfH = 20
    p1Score = 0
    p2Score = 0
    p1Paddle = pygame.Rect(10,230,paddle_width,paddle_height)
    p2Paddle = pygame.Rect(620,230,paddle_width,paddle_height)
    field1 = pygame.Rect(320,0,pole,pole2)
    field2 = pygame.Rect(290,240,cent,cent2)
    sf = pygame.Rect(0,480,sfw,sfH)

    field_color = pygame.color.Color("black")

    paddle_color = pygame.color.Color("blue")
    screen_color = pygame.color.Color("white")

    puck = pygame.Rect(320,240,10,10)
    puck_color = pygame.color.Color("orange")

    p1PaddleSpeedY = 0
    p2PaddleSpeedY = 1

    puckspeedX = 1
    puckspeedY = 1

    k = 10

    myfont = pygame.font.SysFont(None, 30,)
    myfont3 = pygame.font.SysFont(None,100)
    label1 = myfont.render("Player 1", 1, (0,0,0))
    labelc = myfont.render("Comp", 1, (128,128,128))
    labeld = myfont.render("Return the puck to earn points", 1, (0,0,0))
    labelu = myfont.render("Press enter to continue to the home screen",1,(0,0,0))

    while p1Score < 10 and p2Score < 10:
        puck.left = puck.left + puckspeedX
        puck.top = puck.top + puckspeedY
        screen.fill(screen_color);
        screen.fill(field_color,sf)
        screen.blit(label1, (20, 505))
        screen.blit(labelc, (540, 505))
        screen.fill(paddle_color, p1Paddle)
        screen.fill(paddle_color, p2Paddle)
        screen.fill(field_color, field1)
        screen.fill(field_color, field2)
        screen.fill(puck_color, puck)

        pygame.time.delay(k)

        
        
        if puck.colliderect(p1Paddle):
            puckspeedX = puckspeedX * -1
            k = k - 2
            print (k)
            p1Score = p1Score + 1

        if puck.colliderect(p2Paddle):
            puckspeedX = puckspeedX * -1

        if puck.top < 0 or puck.bottom > 480:
            puckspeedY = puckspeedY * -1

        if puck.left < 0 or puck.right > 640:
            puckspeedX = puckspeedX * -1

        if puck.left == 0:
            puck = pygame.Rect(320,240,10,10)
            p2Score = p2Score + 1
            
        elif puck.right == 640:
            puck = pygame.Rect(320,240,10,10)
            p1Score = p1Score + 1
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()

        p2Paddle.top = puck.top
        
        keys = pygame.key.get_pressed()
        if keys[K_w] and p1Paddle.top >= 0:
            p1Paddle.top = p1Paddle.top + p1PaddleSpeedY - 2

        if keys[K_s] and p1Paddle.bottom <=480:
            p1Paddle.top = p1Paddle.top + p1PaddleSpeedY + 2

        s1 = str(p1Score)
        s2 = str(p2Score)
        score1 = myfont.render(s1, 1, (0,0,0))
        screen.blit(score1,(20,530))
        score2 = myfont.render(s2, 1, (0,0,0))
        screen.blit(score2, (540, 530))

        if p1Score == 10:
            labelw = myfont3.render("YOU WIN!!!!",1,(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))

        if p2Score == 10:
            labelw = myfont3.render("YOU LOSE",1,(255,0,0))
                    
        pygame.display.flip()

    while True:
        screen.fill(screen_color)
        screen.blit(labelw, (200,150))
        screen.blit(labelu,(0,520))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()

        keys = pygame.key.get_pressed()

        if keys[K_RETURN]:
            Home()


def playMulti():
    
    # Starts pygame
    pygame.init()

    import random
    
    # Sets values to all items needed on screen
    screen = pygame.display.set_mode((640,580))
    paddle_width = 10
    paddle_height = 50
    pole = 20
    pole2 = 480
    cent = 80
    cent2 = 40
    sfw = 640
    sfH = 20
    p1Score = 0
    p2Score = 0
    p1Paddle = pygame.Rect(10,230,paddle_width,paddle_height)
    p2Paddle = pygame.Rect(620,230,paddle_width,paddle_height)
    field1 = pygame.Rect(320,0,pole,pole2)
    field2 = pygame.Rect(290,240,cent,cent2)
    sf = pygame.Rect(0,480,sfw,sfH)

    field_color = pygame.color.Color("black")

    paddle_color = pygame.color.Color("blue")
    screen_color = pygame.color.Color("white")

    puck = pygame.Rect(320,240,10,10)
    puck_color = pygame.color.Color("orange")

    # Sets speed for items needing it
    p1PaddleSpeedY = 0

    puckspeedX = 1
    puckspeedY = 1
    
    # Counters
    k = 6
    s = 8

    #gameplay text
    myfont = pygame.font.SysFont(None, 30)
    myfont3 = pygame.font.SysFont(None,100)
    label1 = myfont.render("Player 1", 1, (0,0,0))
    label2 = myfont.render("Player 2", 1, (0,0,0))
    labelu = myfont.render("Press enter to continue to the home screen",1,(0,0,0))
    
    while p1Score < 10 and p2Score < 10:
        # Displays the screen
        screen.fill(screen_color);
        screen.fill(field_color,sf)
        screen.blit(label1, (20, 505))
        screen.blit(label2, (540, 505))
        screen.fill(paddle_color, p1Paddle)
        screen.fill(paddle_color, p2Paddle)
        screen.fill(field_color, field1)
        screen.fill(field_color, field2)
        screen.fill(puck_color, puck)
        pygame.time.delay(k)

        # Gets the puck moving
        puck.left = puck.left + puckspeedX
        puck.top = puck.top + puckspeedY

        # How the ball reacts to paddles and walls
        if puck.colliderect(p1Paddle):
            puckspeedX = puckspeedX * -1
            k = k - 1

        if puck.colliderect(p2Paddle):
            puckspeedX = puckspeedX * -1
            k = k - 1

        if puck.top < 0 or puck.bottom > 480:
            puckspeedY = puckspeedY * -1

        if puck.left < 0 or puck.right > 640:
            puckspeedX = puckspeedX * -1

        if puck.left == 0:
            puck = pygame.Rect(320,240,10,10)
            p2Score = p2Score + 1
            k = 5
            
        elif puck.right == 640:
            puck = pygame.Rect(320,240,10,10)
            p1Score = p1Score + 1
            k = 5
        # Player controlled movement
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()

        keys = pygame.key.get_pressed()
        if keys[K_w] and p1Paddle.top >= 0:
            p1Paddle.top = p1Paddle.top + p1PaddleSpeedY - 2

        if keys[K_s] and p1Paddle.bottom <=480:
            p1Paddle.top = p1Paddle.top + p1PaddleSpeedY + 2

        if keys[K_UP] and p2Paddle.top >= 0:
            p2Paddle.top = p2Paddle.top + p1PaddleSpeedY - 2

        if keys[K_DOWN] and p2Paddle.bottom <= 480:
            p2Paddle.top = p2Paddle.top + p1PaddleSpeedY + 2
            
        #Score Keeper
        s1 = str(p1Score)
        s2 = str(p2Score)
        score1 = myfont.render(s1, 1, (0,0,0))
        screen.blit(score1,(20,530))
        score2 = myfont.render(s2, 1, (0,0,0))
        screen.blit(score2, (540, 530))

        if p1Score == 10:
            labelw = myfont3.render("PLAYER 1 WINS!!!!",1,(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))

        if p2Score == 10:
            labelw = myfont3.render("PLAYER 2 WINS!!!!",1,(random.randrange(1,255),random.randrange(1,255),random.randrange(1,255)))
                    
        pygame.display.flip()

    while True:
        screen.fill(screen_color)
        screen.blit(labelw, (10,150))
        screen.blit(labelu,(0,520))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()

        keys = pygame.key.get_pressed()

        if keys[K_RETURN]:
            Home()

        
    Home()

def Home():
    
    #Starts pygame
    pygame.init()
    #Screen display
    screen = pygame.display.set_mode((640,580))
    screen_color = pygame.color.Color("white")
    myfont = pygame.font.SysFont(None, 30)
    myfont1 = pygame.font.SysFont(None,40)

    labelt = myfont.render("Pong .1", 1, (0,0,0))

    select = 1

    while True:
        screen.fill(screen_color)

        if select == 1:
            label = myfont1.render("Single Player", 1, (0,0,255))
        else:
            label = myfont.render("Single Player", 1, (0,0,0))
        if select == 2:
            label2 = myfont1.render("Two Player", 1, (0,0,255))
        else:
            label2 = myfont.render("Two Player", 1, (0,0,0))
        if select == 3:
            label3 = myfont1.render("Controls", 1, (0,0,255))
        else:
            label3 = myfont.render("Controls", 1, (0,0,0))
        if select == 4:
            label4 = myfont1.render("Quit", 1, (0,0,255))
        else:
            label4 = myfont.render("Quit", 1, (0,0,0))

        screen.blit(label, (260, 150))
        screen.blit(label2, (270, 225))
        screen.blit(label3, (280, 300))
        screen.blit(label4, (290, 375))
        screen.blit(labelt, (290, 50))
        pygame.time.delay(250)

        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                pygame.display.update()

        keys = pygame.key.get_pressed()

        if keys[K_w]:
            if (select - 1) < 0:
                select = 4
            else:
                select = select - 1

        if keys[K_s]:
            if (select + 1) > 4:
                select = 1
            else:
                select = select + 1

        if keys[K_RETURN]:
            if select == 1:
                soloDolo()
            elif select == 2:
                playMulti()
            elif select == 3:
                cont()
            else:
                exit()

Home()
