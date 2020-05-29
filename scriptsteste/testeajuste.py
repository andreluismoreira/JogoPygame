import pygame, sys

pygame.init()
janela = pygame.display.set_mode((800, 600))
fonte = pygame.font.SysFont('comicsans', 30, True, True)
#cor
branco = (255, 255, 255)
verde = (50,205,50)
vermelho = (255,0,0)

pygame.display.set_caption('A origem de O-rock')
fundo = pygame.image.load('reino1.png').convert()
clock = pygame.time.Clock()
life = 0
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
reidireita =['reidireita/Rei Baixo Parado.png', 'reidireita/Rei Direita Andando1.png', 'reidireita/Rei Direita Andando2.png']
reiequerda =['reiesquerda/Rei Baixo Parado.png', 'reiesquerda/Rei Esquerda Andando1.png', 'reiesquerda/Rei Esquerda Andando2.png']
rei = pygame.image.load('reidireita/Rei Baixo Parado.png').convert_alpha()
sabio = pygame.image.load('sabioParado.png').convert_alpha()

cena1 = pygame.image.load('casainterior.png') #posiperso x260,y560
cena2 = pygame.image.load('primeiracena.png') #posiperso x635,y330
cena3 = pygame.image.load('entrada_castelo.png') #posiperso x390 y560
cena4 = pygame.image.load('interiorcast.png') #posiperso x394 y540
espada = pygame.image.load('Espada.png')
enemies = True
andar = -1

mdkx = 150
mdky = 500
cimay = 300
cimax = 100
baixox = 150
baixoy = 500


def walk():
    global andar
    andar += 1
    if andar < 2:
        return andar
    else:
        andar = 0
        return andar
mdkx = 150
mdky = 500
cimay = 300
cimax = 100
baixox = 150
baixoy = 500
while enemies == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    janela.blit(cena2, (0, 0))
    pygame.display.update()
    if mdky > cimay and mdkx == baixox:
        pygame.display.update()
        mdky -= 5
        mdk = pygame.image.load(modockcima[walk()]).convert_alpha()
    elif mdky == cimay and mdkx > cimax:
        pygame.display.update()
        mdkx -= 5
        mdk = pygame.image.load(modockesquerda[walk()]).convert_alpha()
    elif mdky <= baixoy and mdkx < baixox:
        pygame.display.update()
        mdky += 5
        mdk = pygame.image.load(modockbaixo[walk()]).convert_alpha()
    elif mdky > baixoy and mdkx >= cimax:
        mdk = pygame.image.load(modockdireita[walk()]).convert_alpha()
        pygame.display.update()
        mdkx += 5

    print(f'x ={mdkx} y = {mdky}')
    pygame.display.update()
    janela.blit(mdk, pygame.rect.Rect(mdkx, mdky, 0, 0))
    pygame.display.update()
    pygame.draw.rect(janela, vermelho, [mdkx - 10, mdky - 10, 50, 2], 4)
    life = pygame.draw.rect(janela, verde, [mdkx - 10, mdky - 10, 50, 2], 4)
    pygame.display.update()
    pygame.time.delay(100)

    if mdkx != 150:
        pygame.draw.rect(janela, verde, [mdkx + (5 + -11), mdky - 9, 50, 2], 4)
    pygame.display.update()