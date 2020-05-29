import pygame

pygame.init()
janela = pygame.display.set_mode((800, 600))
fonte = pygame.font.SysFont('comicsans', 30, True, True)
branco = (255, 255, 255)
pygame.display.set_caption('A origem de O-rock')

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

class Jogador(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.velocidade = 4
        self.esquerda = False
        self.direita = False
        self.cima = False
        self.baixo = False
        self.andarcont = 0
        self.width = width
        self.height = height
        self.standing = True
        self.caixadedano = (self.x, self.y, 23, 30)

    def draw(self, janela):
        if self.andarcont + 1 >= 13:
            self.andarcont = 0
        self.caixadedano = (self.x, self.y, 23, 30)
        #pygame.draw.rect(janela, (255, 0, 0), self.caixadedano, 2)

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


class projectile (object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x - 10
        self.y = y - 5
        self.radius = radius
        self.color = color
        self.velocidade = 5 * facing
        self.facing = facing

    def draw(self, janela):
        janela.blit(espada, (self.x - 10, self.y - 5))


class Enemies (object):
    modrockCima = [pygame.image.load('Modrock Cima Andando 1.png'), pygame.image.load('Modrock Cima Andando 2.png')]
    modrockBaixo = [pygame.image.load('Modrock Baixo Andando 1.png'), pygame.image.load('Modrock Baixo Andando 2.png')]
    reicima = [pygame.image.load('Rei Cima Andando 1.png'), pygame.image.load('Rei Cima Andando 2.png')]
    reibaixo = [pygame.image.load('Rei Baixo Andando 1.png'), pygame.image.load('Rei Baixo Andando 2.png')]


    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.heigth = height
        self.end = end
        self.path = [self.x, self. y]
        self.andarcont = 0
        self.velocidade = 3
        self.caixadedano = (self.x, self.y, 23, 30)
        self.saude = 10
        self.visivel = True


    def draw(self, janela):
        self.move()
        if self.visivel:
            if self.andarcont + 1 >= 13:
                self.andarcont = 0

            if self.velocidade > 0:
                janela.blit(self.modrockBaixo[self.andarcont // 6], (self.x, self.y))
                self.andarcont += 1
            else:
                janela.blit(self.modrockCima[self.andarcont // 6], (self.x, self.y))
                self.andarcont += 1
            pygame.draw.rect(janela, (255, 0, 0), (self.caixadedano[0] - 10, self.caixadedano[1] - 20, 50, 5))
            pygame.draw.rect(janela, (0, 128, 0), (self.caixadedano[0] - 10, self.caixadedano[1] - 20, 50 - (5 * (10 - self.saude)), 5))

    def move(self):
        if self.velocidade > 0:
            if self.y + self.x < self.path[1]:
                self.y += self.velocidade
            else:
                self.velocidade = self.velocidade * -1
                self.andarcont = 0
        else:
            if self.y - self.x > self.path[0]:
                self.y += self.velocidade
            else:
                self.velocidade = self.velocidade * -1
                self.andarcont = 0
        self.caixadedano = (self.x, self.y, 23, 30)
        #pygame.draw.rect(janela, (255,0,0), self.caixadedano, 2)

    def hit(self):
        if self.saude > 0:
            self.saude -= 1
        else:
            self.visivel = False


def redrawgamewindow():
    janela.blit(cena1, (0, 0))
    #text = fonte.render('Score: ' + str(life), 1, (branco))
    #janela.blit(text, [690, 10])
    man.draw(janela)
    modrock.draw(janela)

    pygame.display.update()
    for bullet in bullets:
        bullet.draw(janela)


#def texto(msg, cor):
    #texto1 = fonte.render(msg, True, cor)
    #fundo.blit(texto1, [400 / 40, 300 / 10])

loopdetiro = 0
janelaaberta = True
bullets = []
man = Jogador(10, 430, 25, 31)
modrock = Enemies(150, 600, 64, 64, 800)
janela = pygame.display.set_mode((800, 600))
while janelaaberta:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if loopdetiro > 0:
        loopdetiro += 1
    if loopdetiro > 5:
        loopdetiro = 0

    for bullet in bullets:
        if bullet.y - bullet.radius < modrock.caixadedano[1] + modrock.caixadedano [3] and bullet.y - bullet.radius > modrock.caixadedano[1]:
            if bullet.x + bullet.radius > modrock.caixadedano[0] and bullet.x - bullet.radius < modrock.caixadedano[0] + modrock.caixadedano[2]:
                modrock.hit()
                life += 1
                bullets.pop(bullets.index((bullet)))
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.velocidade
        else:
            bullets.pop(bullets.index(bullet))
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_SPACE] and loopdetiro == 0:
        if man.esquerda:
            facing = -1
        else:
            facing = 1
        if len(bullets) < 5:
            bullets.append(projectile(round(man.x + man.width//2), round(man.y + man.height//2), 6, (0, 0, 0), facing))
        loopdetiro = 1

    if comandos[pygame.K_UP]:
        man.y -= man.velocidade
        man.cima = True
        man.baixo = False
        man.direita = False
        man.esquerda = False
        man.standing = False
    elif comandos[pygame.K_DOWN]:
        man.y += man.velocidade
        man.baixo = True
        man.cima = False
        man.direita = False
        man.esquerda = False
        man.standing = False
    elif comandos[pygame.K_RIGHT]:
        man.x += man.velocidade
        man.direita = True
        man.esquerda = False
        man.standing = False
    elif comandos[pygame.K_LEFT]:
        man.x -= man.velocidade
        man.esquerda = True
        man.direita = False
        man.standing = False
    else:
        man.standing = True
        man.andarcont = 0
    redrawgamewindow()
    pygame.display.update()
    pygame.quit()
