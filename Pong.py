import pygame, random
pygame.init()

NEGRO=(0, 0, 0)
ROJO=(255, 0, 0)
AZUL=(0, 0, 255)
PURPURA=(127, 0, 255)
GRIS=(128, 128, 128)
AZUL_AG_M=(102,205,170)
PLATEADO=(176,196,222)

tamaño=(800,600)
ancho_jugador=15
alto_jugador=90
pantalla=(pygame.display.set_mode(tamaño))
timer=pygame.time.Clock()

jugador1_x_coor=50
jugador1_y_coor=300-45
jugador1_x_speed=0
jugador1_y_speed=0

jugador2_x_coor=750-ancho_jugador
jugador2_y_coor=300-45
jugador2_x_speed=0
jugador2_y_speed=0

pelota_x=400
pelota_y=300
pelota_speed_x=4.5
pelota_speed_y=4.5

puntuacion_jugador1=00
puntuacion_jugador2=00

pygame.display.set_caption("Pong")

def iconos(nombre):
    icono=pygame.image.load(nombre)
    pygame.display.set_icon(icono)

iconos("raquetas.jpg")

fuente=pygame.font.SysFont("arial black",40)
color_texto=(AZUL_AG_M)

def texto(text, fuente, color_texto, x, y):
    img=fuente.render(text, True, color_texto)
    pantalla.blit(img, (x, y))

fuente_titulo=pygame.font.SysFont("serif",40)
color_texto_titulo=(PLATEADO)

def texto_titulo(text, fuente_titulo, color_texto_titulo, x, y):
    img=fuente.render(text, True, color_texto_titulo)
    pantalla.blit(img, (x, y))

introduccion=True
jugando=False
final=False
resultado=""

fondo=pygame.image.load("introd-fondo.png").convert()

#pantalla inicial
while introduccion:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_c:
                introduccion=False
                jugando=True
    pantalla.blit(fondo, [0, 0])
    texto_titulo("¡Bienvenid@s A Pong!", fuente, color_texto_titulo, 185, 80)
    texto_titulo("¿List@s Para Comenzar?", fuente, color_texto_titulo, 150, 250)
    texto_titulo("Presione 'c' Para Iniciar", fuente, color_texto_titulo, 140, 420)

    pygame.display.update()
    timer.tick(3)

    #juego
    while jugando==True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                jugando=False
            #presiona avanza
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    jugador1_y_speed=-3
                if event.key==pygame.K_s:
                    jugador1_y_speed=3
                if event.key==pygame.K_d:
                    jugador1_x_speed=3
                if event.key==pygame.K_a:
                    jugador1_x_speed=-3

                if event.key==pygame.K_UP:
                    jugador2_y_speed=-3
                if event.key==pygame.K_DOWN:
                    jugador2_y_speed=3
                if event.key==pygame.K_RIGHT:
                    jugador2_x_speed=3
                if event.key==pygame.K_LEFT:
                    jugador2_x_speed=-3
            #soltar frena
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    jugador1_y_speed=0
                if event.key==pygame.K_s:
                    jugador1_y_speed=0
                if event.key==pygame.K_d:
                    jugador1_x_speed=0
                if event.key==pygame.K_a:
                    jugador1_x_speed=0

                if event.key==pygame.K_UP:
                    jugador2_y_speed=0
                if event.key==pygame.K_DOWN:
                    jugador2_y_speed=0
                if event.key==pygame.K_RIGHT:
                    jugador2_x_speed=0
                if event.key==pygame.K_LEFT:
                    jugador2_x_speed=0
        #pelota rebota arriba y abajo
        if pelota_y>590 or pelota_y<10:
            pelota_speed_y*=-1
        #pelota sale lado derecho
        if pelota_x>800:
            pelota_x=400
            pelota_y=300
            pelota_speed_x*=-1
            pelota_speed_y*=-1
            puntuacion_jugador1+=1
        #pelota sale lado izquierdo
        if pelota_x<0:
            pelota_x=400
            pelota_y=300
            pelota_speed_x*=-1
            pelota_speed_y*=-1
            puntuacion_jugador2+=1

        #movimiento jugadores
        jugador1_y_coor+=jugador1_y_speed
        jugador1_x_coor+=jugador1_x_speed
        
        jugador2_x_coor+=jugador2_x_speed
        jugador2_y_coor+=jugador2_y_speed

        #movimiento pelota
        pelota_x+=pelota_speed_x
        pelota_y+=pelota_speed_y

        pantalla.fill(NEGRO)

        jugador1=pygame.draw.rect(pantalla, AZUL, (jugador1_x_coor, jugador1_y_coor, ancho_jugador, alto_jugador))
        jugador2=pygame.draw.rect(pantalla, ROJO, (jugador2_x_coor, jugador2_y_coor, ancho_jugador, alto_jugador))
        pelota=pygame.draw.circle(pantalla, PURPURA, (pelota_x, pelota_y), 10)

        for y in range(5,950,20):
            pygame.draw.rect(pantalla, GRIS, (395, y, 10, 10))

        #rebote jugadores arriba y abajo
        if(jugador1_y_coor>510 or jugador1_y_coor<0):
            jugador1_y_speed*=-1

        if(jugador2_y_coor>510 or jugador2_y_coor<0):
            jugador2_y_speed*=-1
        #rebote juagores extremos y centro
        if(jugador1_x_coor>380 or jugador1_x_coor<0):
            jugador1_x_speed*=-1

        if(jugador2_x_coor>790 or jugador2_x_coor<400):
            jugador2_x_speed*=-1

        #pelota cambia direccion al chocar jugadores
        if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
            pelota_speed_x*=-1

        #marcador
        texto(str(puntuacion_jugador1), fuente, color_texto, 250, 20)
        texto(str(puntuacion_jugador2), fuente, color_texto, 550, 20)

        #pantalla final- fin del juego
        if(puntuacion_jugador1==20 or puntuacion_jugador2==20):
            pelota_speed_x=0
            pelota_speed_y=0
            final=True
        if final==True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    quit()
            pantalla.blit(fondo, [0, 0])
            texto_titulo("Juego Terminado", fuente, color_texto_titulo, 210, 20)
            texto_titulo("¡Gracias Por Jugar!", fuente, color_texto_titulo, 194, 70)
            texto_titulo("El Ganador Es:", fuente, color_texto_titulo, 240, 260)
            if puntuacion_jugador1==20:
                resultado="Jugador 1"
                texto_titulo(str(resultado), fuente, AZUL, 290, 310)
            if puntuacion_jugador2==20:
                resultado="Jugador 2"
                texto_titulo(str(resultado), fuente, ROJO, 290, 310)
            texto_titulo("Presione 'esc' Para Cerrar", fuente, color_texto_titulo, 120, 470)

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    quit()
        pygame.display.flip()
        timer.tick(60)
pygame.quit()