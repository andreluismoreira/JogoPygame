import pygame
from random import randrange

branco = (255, 255, 255)
preto = (0, 0, 0)
amarelo = (255, 215, 0)
azul = (70, 130, 180)
cinza = (47, 79, 79)
tamanho = 10
largura = 320
altura = 240

pygame.init()
fundo = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()
pygame.display.set_caption('Snake')
fonte = pygame.font.SysFont(None, 17, 0)

def texto(msg, cor):
    texto1 = fonte.render(msg, True, cor)
    fundo.blit(texto1, [largura/15, altura/2.2])


def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, azul, [XY[0], XY[1], tamanho, tamanho])

def maca(maca_x, maca_y):
    pygame.draw.rect(fundo, amarelo, [maca_x, maca_y, tamanho, tamanho, ])


def jogo():
    velocidade_x = 0
    velocidade_y = 0
    pos_x = randrange(0, largura-tamanho, 10)
    pos_y = randrange(0, altura-tamanho, 10)
    maca_x = randrange(0, largura-tamanho, 10)
    maca_y = randrange(0, altura-tamanho, 10)
    sair = True
    fimdejogo = False
    CobraXY = []
    Cobracomp = 0
    while sair:
        while fimdejogo:
            fundo.fill(preto)
            texto('Fim de Jogo, Para continuar tecle c para sair tecle s', branco)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        jogo()
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_y = 0
                    velocidade_x = -tamanho
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_y = 0
                    velocidade_x = tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
        if sair:
            fundo.fill(cinza)
            pos_y += velocidade_y
            pos_x += velocidade_x
            if pos_x > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x = largura - tamanho
            if pos_y > altura:
                pos_y = 0
            if pos_y < 0:
                pos_y = altura - tamanho
            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura - tamanho, 10)
                maca_y = randrange(0, altura - tamanho, 10)
                Cobracomp += 1
            Cobrainicio = []
            Cobrainicio.append(pos_x)
            Cobrainicio.append(pos_y)
            CobraXY.append(Cobrainicio)
            cobra(CobraXY)
            if len(CobraXY) > Cobracomp:
                del CobraXY[0]
            if any(Bloco == Cobrainicio for Bloco in CobraXY[:-1]):
                fimdejogo = True
            maca(maca_x, maca_y)
            relogio.tick(15)
            pygame.display.update()
jogo()
pygame.quit()
quit()
