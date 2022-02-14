import pygame
import os
import sys


def image1(name, color_key=None):
    tous = os.path.join('data',
                        name)
    try:
        image = pygame.image.load(tous)
    except pygame.error as message:
        print('Не удаётся загрузить:',
              name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is None:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '300, 130'
pygame.display.set_caption('Перемещение героя')
w = 500
h = 500
size = w, h
screen = pygame.display.set_mode(size)
images = {'wall': image1('box.png'),
          'empty': image1('grass.png')}
player_1 = image1('mar.png')
width = 50
height = 50
FPS = 75


class The_first_logic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.rect = (0,
                     0,
                     500,
                     500)


class Full_group(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

    def something(self, some):
        for sprite in self:
            sprite.something(some)


class The_most_important(pygame.sprite.Sprite):
    def __init__(self, lis):
        super().__init__(lis)
        self.rect = None

    def something(self, some):
        pass


class Number_1(The_most_important):
    def __init__(self, tipe, x, y):
        super().__init__(sprites)
        self.image = images[tipe]
        self.rect = self.image.get_rect().move(width * x, height * y)


class process(The_most_important):
    def __init__(self, x, y):
        super().__init__(pro_hero)
        self.image = player_1
        self.rect = self.image.get_rect().move(width * x + 15,
                                               height * y + 5)
        self.pos = (x, y)

    def move(self, x, y):
        self.pos = (x, y)
        self.rect = self.image.get_rect().move(width * self.pos[0] + 15,
                                               height * self.pos[1] + 5)


player = None
running = True

hours = pygame.time.Clock()
sprites = Full_group()
pro_hero = Full_group()


def end():
    pygame.quit()
    sys.exit()


def begin_screen():
    intext = ["Déplacer le héros",
                  "",
                  "carte à sa place",
                  "Le héros fait le mouvement"]
    verb = pygame.transform.scale(image1('fon.jpg'),
                                  size)
    screen.blit(verb, (0, 0))
    faire = pygame.font.Font(None, 40)
    text = 50
    for line in intext:
        string_ = faire.render(line,
                               1,
                               pygame.Color('black'))
        rect_difficult = string_.get_rect()
        text += 20
        rect_difficult.top = text
        rect_difficult.x = 10
        text += rect_difficult.height
        screen.blit(string_,
                    rect_difficult)
    while True:
        for some in pygame.event.get():
            if some.type == pygame.QUIT:
                end()
            elif some.type == pygame.KEYDOWN or \
                    some.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        hours.tick(FPS)


def mygame(file):
    file = "data/" + file
    with open(file, 'r') as mapFile:
        cartoon = [line.strip() for line in mapFile]
    max_width = max(map(len,
                        cartoon))
    return list(map(lambda x: list(x.ljust(max_width,
                                           '.')),
                    cartoon))


def my_work(tr):
    again = None
    x = None
    y = None
    for y in range(len(tr)):
        for x in range(len(tr[y])):
            if tr[y][x] == '.':
                Number_1('empty',
                         x,
                         y)
            elif tr[y][x] == '#':
                Number_1('wall',
                         x,
                         y)
            elif tr[y][x] == '@':
                Number_1('empty',
                         x, y)
                again = process(x,
                                y)
                tr[y][x] = "."
    return again, x, y


def go(hero, diff):
    x, y = hero.pos
    if diff == "up":
        if y > 0 and level[y - 1][x] == ".":
            hero.move(x,
                      y - 1)
    elif diff == "down":
        if y < _iy - 1 and level[y + 1][x] == ".":
            hero.move(x,
                      y + 1)
    elif diff == "left":
        if x > 0 and level[y][x - 1] == ".":
            hero.move(x - 1,
                      y)
    elif diff == "right":
        if x < _x - 1 and level[y][x + 1] == ".":
            hero.move(x + 1,
                      y)


begin_screen()
level = mygame("new_file.txt")
heroid, _x, _iy = my_work(level)
while running:
    for some in pygame.event.get():
        if some.type == pygame.QUIT:
            running = False
        elif some.type == pygame.KEYDOWN:
            if some.key == pygame.K_UP:
                go(heroid, "up")
            elif some.key == pygame.K_DOWN:
                go(heroid, "down")
            elif some.key == pygame.K_LEFT:
                go(heroid, "left")
            elif some.key == pygame.K_RIGHT:
                go(heroid, "right")
    screen.fill(pygame.Color("black"))
    sprites.draw(screen)
    pro_hero.draw(screen)
    hours.tick(FPS)
    pygame.display.flip()
pygame.quit()
