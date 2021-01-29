import pygame
from time import sleep
from pygame.constants import KEYDOWN, K_ESCAPE, K_SPACE, K_UP, K_y, QUIT, K_DOWN, K_LEFT, K_RIGHT, WINDOWEXPOSED
from random import randint, randrange


def message(text, color, x, y):
    message = fontStyle.render(text, 1, color)
    screen.blit(message, [x, y])


def playerSnake(snakeBlock, snakeList):
    for i in snakeList:
        pygame.draw.rect(screen, (100, 100, 100),
                         (i[0], i[1], snakeBlock, snakeBlock))


pygame.init()

windowWidth = 400
windowHeight = 400

screen = pygame.display.set_mode((windowWidth, windowHeight))
clock = pygame.time.Clock()


fontStyle = pygame.font.SysFont(None, 25)
fontStyleScore = pygame.font.SysFont(None, 20)
fontStyleLevel = pygame.font.SysFont(None, 15)
positionX = windowWidth/2
positionY = windowHeight/2
deltaX = 0
deltaY = 0
snakeBlock = 10
snakeSpeed = 10
snakeList = []
snakeLength = 1

foodX = round((randrange(10, windowWidth-10))/10) * 10
foodY = round((randrange(10, windowHeight-10))/10) * 10


appRunning = True
while appRunning:

    gameRunning = True
    while gameRunning:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    gameRunning = False
                elif event.type == QUIT:
                    gameRunning = False
                elif event.key == K_UP:
                    deltaX = 0
                    deltaY = -snakeBlock
                elif event.key == K_DOWN:
                    deltaX = 0
                    deltaY = snakeBlock
                elif event.key == K_LEFT:
                    deltaX = -snakeBlock
                    deltaY = 0
                elif event.key == K_RIGHT:
                    deltaX = snakeBlock
                    deltaY = 0

        positionX += deltaX
        positionY += deltaY

        if positionX > windowWidth - (snakeBlock) or positionX < 0:
            gameRunning = False
        elif positionY > windowHeight - (snakeBlock) or positionY < 0:
            gameRunning = False
        screen.fill((200, 200, 000))

        food = pygame.draw.rect(screen, (50, 50, 50), [foodX, foodY, 10, 10])
        if snakeLength >= 5 and snakeLength <= 10:
            snakeSpeed = 15
        elif snakeLength > 10 and snakeLength <= 15:
            snakeSpeed = 20
        elif snakeLength > 15:
            snakeSpeed = 25

        snakeHead = []
        snakeHead.append(positionX)
        snakeHead.append(positionY)
        snakeList.append(snakeHead)
        print('snakeHead', snakeHead)
        print('snakeList: ', snakeList)
        if len(snakeList) > snakeLength:
            del snakeList[0]

        for i in snakeList[:-1]:
            if i == snakeHead:
                gameRunning = False

        playerSnake(snakeBlock, snakeList)

        if positionX == foodX and positionY == foodY:
            print('Yummy')
            foodX = round((randint(10, windowWidth-10))/10) * 10
            foodY = round((randint(10, windowHeight-10))/10) * 10
            snakeLength += 1

        pygame.display.flip()
        clock.tick(snakeSpeed)

    decisionToContinueOrExit = True
    while decisionToContinueOrExit:
        screen.fill((0, 0, 0))
        message('Game Ended', (100, 0, 0), windowWidth/4, windowHeight/3)
        message('Press space or y key to start again',
                (100, 100, 0), windowWidth/4, windowHeight/3 + 40)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_y or event.key == K_SPACE:
                    gameRunning = True
                    decisionToContinueOrExit = False
                    positionX = windowWidth/2
                    positionY = windowHeight/2
                    deltaX = 0
                    deltaY = 0
                    snakeBlock = 10
                    snakeSpeed = 10
                    snakeList = []
                    snakeLength = 1
                    foodX = round((randint(10, windowWidth-10))/10) * 10
                    foodY = round((randint(10, windowHeight-10))/10) * 10
                elif event.type == QUIT:
                    pygame.quit()
                    quit()


pygame.quit()
