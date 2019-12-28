import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,50)

import pygame
from pygame.locals import *

# pygame module init
pygame.init()
pygame.key.set_repeat(50, 25)

# window config
WND_WIDTH = 800
WND_HEIGHT = 600
WND_TITLE = "Pong"
WND_COLOR = (230, 255, 255)
window = pygame.display.set_mode((WND_WIDTH, WND_HEIGHT))
pygame.display.set_caption(WND_TITLE)

# user paddle config
PAD_WIDTH = 100
PAD_HEIGHT = 20
USER_PAD_COLOR = (0, 0, 255)
USER_PAD_POS = (350, 560)
# create user paddle with fill
user_pad = pygame.Surface((PAD_WIDTH, PAD_HEIGHT), 0, 32)
user_pad.fill(USER_PAD_COLOR)
# set user paddle rectangle for starting position
user_pad_rect = user_pad.get_rect()
user_pad_rect.x = USER_PAD_POS[0]
user_pad_rect.y = USER_PAD_POS[1]

# AI paddle config
AI_PAD_COLOR = (255, 0, 0)
AI_PAD_POS = (350, 20)
# create AI paddle with fill
ai_pad = pygame.Surface((PAD_WIDTH, PAD_HEIGHT))
ai_pad.fill(AI_PAD_COLOR)
# set AI paddle rectangle for starting position
ai_pad_rect = ai_pad.get_rect()
ai_pad_rect.x = AI_PAD_POS[0]
ai_pad_rect.y = AI_PAD_POS[1]
# ai pad speed
AI_SPEED = 5

# ball config
BALL_WIDTH = 20
BALL_HEIGHT = 20
BALL_SPEEDX = 6
BALL_SPEEDY = 6
BALL_COLOR = (0, 255, 0)
# create ball with fill
ball = pygame.Surface((BALL_WIDTH, BALL_HEIGHT), pygame.SRCALPHA, 32).convert_alpha()
pygame.draw.ellipse(ball, BALL_COLOR, (0, 0, BALL_WIDTH, BALL_HEIGHT))
# set ball rectangle for starting position
ball_rect = ball.get_rect()
ball_rect.x = WND_WIDTH/2
ball_rect.y = WND_HEIGHT/2
# set ball animation
BALL_FPS = 30
fpsClock = pygame.time.Clock()

# result labels
USER_PTS = '0'
AI_PTS = '0'
font = pygame.font.Font('freesansbold.ttf', 64)

def showUserPts():
    user_label = font.render(USER_PTS, True, (0, 0, 0))
    user_label_rect = user_label.get_rect()
    user_label_rect.center = (WND_WIDTH/2, WND_HEIGHT*0.75)
    window.blit(user_label, user_label_rect)
def showAiPts():
    ai_label = font.render(AI_PTS, True, (0, 0, 0))
    ai_label_rect = ai_label.get_rect()
    ai_label_rect.center = (WND_WIDTH/2, WND_HEIGHT/4)
    window.blit(ai_label, ai_label_rect)

# main loop
while True:
    for event in pygame.event.get():
        # catch window close
        if event.type == QUIT:
            pygame.quit()
            import sys
            sys.exit()
        
        # catch mouse movement
        if event.type == MOUSEMOTION:
            # mouse coordinates
            mouseX, mouseY = event.pos

            # paddle shift
            pad_shift = mouseX - (PAD_WIDTH/2)

            # if mouse go out of window set paddle in window
            if pad_shift > WND_WIDTH - PAD_WIDTH:
                pad_shift = WND_WIDTH - PAD_WIDTH
            if pad_shift < 0:
                pad_shift = 0
            
            # update paddle position
            user_pad_rect.x = pad_shift

        # catch arrows movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                user_pad_rect.x -= 5
                if user_pad_rect.x < 0:
                    user_pad_rect.x = 0
            if event.key == pygame.K_RIGHT:
                user_pad_rect.x += 5
                if user_pad_rect.x > WND_WIDTH - PAD_WIDTH:
                    user_pad_rect.x = WND_WIDTH - PAD_WIDTH
            
    # ball movement
    ball_rect.move_ip(BALL_SPEEDX, BALL_SPEEDY)

    # if ball go out of window reverse ball movement
    ## left/right
    if ball_rect.right >= WND_WIDTH or ball_rect.left <= 0:
        BALL_SPEEDX *= -1
    ## top, user won
    if ball_rect.top <= 0:
        ball_rect.x = WND_WIDTH/2
        ball_rect.y = WND_HEIGHT/2
        USER_PTS = str(int(USER_PTS) + 1)
    ## bottom, user lost
    if ball_rect.bottom >= WND_HEIGHT:
        ball_rect.x = WND_WIDTH/2
        ball_rect.y = WND_HEIGHT/2
        AI_PTS = str(int(AI_PTS) + 1)
    
    # if ball touch user paddle, point it to opposite direction
    if ball_rect.colliderect(user_pad_rect):
        BALL_SPEEDY *= -1
        # prevent paddle to cover the ball 
        ball_rect.bottom = user_pad_rect.top
    
    # AI movement, ai paddle follows ball
    if ball_rect.center > ai_pad_rect.center:
        ai_pad_rect.x += AI_SPEED
    if ball_rect.center < ai_pad_rect.center:
        ai_pad_rect.x -= AI_SPEED
    # if ball touch ai paddle, point it to opposite direction
    if ball_rect.colliderect(ai_pad_rect):
        BALL_SPEEDY *= -1
        # prevent paddle to cover the ball 
        ball_rect.top = ai_pad_rect.bottom

    # fill window with color
    window.fill(WND_COLOR)
    showUserPts()
    showAiPts()
    # add objects to window
    window.blit(user_pad, user_pad_rect)
    window.blit(ai_pad, ai_pad_rect)
    window.blit(ball, ball_rect)

    # update clock tick
    fpsClock.tick(BALL_FPS)
    
    # update window and show
    pygame.display.update()