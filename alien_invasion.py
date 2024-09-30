import pygame
import random
import math
import sys

""" initialising the pygame"""
pygame.init()
""" Creating the screen for python program"""
length = 800
width = 600
screen = pygame.display.set_mode((length, width))

""" creating the logo and the name for the game"""
pygame.display.set_caption('vineet jangir')

icon = pygame.image.load('boring human.png')
pygame.display.set_icon(icon)

"""defining the player"""
set_image = pygame.image.load('spaceship.png')
playerX = 336
playerY = 440
playerX_change = 0
playerY_change = 0

# variables for the bullets
set_bullet = pygame.image.load('bullet.png')
bulletX = playerX + 48
bulletY = 440
bulletX_change = 5
bulletY_change = 0

"""defining the enemy"""
set_enemy = pygame.image.load('img.png')
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
enemy_alive = []
enemy_count = 2

for i in range(enemy_count):
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 50))
    enemyX_change.append(2.5)
    enemyY_change.append(1)
    enemy_alive.append(True)

# setting background
back = pygame.image.load('background.png')
bullet_state = "ready"

# score calculator
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
score_list = []

# Game over
game_over = pygame.font.Font('freesansbold.ttf', 70)

# timer
mera_time = pygame.font.Font('freesansbold.ttf', 32)


def show_score(x, y):
    score = font.render(f'SCORE = {score_value}', True, (255, 255, 0))
    screen.blit(score, (x, y))


def game_over_text():
    score = game_over.render(f'GAME OVER', True, (255, 255, 255))
    screen.blit(score, (250, 200))


def collision(ex, ey, bx, by):
    x = math.pow(bx - ex, 2)
    y = math.pow(by - ey, 2)
    distance = math.sqrt(x + y)
    return distance


def player(x, y):
    screen.blit(set_image, (playerX, playerY))


def enemy(x, y):
    screen.blit(set_enemy, (enemyX[i], enemyY[i]))


def bullet(x, y):
    bullets = pygame.image.load('bullet.png')
    screen.blit(bullets, (x, y))


running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
        # linking the movement of the spaceship with the keyboard button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_UP:
                playerY_change = -4
            if event.key == pygame.K_DOWN:
                playerY_change = 4

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                bye = True
                exit()

        if event.type == pygame.KEYUP:
            if (
                    event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key ==
                    pygame.K_DOWN):
                playerX_change = 0
                playerY_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_state = "fire"
                    bulletX = playerX + 48
                    bulletY = playerY
                    bulletY_change = 6

    """creating the walls in the motion of the player"""
    if playerX <= 0:
        playerX = 0
    if playerY <= 0:
        playerY = 0
    if playerX >= length - 128:
        playerX = length - 128
    if playerY >= width - 128:
        playerY = width - 128

    screen.fill((128, 128, 128))

    # adding the background image
    screen.blit(back, (0, 0))
    playerX += playerX_change
    playerY += playerY_change
    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    if bulletY < 0:
        bulletY = 440
        bullet_state = "ready"
    instruct = ""

    """describing the movements of the enemy"""
    for i in range(enemy_count):
        if enemyX[i] <= -14:
            enemyX_change[i] = 2.5
            instruct = "right"

        if enemyX[i] >= length - 50:
            enemyX_change[i] = -2.5
            instruct = "left"

    # describing the movements of the alien in the vertical direction
    for i in range(enemy_count):
        if instruct == "right" or instruct == "left":
            enemyY_change[i] = 1

    # creating wall on the downward side for the alien
    for i in range(enemy_count):
        if enemyY[i] <= -6:
            enemyY_change[i] = 2
            instruct = "right"

        if enemyY[i] >= width - 60:
            enemyY_change[i] = -2
            instruct = "left"

        if enemy_alive:
            enemyY[i] += enemyY_change[i]

            enemyX[i] += enemyX_change[i]
            enemy(enemyX[i], enemyY[i])

    # collision of the bullet and the alien
    for i in range(enemy_count):
        if collision(enemyX[i], enemyY[i], bulletX, bulletY) <= 27:
            if bulletY == playerY:
                continue
            else:
                bulletY = playerY
                bullet_state = "ready"
                enemyX[i] = random.randint(0, 736)
                enemyY[i] = random.randint(0, 50)
                score_value += 1

    show_score(textX, textY)
    score_list.append(score_value)
    maxi = 0
    for i in range(len(score_list)):
        if score_list[i] > maxi:
            maxi = score_list[i]
            pass

    # displaying a timer for showing the time left

    # game over
    for i in range(enemy_count):
        if collision(enemyX[i], enemyY[i], playerX, playerY) < 60:
            exit(f'GAME OVER\n'
                 f'Current score: {score_value}')

    pygame.display.update()
print(score_list)

# Completed the game but was not able to display the game over

