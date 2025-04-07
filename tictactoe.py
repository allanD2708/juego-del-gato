import pygame

pygame.init()
screen = pygame.display.set_mode((450,450))
pygame.display.set_caption("Gato")


fondo = pygame.image.load('static/fondo.png')
circulo = pygame.image.load('static/circle.png')
equis = pygame.image.load('static/x.png')
win = pygame.image.load('static/Game_Over.jpg')

fondo = pygame.transform.scale(fondo,(450,450))
circulo = pygame.transform.scale(circulo,(125,125))
equis = pygame.transform.scale(equis,(125,125))
win = pygame.transform.scale(win,(450,450))

coor = [[(40,50),(165,50),(290,50)],
        [(40,175),(165,175),(290,175)],
        [(40,300),(165,300),(290,300)]]

tablero = [['','',''],
           ['','',''],
           ['','','']]

turno = 'X'
game_over = False
clock = pygame.time.Clock()




#---------------------------------------------------------------------------------
# Cargar la imagen del botón de reinicio
boton_reiniciar = pygame.image.load('static/start.png')
boton_reiniciar = pygame.transform.scale(boton_reiniciar, (150, 50))  # Ajustar tamaño

def fin():
    """Muestra la pantalla de victoria y permite reiniciar o cerrar."""
    screen.blit(win, (0, 0))
    screen.blit(boton_reiniciar, (150, 350))  # Dibujar el botón en la pantalla
    pygame.display.flip()  # Actualizar la pantalla

    esperando_accion = True
    while esperando_accion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                esperando_accion = False  # Salir del bucle y cerrar el programa
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = event.pos
                # Detectar si el clic está dentro del botón de reinicio
                if 150 <= mouseX <= 300 and 350 <= mouseY <= 400:
                    reiniciar_juego()  # Llamar a la función para reiniciar el juego
                    esperando_accion = False  # Salir de este bucle para volver al juego

def reiniciar_juego():
    """Reinicia el estado del juego para comenzar de nuevo."""
    global tablero, turno, game_over
    tablero = [['', '', ''], ['', '', ''], ['', '', '']]  # Vaciar el tablero
    turno = 'X'  # Reiniciar el turno al jugador 'X'
    game_over = False  # Permitir que el bucle principal corra de nuevo

#---------------------------------------------------------------------------------------------


def graficar_board():
    screen.blit(fondo,(0,0))
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == 'X':
                dibujar_x(fila,col)
            elif tablero[fila][col] == '0':
                dibujar_0(fila,col)


def dibujar_x(fila,col):
      screen.blit(equis, coor[fila][col])
def dibujar_0(fila,col):
      screen.blit(circulo, coor[fila][col])


def ganador():
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != '':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != '':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
            return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
            return True  
    return False
    




while not game_over:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = event.pos
            if (mouseX >= 40 and mouseX < 415) and (mouseY >= 50 and mouseY < 425):
                fila = (mouseY - 50) // 125
                col = (mouseX - 40) // 125
                if tablero[fila][col] == '':
                    tablero[fila][col] = turno
                    end_game = ganador()
                    if end_game:
                         print(f"El jugador {turno} ha ganado!!")
                         game_over = True
                         fin()
                    turno = '0' if turno == 'X' else 'X'
          
    graficar_board()
    pygame.display.update()
pygame.quit()


