import graphics as gf  #trazer o arquivo da graphics
import random as rd 

win = gf.GraphWin(  "Minha Janela"  , 400, 350)   #cria uma janela
c = gf.Circle(gf.Point(100, 150), 10)             #cria o ponto
c.setFill('red')
c.draw(win)                                       #fala em qual janela o ponto deve ser draw
cores = ['red', 'blue', 'green', 'orange', 'yellow', 'black', 'pink']

#cont = 0
while True:
    onde_cliquei = win.getMouse()
    print(onde_cliquei.getX(), onde_cliquei.getY())
    nova_bolinha = gf.Circle(onde_cliquei, 10)
    cor = rd.randint(0, len(cores) - 1)
    nova_bolinha.setFill(cores[cor])
    '''cont += 1
    if cont == len(cores):
        cont = 0'''
    nova_bolinha.draw(win)