import pygame

pygame.init()
janela = pygame.display.set_mode((800, 600))
fonte = pygame.font.SysFont('comicsans', 30, True, True)
branco = (255, 255, 255)
pygame.display.set_caption('A origem de O-rock')

fundo = pygame.image.load('reino1.png')
orock = pygame.image.load('O-rockParado.png')
clock = pygame.time.Clock()
life = 0
andarDireita = [pygame.image.load('O-Rock Direita Andando 1.png'), pygame.image.load('O-Rock Direita Andando 2.png')]
andarEsquerda = [pygame.image.load('O-Rock Esquerda Andando 1.png'), pygame.image.load('O-Rock Esquerda Andando 2.png')]
andarCima = [pygame.image.load('O-Rock Cima Andando 1.png'), pygame.image.load('O-Rock Cima Andando 2.png')]
andarBaixo = [pygame.image.load('O-Rock Baixo Andando 1.png'), pygame.image.load('O-Rock Baixo Andando 2.png')]
sabioparado = pygame.image.load('SabioParado.png')
reiparado = pygame.image.load('ReiBaixoParado.png')
cena1 = pygame.image.load('primeiracena.png')
cena2 = pygame.image.load('casainterior.png')
cena3 = pygame.image.load('primeiracena.png')
cena4 = pygame.image.load('entrada_castelo.png')
cena5 = pygame.image.load('interiorcast.png')
espada = pygame.image.load('Espada.png')


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.esquerda = False
        self.direita = False
        self.cima = False
        self.baixo = False
        self.andarcont = 0
        self.standing = True
        self.caixadedano = (self.x, self.y, 23, 30)

    def draw(self, janela):
        if self.andarcont + 1 >= 13:
            self.andarcont = 0
        self.caixadedano = (self.x, self.y, 23, 30)

        if not (self.standing):
            if self.esquerda:
                janela.blit(andarEsquerda[self.andarcont // 6], (self.x, self.y))
                self.andarcont += 1
            elif self.direita:
                janela.blit(andarDireita[self.andarcont // 6], (self.x, self.y))
                self.andarcont += 1
            elif self.cima:
                janela.blit(andarCima[self.andarcont // 6], (self.x, self.y))
                self.andarcont += 1
            elif self.baixo:
                janela.blit(andarBaixo[self.andarcont // 6], (self.x, self.y))
                self.andarcont += 1
        else:
            if self.direita:
                janela.blit(andarDireita[0], (self.x, self.y))
            elif self.esquerda:
                janela.blit(andarEsquerda[0], (self.x, self.y))
            elif self.cima:
                janela.blit(andarCima[0], (self.x, self.y))
            elif self.baixo:
                janela.blit(andarBaixo[0], (self.x, self.y))


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x - 10
        self.y = y - 5
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 5 * facing

    def draw(self, janela):
        janela. blit(janela, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    janela.blit(cena1, (0, 0))
    man.draw(janela)
    for bullet in bullets:
        bullet.draw(janela)

    pygame.display.update()


# mainloop
man = player(200, 410, 64, 64)
bullets = []
run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 5:
            bullets.append(
                projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0, 0, 0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    redrawGameWindow()

pygame.quit()