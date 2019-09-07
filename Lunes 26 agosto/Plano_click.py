import pygame

NEGRO=[0,0,0]
VERDE=[0,255,0]
ROJO=[255,0,0]
AZUL=[0,0,255]
BLANCO = [255,255,255]
ANCHO = 600
ALTO = 400


def plano(p,origen):
    ox = origen[0]
    oy = origen[1]
    pygame.draw.line(pantalla,BLANCO,[ox,0],[ox,ALTO])
    pygame.draw.line(pantalla,BLANCO,[0,oy],[ANCHO,oy])
    pygame.display.flip()

def Cart_plano(pto,origen):
    x = pto[0]
    y = pto[1]
    xp = x + origen[0]
    yp = -y + origen[1]
    return [xp,yp]



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])

    pygame.display.flip()
    fin=False
    while not fin:
        pantalla.fill(NEGRO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                origen = event.pos
                v1 = Cart_plano([70,-80],origen)
                pygame.draw.line(pantalla,ROJO,origen,v1)
                plano(pantalla,origen)
                print(v1)
pygame.display.flip()
