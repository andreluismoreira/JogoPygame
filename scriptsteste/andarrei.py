import pygame, sys

pygame.init()
janela = pygame.display.set_mode((800, 600))
fonte = pygame.font.SysFont('comicsans', 30, True, True)
#cor
branco = (255, 255, 255)
verde = (50,205,50)
vermelho = (255,0,0)
liferei = 50
pygame.display.set_caption('A origem de O-rock')
fundo = pygame.image.load('reino1.png').convert()
clock = pygame.time.Clock()

personright = ['orockdireita/OrockDireitaParado.png', 'orockdireita/OrockDireitaAndando1.png', 'orockdireita/OrockDireitaAndando2.png']
personleft = ['orockesquerda/OrockEsquerdaParado.png', 'orockesquerda/OrockEsquerdaAndando1.png', 'orockesquerda/OrockEsquerdaAndando2.png']
personup = ['orockcima/OrockCimaParado.png','orockcima/OrockCimaAndando1.png', 'orockcima/OrockCimaAndando2.png']
persondown = ['orockbaixo/OrockbaixoParado0.png', 'orockbaixo/OrockbaixoAndando1.png', 'orockbaixo/OrockbaixoAndando2.png']
loadperson = pygame.image.load('O-RockParado.png').convert_alpha()

modockcima =['modrockcima/Modrock Cima Andando 1.png', 'modrockcima/Modrock Cima Andando 2.png']
modockbaixo =['modrockbaixo/Modrock Baixo Parado.png', 'modrockbaixo/Modrock Baixo Andando 1.png', 'modrockbaixo/Modrock Baixo Andando 2.png']
modockesquerda = ['modrockesquerda/modrockesquerdaparado.png', 'modrockesquerda/modrockesquerdaandando1.png', 'modrockesquerda/modrockesquerdaandando2.png' ]
modockdireita = ['modrockdireita/modrockdireitaparado.png', 'modrockdireita/modrockdireitaandando1.png', 'modrockdireita/modrockdireitaandando2.png']
mdk = pygame.image.load('modrockcima/Modrock Baixo Parado.png').convert_alpha()

reidireita =['reidireita/Rei Direita Andando 1.png', 'reidireita/Rei Direita Andando 2.png']
reicima = ['reicima/reicimaparado.png', 'reicima/reicimaandando 1.png', 'reicima/reicimaandando2.png']
reibaixo = ['reibaixo/reibaixoandando1.png','reibaixo/reibaixo andando2.png']
reiequerda =[ 'reiesquerda/Rei Esquerda Andando 1.png', 'reiesquerda/Rei Esquerda Andando 2.png']
rei = pygame.image.load('ReiBaixoParado.png').convert_alpha()

sabio = pygame.image.load('sabioParado.png').convert_alpha()

cena1 = pygame.image.load('casainterior.png') #posiperso x260,y560
cena2 = pygame.image.load('primeiracena.png') #posiperso x635,y330
cena3 = pygame.image.load('entrada_castelo.png') #posiperso x390 y560
cena4 = pygame.image.load('interiorcast1.png') #posiperso x394 y540
espada = pygame.image.load('Espada.png')
enemies = True
andar = -1


def walk():
    global andar
    andar += 1
    if andar < 2:
        return andar
    else:
        andar = 0
        return andar
reix = 390
reiy = 315
reicimay = 320
reicimax = 305
reibaixox = 505
reibaixoy = 495
while enemies == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    janela.blit(cena4, (0, 0))
    pygame.display.update()
    if reiy > reicimay and reix == reibaixox:
        pygame.display.update()
        reiy -= 5
        rei = pygame.image.load(reicima[walk()]).convert_alpha()
    elif reiy == reicimay and reix > reicimax:
        pygame.display.update()
        reix -= 5
        rei = pygame.image.load(reiequerda[walk()]).convert_alpha()
    elif reiy <= reibaixoy and reix < reibaixox:
        pygame.display.update()
        reiy += 5
        rei = pygame.image.load(reibaixo[walk()]).convert_alpha()
    elif reiy > reibaixoy and reix >= reicimax:
        rei = pygame.image.load(reidireita[walk()]).convert_alpha()
        pygame.display.update()
        reix += 5

    print(f'x ={reix} y = {reiy}')
    pygame.display.update()
    janela.blit(rei, pygame.rect.Rect(reix, reiy, 0, 0))
    pygame.display.update()
    pygame.draw.rect(janela, vermelho, [reix - 10, reiy - 10, liferei, 2], 4)
    life = pygame.draw.rect(janela, verde, [reix - 10, reiy - 10, liferei, 2], 4)
    pygame.display.update()
    pygame.time.delay(100)

