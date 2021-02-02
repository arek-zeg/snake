import pygame
from pygame.locals import K_DOWN, K_ESCAPE, K_UP, K_LEFT, K_RIGHT, QUIT, KEYDOWN
from random import randrange


class SnakeHead(pygame.sprite.Sprite):

    def __init__(self, screen, score=0):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 100, 100))
        self.rect = self.surf.get_rect(
            center=(screen.get_width()/2, screen.get_height()/2))
        self.speed = 25
        self.moveDirectionX = 0
        self.moveDirectionY = 0
        self.score = score

    def update(self, pressedKey):
        self.rect.move_ip(self.moveDirectionX, self.moveDirectionY)

        if pressedKey == K_UP:
            self.moveDirectionX = 0
            self.moveDirectionY = -self.speed * 1
        if pressedKey == K_DOWN:
            self.moveDirectionX = 0
            self.moveDirectionY = self.speed * 1
        if pressedKey == K_LEFT:
            self.moveDirectionX = -self.speed * 1
            self.moveDirectionY = 0
        if pressedKey == K_RIGHT:
            self.moveDirectionX = self.speed * 1
            self.moveDirectionY = 0

    def playerSnake(self, screen1, snakeList):
        for i in snakeList:
            self.surf = pygame.Surface((25, 25))
            self.surf.fill((100, 100, 100))
            self.rect = self.surf.get_rect(center=(i[0], i[1]))
            all_sprites.add(self)
            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)


class Food(pygame.sprite.Sprite):
    def __init__(self, screen, ):
        super().__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                round((randrange(0, screen.get_width()-25)/25)) * 25,
                round((randrange(0, screen.get_height()-25)/25)) * 25
            )
        )

    def update(self):
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(
            center=(
                round((randrange(0, screen.get_width()-25)/25)) * 25,
                round((randrange(0, screen.get_height()-25)/25)) * 25
            )
        )


class ScoreBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((400, 25))
        self.surf.fill((0, 0, 200))
        self.rect = self.surf.get_rect()
        self.speedLevelFont = pygame.font.SysFont(None, 20)
        self.snakeLengthFont = pygame.font.SysFont(None, 22)

    def update(self, snakeLength, speedLevel, screen):
        self.labelLevel = self.speedLevelFont.render(
            'Level: ' + str(speedLevel), True, 'yellow')
        self.labelLength = self.snakeLengthFont.render(
            'Score: ' + str(snakeLength), True, 'yellow')
        screen.blit(self.labelLength, (5, 20))
        screen.blit(self.labelLevel, (330, 20))


pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((17, 193, 242))

snakeList = []
snakeLength = 1
positionX = screen.get_width()/2
positionY = screen.get_height()/2

snakeHead1 = SnakeHead(screen)
food1 = Food(screen)
scoreBar = ScoreBar()

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
all_sprites.add(snakeHead1)
all_sprites.add(food1)
all_sprites.add(scoreBar)

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            elif event.type == QUIT:
                running = False
            elif event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT:
                snakeHead1.update(event.key)

    positionX += snakeHead1.moveDirectionX
    positionY += snakeHead1.moveDirectionY

    screen.fill((17, 193, 242))

    scoreBar.update(snakeLength, 1, screen)  # why not showing on top of bar?

    snakeHeadList = []
    snakeHeadList.append(positionX)
    snakeHeadList.append(positionY)
    snakeList.append(snakeHeadList)
    if len(snakeList) > snakeLength:
        del snakeList[0]

    # condition for endgames

    for i in snakeList[:-1]:
        if i == snakeHeadList:
            running = False

    if positionX > screen.get_width() - 25 or positionX < 0:
        running = False
    elif positionY > screen.get_height() - 25 or positionY < 0:
        running = False

    snakeHead1.playerSnake(screen, snakeList)

    if positionX == food1.rect.centerx and positionY == food1.rect.centery:
        print('yummy')
        food1.update()
        snakeLength += 1

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    pygame.display.flip()

    clock.tick(25)


pygame.quit()
