import pygame, sys

pygame.init()
janela = pygame.display.set_mode((800, 600))

fonte = pygame.font.SysFont('comicsans', 30, True, True)
branco = (255, 255, 255)
pygame.display.set_caption('A origem de O-rock')
fundo = pygame.image.load('reino1.png').convert()
clock = pygame.time.Clock()
life = 0
personright = ['orockdireita/OrockDireitaParado.png', 'orockdireita/OrockDireitaAndando1.png', 'orockdireita/OrockDireitaAndando2.png']
personleft = ['orockesquerda/OrockEsquerdaParado.png', 'orockesquerda/OrockEsquerdaAndando1.png', 'orockesquerda/OrockEsquerdaAndando2.png']
personup = ['orockcima/OrockCimaParado.png','orockcima/OrockCimaAndando1.png', 'orockcima/OrockCimaAndando2.png']
persondown = ['orockbaixo/OrockbaixoParado0.png', 'orockbaixo/OrockbaixoAndando1.png', 'orockbaixo/OrockbaixoAndando2.png']
loadperson = pygame.image.load('O-RockParado.png').convert_alpha()
modockcima =['modrockcima/Modrock Baixo Parado.png','modrockcima/Modrock Cima Andando1.png', 'modrockcima/Modrock Cima Andando2.png']
modockbaixo =['modrockbaixo/Modrock Baixo Parado.png', 'modrockbaixo/Modrock Baixo Andando1.png', 'modrockbaixo/Modrock Baixo Andando2.png']
reidireita =['reidireita/Rei Baixo Parado.png', 'reidireita/Rei Direita Andando1.png', 'reidireita/Rei Direita Andando2.png']
reiequerda =['reiesquerda/Rei Baixo Parado.png', 'reiesquerda/Rei Esquerda Andando1.png', 'reiesquerda/Rei Esquerda Andando2.png']
sabio = pygame.image.load('sabioParado.png').convert_alpha()
cena1 = pygame.image.load('casainterior.png') #posiperso x260,y560
cena2 = pygame.image.load('primeiracena.png') #posiperso x635,y330
cena3 = pygame.image.load('entrada_castelo.png') #posiperso x390 y560
cena4 = pygame.image.load('interiorcast1.png') #posiperso x394 y540
espada = pygame.image.load('Espada.png')
personx = 260
persony = 560
andar = -1

def walk():
    global andar
    andar += 1
    if andar < 2:
        return andar
    else:
        andar = 0
        return andar

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    janela.blit(cena4, (0, 0))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP] :
        personx += 5
        loadperson = pygame.image.load(personright[walk()]).convert_alpha()
    if pressed[pygame.K_DOWN]:
        persony += 5
        loadperson = pygame.image.load(persondown[walk()]).convert_alpha()
    if pressed[pygame.K_LEFT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
        personx -= 5
        loadperson = pygame.image.load(personleft[walk()]).convert_alpha()
    if pressed[pygame.K_UP]:
        persony -= 5
        loadperson = pygame.image.load(personup[walk()]).convert_alpha()
    janela.blit(loadperson, pygame.rect.Rect(personx, persony, 0, 0))
    janela.blit(sabio, (417, 345))
    pygame.display.update()
    pygame.time.delay(100)
    print(f'x={personx}   y= {persony}')
