import graphics as gf  #trazer o arquivo da graphics
import random as rd 
import math as mt
rd.seed()

def foiNoBotao(botao, onde_cliquei):
    bt_x = botao.getP1().getX()
    bt_y = botao.getP1().getY()
    bt2_x = botao.getP2().getX()
    bt2_y = botao.getP2().getY()
    print(f'----> ({bt_x} {bt_y})({bt2_x} {bt2_y})')
    if onde_cliquei.getX() > bt_x and onde_cliquei.getX() < bt2_x and onde_cliquei.getY() > bt_y and onde_cliquei.getY() < bt2_y:
        return True
    else:
        return False

def abs(x):
    print(x)
    if x < 0:
        return x * -1
    return x

win = gf.GraphWin(  "Minha Janela"  , 400, 350)   #cria uma janela
c = gf.Circle(gf.Point(100, 150), 10)             #cria o ponto
c.setFill('red')
c.draw(win)                                       #fala em qual janela o ponto deve ser draw
cores = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'pink', 'purple', 'brown']

i = True
erro = 15
botao = gf.Rectangle(gf.Point(10, 10), gf.Point(190, 50))
botao.setFill('pink')
botao.draw(win)
onde_cliquei = gf.Point(0, 0)

while i != False:
    cliquei_antes = onde_cliquei
    print(onde_cliquei.getX(), onde_cliquei.getY())
    onde_cliquei = win.getMouse()
    if foiNoBotao(botao, onde_cliquei):
        botao.setFill('red')
        print('dentro do botao')
    else:
        botao.setFill('yellow')
        print('fora')
    print(onde_cliquei.getX(), onde_cliquei.getY())
    #onde_cliquei = win.getMouse()
    nova_bolinha = gf.Circle(onde_cliquei, 10)
    cor = rd.randint(0, len(cores) - 1)
    nova_bolinha.setFill(cores[cor])
    nova_bolinha.draw(win)
    onde_cliquei2 = cliquei_antes
    #onde_cliquei2 = win.getMouse()
    print(onde_cliquei2.getX(), onde_cliquei2.getY())
    dx = abs(onde_cliquei2.getX() - onde_cliquei.getX())
    dy = abs(onde_cliquei2.getY() - onde_cliquei.getY())
    d = round(mt.sqrt(dx * dx + dy * dy))
    print(d)
    if abs(onde_cliquei2.getX() - onde_cliquei.getX()) < erro and abs(onde_cliquei2.getY() - onde_cliquei.getY()) < erro:
        i = False
    else:
        nova_bolinha = gf.Circle(onde_cliquei2, 10)
        cor = rd.randint(0, len(cores) - 1)
        nova_bolinha.setFill(cores[cor])
        nova_bolinha.draw(win)