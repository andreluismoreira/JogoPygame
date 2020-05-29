import pygame, sys
from random import randint

#variaveis
itens = []
titem = ', '.join(itens)
itemx = 100
itemy = 100
tela = 0
x = 260
y = 560
width = 800
heigth = 600
mdklife = 50
reilife = 50
lifeorock = 50

#janelajogo
pygame.init()
janela = pygame.display.set_mode((width, heigth))
pygame.display.set_caption('A Origem de O-rock')
clock = pygame.time.Clock()

#cores
branco = (255, 255, 255)
amarelo = (255, 215, 0)
vermelho = (255, 0,  0)
verde = (50, 205, 50)

#imagens
personright = ['imagens/orockdireita/OrockDireitaParado.png', 'imagens/orockdireita/OrockDireitaAndando1.png', 'imagens/orockdireita/OrockDireitaAndando2.png']
personleft = ['imagens/orockesquerda/OrockEsquerdaParado.png', 'imagens/orockesquerda/OrockEsquerdaAndando1.png', 'imagens/orockesquerda/OrockEsquerdaAndando2.png']
personup = ['imagens/orockcima/OrockCimaParado.png', 'imagens/orockcima/OrockCimaAndando1.png', 'imagens/orockcima/OrockCimaAndando2.png']
persondown = ['imagens/orockbaixo/OrockbaixoParado0.png', 'imagens/orockbaixo/OrockbaixoAndando1.png', 'imagens/orockbaixo/OrockbaixoAndando2.png']
loadperson = pygame.image.load('imagens/O-RockParado.png').convert_alpha()

modockcima =['imagens/modrockcima/Modrock Cima Andando 1.png', 'imagens/modrockcima/Modrock Cima Andando 2.png']
modockbaixo =['imagens/modrockbaixo/Modrock Baixo Andando 1.png', 'imagens/modrockbaixo/Modrock Baixo Andando 2.png']
modockesquerda = ['imagens/modrockesquerda/modrockesquerdaandando1.png', 'imagens/modrockesquerda/modrockesquerdaandando2.png' ]
modockdireita = ['imagens/modrockdireita/modrockdireitaandando1.png', 'imagens/modrockdireita/modrockdireitaandando2.png']
modock = pygame.image.load('imagens/modrockcima/Modrock Baixo Parado.png').convert_alpha()

reidireita =['imagens/reidireita/Rei Direita Andando 1.png', 'imagens/reidireita/Rei Direita Andando 2.png']
reiequerda =['imagens/reiesquerda/Rei Esquerda Andando 1.png', 'imagens/reiesquerda/Rei Esquerda Andando 2.png']
reicima = ['imagens/reicima/reicimaandando 1.png', 'imagens/reicima/reicimaandando2.png']
reibaixo = ['imagens/reibaixo/reibaixoandando1.png', 'imagens/reibaixo/reibaixo andando2.png']
rei = pygame.image.load('imagens/reidireita/Rei Baixo Parado.png').convert_alpha()

sabio = pygame.image.load('imagens/sabioParado.png').convert_alpha()#largura23 altura31

cena1 = pygame.image.load('imagens/cenarios/casainterior.png') #posiperso x260,y560
cena2 = pygame.image.load('imagens/cenarios/primeiracena.png') #posiperso x635,y330
cena3 = pygame.image.load('imagens/cenarios/entrada_castelo.png') #posiperso x390 y560
cena4 = pygame.image.load('imagens/cenarios/interiorcast1.png') #posiperso x395 y550
intro = pygame.image.load('imagens/cenarios/intro.png')
gameover = pygame.image.load('imagens/cenarios/gameover.png')
end = pygame.image.load('imagens/cenarios/orockfinal.png')
espada = pygame.image.load('imagens/Espada.png').convert_alpha()
bgseta = pygame.image.load("imagens/seta2.png")
bgmenu = pygame.image.load("imagens/cenarios/ORockMenu.png").convert()
espada = pygame.image.load('imagens/Espada.png')
chave = pygame.image.load('imagens/Chave.png')

##dialogos##
font = pygame.font.SysFont("Arial", 20, bold=1)
textx = 150
texty = 200
txtOx = 370
txtOy = 400

andarmdk = -1
andar = -1
andarei = -1

def walk():
    global andar
    andar += 1
    if andar < 2:
        return andar
    else:
        andar = 0
        return andar


def walkmdk():
    global andarmdk
    andarmdk += 1
    if andarmdk < 2:
        return andarmdk
    else:
        andarmdk = 0
        return andarmdk


def walkrei():
    global andarei
    andarei += 1
    if andarei < 2:
        return andarei
    else:
        andarei = 0
        return andarei


##FUNCAOAREAareasdefinidasemcadaloop
def area(topx, topy, rightx, righty):
    global x;global y
    #pygame.draw.rect(janela, branco, [topx, topy, rightx-topx, righty-topy], 2)
    if x == topx and topy <= y <= righty:
        x -= 5
    if y == righty and topx <= x <= rightx:
        y += 5
    if x == rightx and topy <= y <= righty:
        x += 5
    if y == topy and topx <= x <= rightx:
        y -= 5
    return


if tela == 0:
    pygame.mixer.music.load('sons/temajogo.mpeg')
    pygame.mixer.music.play(-1)
bgsetax = 250
bgsetay = 433
while tela == 0:

    ##Saida##
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    janela.blit(bgmenu, (0, 0))
    janela.blit(bgseta, pygame.rect.Rect(bgsetax, bgsetay, 0, 0))
    pygame.display.update()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]:
        bgsetay = 490
    if pressed[pygame.K_UP]:
        bgsetay = 433
        bgmenu = pygame.image.load("imagens/cenarios/ORockMenu.png").convert()
        pygame.display.update()
    if pressed[pygame.K_RETURN]:
        bgmenu = pygame.image.load("imagens/cenarios/ORockMenu.png").convert()
        pygame.display.update()
        if bgsetay == 433 and pressed[pygame.K_RETURN]:
            tela = 1
            pygame.time.delay(70)
        if bgsetay == 490 and pressed[pygame.K_RETURN]:
            bgmenu = pygame.image.load("imagens/cenarios/Créditos.png").convert()
            pygame.display.update()
    pygame.time.delay(70)

while tela == 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    janela.blit(intro, (0, 0))
    pygame.display.update()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_SPACE]:
        tela = 2

contiten = 0
while tela == 2:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    pygame.display.update()
    janela.blit(cena1, (0, 0))
    
    #variaveisitem
    itens = []
    titem = ', '.join(itens)
    textitems = font.render('Itens: ' + titem, 1, branco)

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP] :
        x += 5
        loadperson = pygame.image.load(personright[walk()]).convert_alpha()
    if pressed[pygame.K_DOWN]:
        y += 5
        loadperson = pygame.image.load(persondown[walk()]).convert_alpha()
    if pressed[pygame.K_LEFT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
        x -= 5
        loadperson = pygame.image.load(personleft[walk()]).convert_alpha()
    if pressed[pygame.K_UP]:
        y -= 5
        loadperson = pygame.image.load(personup[walk()]).convert_alpha()
    janela.blit(loadperson, pygame.rect.Rect(x, y, 0, 0))
    janela.blit(sabio, (417, 345))
    if x == 415 and y == 375:
        text = font.render('Você e O-rock ?, General Modock esta la fora a sua procura', True, amarelo)
        janela.blit(text, (textx - 30, 200))
        text1 = font.render('Seu destino e derrotar o Rei tibério e trazer a Paz para o nosso reino', True, amarelo)
        janela.blit(text1, (textx - 75, texty + 20))
        text2 = font.render('Pressione enter para adicionar espada', True, amarelo)
        janela.blit(text2, (textx + 78, texty + 40))
        txt3 = font.render('Obrigado Sábio !!!', True, branco)
        janela.blit(txt3, (txtOx - 30, txtOy))
    if pressed[pygame.K_RETURN] and x == 415 and y == 375:
        contiten += 2
    if contiten == 0:
        janela.blit(textitems, (10, 20))
    if contiten > 0:
        item = 'Espada'
        itens.append(item)
        titem = ', '.join(itens)
        textitems = font.render('Itens: ', 1, branco)
        janela.blit(textitems, (10, 20))
        janela.blit(espada, (70, 20))
        pygame.display.update()
    print(itens)

    #trocadecenario
    if 'Espada' in itens and y > 560:
        tela = 3
    pygame.display.update()
    pygame.time.delay(70)

    #PadrãoTravasBordas
    if x < 1:
        x = 1
    if y < 1:
        y = 1
    if x > (width - 30):
        x = (width - 30)
    if y > (heigth - 30):
        y = (heigth - 30)

    ##Areas Travadas##
    area(455, 330, 495, 565)#parededireitasabio
    area(255, 260, 495, 325)#paredecimasabio
    area(285, 545, 500, 570)#paredefrentesabio
    area(280, 395, 390, 490)#personagens
    area(160, 340, 200, 570)
    area(195, 280, 305, 435)
    area(155, 545, 230, 575)
    area(395, 345, 435, 370)#posiçãodosabio
    print(f'x= {x}, y ={y}')

class projectile(object):
    def __init__(self, x, y, radius, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.velocidade = 10 * facing

    def draw(self, janela):
        janela.blit(espada, (self.x, self.y))
        pygame.display.update()


x = 635
y = 350
mdkx = 150
mdky = 500
cimay = 300
cimax = 100
baixox = 150
baixoy = 500
contiten = 0
bullets = []
visivel = ['modock']
while tela == 3:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    janela.blit(cena2, (0, 0))

    #itens
    itens = ['Espada']
    titem = ', '.join(itens)
    textitems = font.render('Itens: ', 1, branco)
    janela.blit(textitems, (10, 20))
    janela.blit(espada, (70, 20))

    #caixadedano
    caixadedano = (x, y, 23, 30)
    #pygame.draw.rect(janela, branco, (caixadedano), 2)
    caixadedanomdk = (mdkx, mdky, 23, 30)
    #pygame.draw.rect(janela, branco, (caixadedanomdk), 2)

    ##movimentodopersonagem
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
        x += 5
        loadperson = pygame.image.load(personright[walk()]).convert_alpha()
    if pressed[pygame.K_DOWN]:
        y += 5
        loadperson = pygame.image.load(persondown[walk()]).convert_alpha()
    if pressed[pygame.K_LEFT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
        x -= 5
        loadperson = pygame.image.load(personleft[walk()]).convert_alpha()
    if pressed[pygame.K_UP]:
        y -= 5
        loadperson = pygame.image.load(personup[walk()]).convert_alpha()
    janela.blit(loadperson, pygame.rect.Rect(x, y, 0, 0))

    #moviemntodoinimigo
    if 'modock' in visivel:
        if mdky > cimay and mdkx == baixox:
            mdky -= 5
            modock = pygame.image.load(modockcima[walkmdk()]).convert_alpha()
        elif mdky == cimay and mdkx > cimax:
            mdkx -= 5
            modock = pygame.image.load(modockesquerda[walkmdk()]).convert_alpha()
        elif mdky <= baixoy and mdkx < baixox:
            mdky += 5
            modock = pygame.image.load(modockbaixo[walkmdk()]).convert_alpha()
        elif mdky > baixoy and mdkx >= cimax:
            modock = pygame.image.load(modockdireita[walkmdk()]).convert_alpha()
            mdkx += 5

    #life
    if 'modock' in visivel:
        janela.blit(modock, pygame.rect.Rect(mdkx, mdky, 0, 0))
        pygame.draw.rect(janela, vermelho, [mdkx - 10, mdky - 10, 50, 2], 4)
        pygame.draw.rect(janela, verde, [mdkx - 10, mdky - 10, mdklife, 2], 4)
        if mdklife <= 0:
            visivel.remove('modock')
    if 'modock' not in visivel:
        item = 'Chave'
        itens.append(item)
        titem = ', '.join(itens)
        textitems = font.render('Itens: ', 1, branco)
        janela.blit(textitems, (10, 20))
        janela.blit(espada, (70, 20))
        janela.blit(chave, (100, 20))
        print(itens)
    pygame.time.delay(70)


    #funçõesdetiroedano
    if pressed[pygame.K_SPACE]:
        if x > 400:
            facing = -1
        if len(bullets) < 5:
            facing = -1
            bullets.append(projectile(x, y, -1, facing))
    for bullet in bullets:
        bullet.draw(janela)

    #limitesdotiro
    for bullet in bullets:
        if bullet.y - bullet.radius < caixadedanomdk[1] + caixadedanomdk [3] and bullet.y - bullet.radius > caixadedanomdk[1]:
            if bullet.x + bullet.radius > caixadedanomdk[0] and bullet.x - bullet.radius < caixadedanomdk[0] + caixadedanomdk[2]:
                bullets.pop(bullets.index((bullet)))
                mdklife -= 5
        if bullet.x < 800 and bullet.x > 0:
            bullet.x += bullet.velocidade
        else:
            bullets.pop(bullets.index(bullet))
        pygame.display.update()

    #mudancadecenario
    if 'espada' and 'Chave' in itens and x < 31:
        tela = 4

    #PadrãoTravasBordas
    if x < 1:
        x = 1
    if y < 1:
        y = 1
    if x > (width - 30):
        x = (width - 30)
    if y > (heigth - 30):
        y = (heigth - 30)

    #AreasTravadas
    area(175, 450, 330,575)#partebaixario
    area(170, 1, 325, 390) #partealtario
    area(475, 1, 770, 340)#casa
    area(295, -4, 430, 145)#plantalateralcasa
    area(425, 520, 775, 570)#plantafrenteacasa
    area(0, 0, 55, 395)#floresta
    area(420, -4, 470, 280) #partecasa
    #(11, 445, 61, 510)#arvore
    area(0, 440, 75, 575)#florestabaixo
    print(f'x= {x}, y ={y}')


x = 390
y = 560
while tela == 4:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    janela.blit(cena3, (0, 0))
    textitems = font.render('Itens: ', 1, branco)
    janela.blit(textitems, (10, 20))
    janela.blit(espada, (70, 20))

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
        x += 5
        loadperson = pygame.image.load(personright[walk()]).convert_alpha()
    if pressed[pygame.K_DOWN]:
        y += 5
        loadperson = pygame.image.load(persondown[walk()]).convert_alpha()
    if pressed[pygame.K_LEFT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
        x -= 5
        loadperson = pygame.image.load(personleft[walk()]).convert_alpha()
    if pressed[pygame.K_UP]:
        y -= 5
        loadperson = pygame.image.load(personup[walk()]).convert_alpha()
    janela.blit(loadperson, pygame.rect.Rect(x, y, 0, 0))
    pygame.time.delay(70)
    if y <= 370:
        tela = 5

    #PadrãoTravasBordas
    if x < 1:
        x = 1
    if y < 1:
        y = 1
    if x > (width - 30):
        x = (width - 30)
    if y > (heigth - 30):
        y = (heigth - 30)

    #AreasTravadas
    #area(mdkx, mdky, 25, 30)#modock
    area(285, 440, 345, 575)#ponte
    area(430, 445, 500, 570)#pontedireita
    area(250, 329, 305, 460)#casteloesuqerda
    area(475, 310, 520, 440)#castelodireita
    area(410, 305, 470, 375)#portadocastelodireita
    area(300, 295, 370, 380)#portadocasteloesuqerda
    area(315, 275, 420, 360)#portadocastelocima
    print(f'x= {x}, y ={y}')

##SOMs
if tela == 5:
    pygame.mixer.music.load('sons/temaluta.mpeg')
    pygame.mixer.music.play(0)

reix = 390
reiy = 315
reicimay = 320
reicimax = 305
reibaixox = 505
reibaixoy = 495
andarei = -1
contrei = 0
bulletsrei = []
visivel = ['rei','loadperson']
facing = 1
while tela == 5:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
    janela.blit(cena4, (0, 0))
    textitems = font.render('Itens: ', 1, branco)
    janela.blit(textitems, (10, 20))
    janela.blit(espada, (70, 20))
    # caixadedano
    caixadedano = (x, y, 23, 30)
    # pygame.draw.rect(janela, branco, (caixadedano), 2)
    caixadedanorei = (reix, reiy, 23, 30)
    # pygame.draw.rect(janela, branco, (caixadedanorei), 2)

    pressed = pygame.key.get_pressed()
    if 'loadperson' in visivel:
        if lifeorock <= 0:
            visivel.remove('loadperson')
            tela = 7
        if pressed[pygame.K_RIGHT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
            x += 5
            loadperson = pygame.image.load(personright[walk()]).convert_alpha()
        if pressed[pygame.K_DOWN]:
            y += 5
            loadperson = pygame.image.load(persondown[walk()]).convert_alpha()
        if pressed[pygame.K_LEFT] and not pressed[pygame.K_DOWN] and not pressed[pygame.K_UP]:
            x -= 5
            loadperson = pygame.image.load(personleft[walk()]).convert_alpha()
        if pressed[pygame.K_UP]:
            y -= 5
            loadperson = pygame.image.load(personup[walk()]).convert_alpha()
        janela.blit(loadperson, pygame.rect.Rect(x, y, 0, 0))
        pygame.draw.rect(janela, vermelho, [x - 10, y - 10, 50, 2], 4)
        pygame.draw.rect(janela, verde, [x - 10, y - 10, lifeorock, 2], 4)

        # funçõesdetiroedano
        if pressed[pygame.K_SPACE]:
            if x > 0:
                facing = -1
            if len(bullets) < 5:
                bullets.append(projectile(x, y, 0, facing))
        for bullet in bullets:
            bullet.draw(janela)

        # limitesdotiro
        for bullet in bullets:
            if bullet.y - bullet.radius < caixadedanorei[1] + caixadedanorei[3] and bullet.y - bullet.radius > caixadedanorei[1]:
                if bullet.x + bullet.radius > caixadedanorei[0] and bullet.x - bullet.radius < caixadedanorei[0] + \
                        caixadedanorei[2]:
                    bullets.pop(bullets.index(bullet))
                    reilife -= 5
            if bullet.x < 560 and bullet.x > 180:
                bullet.x += bullet.velocidade
            else:
                bullets.pop(bullets.index(bullet))
            pygame.display.update()

    if 'rei' in visivel:
        if pressed[pygame.K_RETURN]:
            contrei += 2
        if contrei == 0:
            janela.blit(rei, (390, 315))
            pygame.draw.rect(janela, vermelho, [reix - 10, reiy - 10, 50, 2], 4)
            life = pygame.draw.rect(janela, verde, [reix - 10, reiy - 10, reilife, 2], 4)
            if x == 390 and y == 345:
                txt6 = font.render('Quem e você ? ', True, amarelo)
                janela.blit(txt6, (335, 230))
                txt7 = font.render('Como Você entrou aqui ?', True, amarelo)
                janela.blit(txt7, (290, 250))
                txt8 = font.render('Meu nome é O-ROCK...', True, branco)
                janela.blit(txt8, (280, 380))
                txt9 = font.render('E vim por um fim no seu reinado Tirano ', True, branco)
                janela.blit(txt9, (195, 400))
                txt10 = font.render('<>Pressione enter para continuar<>', True, branco)
                janela.blit(txt10, (220, 420))
            pygame.display.update()

        #funçãoreiandar
        if contrei > 0:
            if reiy > reicimay and reix == reibaixox:
                reiy -= 5
                rei = pygame.image.load(reicima[walkrei()]).convert_alpha()
            elif reiy == reicimay and reix > reicimax:
                reix -= 5
                rei = pygame.image.load(reiequerda[walkrei()]).convert_alpha()
            elif reiy <= reibaixoy and reix < reibaixox:
                reiy += 5
                rei = pygame.image.load(reibaixo[walkrei()]).convert_alpha()
            elif reiy > reibaixoy and reix >= reicimax:
                rei = pygame.image.load(reidireita[walkrei()]).convert_alpha()
                reix += 5

            #liferei
            janela.blit(rei, pygame.rect.Rect(reix, reiy, 0, 0))
            pygame.draw.rect(janela, vermelho, [reix - 10, reiy - 10, 50, 2], 4)
            life = pygame.draw.rect(janela, verde, [reix - 10, reiy - 10, reilife, 2], 4)
            pygame.display.update()

            #ataquerei
            for bulletr in bulletsrei:
                bulletr.draw(janela)
            if randint(0, 5) == 1:
                if reix == 305:
                    facing = 1
                elif reix == 505:
                    facing = -1
                if len(bulletsrei) < 20:
                    bulletsrei.append(projectile(reix, reiy, 0, facing))
            pygame.display.update()
            for bulletr in bulletsrei:
                bulletr.draw(janela)
                if bulletr.y - bulletr.radius < caixadedano[1] + caixadedano[3] and bulletr.y - bulletr.radius > caixadedano[1]:
                    if bulletr.x + bulletr.radius > caixadedano[0] and bulletr.x - bulletr.radius < caixadedano[0] + caixadedano[2]:
                        bulletsrei.pop(bulletsrei.index(bulletr))
                        lifeorock -= 10
                if bulletr.x < 560 and bulletr.x > 180:
                    bulletr.x += bulletr.velocidade
                else:
                    bulletsrei.pop(bulletsrei.index(bulletr))
            pygame.display.update()
        if reilife <= 0:
            visivel.remove('rei')
            tela = 6

    #PadrãoTravasBordas
    if x < 1:
        x = 1
    if y < 1:
        y = 1
    if x > (width - 30):
        x = (width - 30)
    if y > (heigth - 30):
        y = (heigth - 30)
    #AreasTravadas
    area(530, 160, 595, 570)  #lateraldireita
    area(175, 150, 220, 575)  #lateralesquerda
    area(205, 115, 600, 210)  #paredecima
    area(200, 300, 300, 365)  #paredemaioresquerda
    area(220, 505, 365, 575)  #paredeesquerda
    area(430, 505, 545, 575)  #portadocastelocima
    area(360, 250, 430, 295)  #estatua
    area(330, 355, 360, 385)  #vaso1
    area(435, 355, 460, 380)  #vaso2
    area(435, 405, 460, 430)  #vaso3
    area(430, 450, 460, 475)  #vaso4
    area(330, 410, 355, 430)  #vaso5
    area(330, 455, 355, 480)  #vaso6
    print(f'x= {x}, y ={y}')
    pygame.display.update()
    pygame.time.delay(70)

if tela == 6 or tela == 7:
    pygame.mixer.music.load('sons/final.mpeg')
    pygame.mixer.music.play(0)
while tela == 6:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()

    janela.blit(end, (0, 0))
    pygame.display.update()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RETURN]:
        tela = 7

while tela == 7:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()

    janela.blit(gameover, (0, 0))
    pygame.display.update()