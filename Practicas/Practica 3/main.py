import pygame
import numpy as np
from algoritmos_evaluacion import A_star, distancia_manhattan
import time

# Algunas variables:

# Tamaño de cada cuadricula
grid_size = 20*2
n = 15 # Tamaño del tablero n x n
cadencia_entre_turnos = 0.3 # segundos 

grid_width, grid_height = n * grid_size, n * grid_size
width = grid_width + 300 # Para tener instrucciones / botones / informacion sobre el juego
height = grid_height
botoien_dist = height // 10

# Colores:
WHITE = (238,238,210)
BLACK = (186,202,68)
GRID_COLOR = (200, 200, 200) # Karratuen arteko kolorea eta pantaila atzeko kolorea
TEXT_COLOR = (0,0,0)
BUTTON_COLOR = (200, 200, 200)
GREEN = (0, 255, 0)
RED =(255,0,0)










def es_posible(PillaPilla,posicion):
    x,y = posicion
    return 0 <= x < n and 0 <= y < n and PillaPilla.mapa[x][y] != 1

mapa_default = np.array([[]],dtype = int)
class PillaPilla:
    """
    Clase para guardar las partidas. Las diferentes partidas se guardarán aquí y 
    """

    def __init__(self,modo_de_juego,funcion_evaluacion,profundidad_minmax,mapa,funcion_evaluacion_2 = None,imax = 30):
        # Constantes durante la ejecucion: 
        self.funcion_evaluacion = funcion_evaluacion # eval de perseguidor (solo influye si es maquina vs maquina)
        self.funcion_evaluacion_2 = funcion_evaluacion_2 # eval de perseguido (solo influye si es maquina vs maquina)
        self.profundidad_minmax = profundidad_minmax # Profundidad de las ramas en las que se evaluara el juego
        self.mapa = mapa # Tiene que ser un array de NUMPY
        self.n = len(self.mapa)
        self.evolucion_partida = [] # Aquí guardaremos el historial de la partida
        self.modo_de_juego = modo_de_juego # Otras opciones: "perseguido", "maquina vs maquina"
        self.imax = imax

        if self.modo_de_juego != "maquina vs maquina":
            self.funcion_evaluacion_2 = self.funcion_evaluacion

        # Variables durante la ejecucion:
        self.juego_terminado = False
        self.iteracion = 0
        self.posicion_perseguidor = np.array((0,0)) # Tiene que ser un array de NUMPY
        self.posicion_perseguido = np.array((self.n - 1, self.n - 1)) # Tiene que ser un array de NUMPY
        self.turno = "perseguidor" # Siempre empieza el perseguidor a jugar

    def __repr__(self):
        x0,y0 = self.posicion_perseguidor
        x1,y1 = self.posicion_perseguido
        a = self.mapa[x0][y0]
        b = self.mapa[x1][y1]
        self.mapa[x0][y0] = 2
        self.mapa[x1][y1] = 3
        m = self.mapa.copy()
        self.mapa[x0][y0] = a
        self.mapa[x1][y1] = b
        return m.__repr__()
    
    def conseguir_posiciones_iniciales(self):
        """
        Al ejecutarse, se abre pygame y pide al jugador que elija las posiciones iniciales 
        """
        pass

    def pedir_movimiento(self):
        """
        Esta función pedira un input al jugador (persona real) y 
        """    

    def minmax(self, turno_perseguidor, profundidad):
        """
        Sirve para mover a la maquina a la siguiente casilla utilizando el algoritmo 
        minmax y la función de evaluación. Tiene como inputs: 
        - Cuál es el turno de la máquina: (turno_perseguidor = True / False)
        - profundidad: nivel de profundidad recursivo en el que estamos
        """
        if (profundidad == 0 or tuple(self.posicion_perseguido) == tuple(self.posicion_perseguidor)):
            return self.funcion_evaluacion(self)
        
        elif turno_perseguidor: # turno_perseguidor == nodo min (tiene que atrapar)
            min = float("inf")
            caminos = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in caminos:
                if es_posible(self, self.posicion_perseguidor + np.array((dx,dy))):
                    turno_anterior = self.posicion_perseguidor
                    self.posicion_perseguidor = self.posicion_perseguidor + np.array((dx,dy))
                    valor = self.minmax(turno_perseguidor = False, profundidad=profundidad-1)
                    # print("--------------------")
                    # print(f"Turno min, valor = {valor}, profundidad = {profundidad}")
                    # print(self)
                    # print("--------------------")
                    if valor < min:
                        min = valor
                        if profundidad == self.profundidad_minmax:
                            mejor_posicion = self.posicion_perseguidor
                    self.posicion_perseguidor = turno_anterior
            if profundidad == self.profundidad_minmax:
                self.posicion_perseguidor = mejor_posicion
                self.turno = "perseguido"    
            else:
                return min
            
        elif not turno_perseguidor: # not turno_perseguidor == nodo max (tiene que huir)
            max = float("-inf")
            caminos = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in caminos:
                if es_posible(self, self.posicion_perseguido + np.array((dx,dy))):
                    turno_anterior = self.posicion_perseguido
                    self.posicion_perseguido = self.posicion_perseguido + np.array((dx,dy))
                    valor = self.minmax(turno_perseguidor = True, profundidad=profundidad-1)
                    # print("--------------------")
                    # print(f"Turno max, valor = {valor}, profundidad = {profundidad}")
                    # print(self)
                    # print("--------------------") 
                    if valor > max:
                        max = valor
                        if profundidad == self.profundidad_minmax:
                            mejor_posicion = self.posicion_perseguido
                    self.posicion_perseguido = turno_anterior
            if profundidad == self.profundidad_minmax:
                self.posicion_perseguido = mejor_posicion
                print(self.turno)
                self.turno = "perseguidor"
            else:
                return max
    def siguiente_movimiento(self):
        """
        Aquí se hará el juego. Es decir, se moveran las posiciones de los jugadores en base al turno
        """
        if self.modo_de_juego == "perseguidor" and distancia_manhattan(self) != 1:
            if self.turno == "perseguidor": # Turno del jugador (se gestiona directamente en pygame)
                pass
            else:
                time.sleep(cadencia_entre_turnos)
                self.minmax(turno_perseguidor = False,profundidad= self.profundidad_minmax)
                self.turno = "perseguidor"



        elif self.modo_de_juego == "perseguido":
            pass
        elif self.modo_de_juego == "maquina vs maquina":
            pass
        elif distancia_manhattan(self) == 1:
            self.juego_terminado = True
            
class Botoia:
    def __init__(self, x, y, width, height, color, text, font_size = 24):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, font_size)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

def dibujar_cuadricula(pilla_pilla,screen):
    screen.fill(WHITE)
    for i in range(pilla_pilla.n):
        for j in range(pilla_pilla.n):
            if (i,j) != tuple(pilla_pilla.posicion_perseguidor) and (i,j) != tuple(pilla_pilla.posicion_perseguido): 
                balioa = pilla_pilla.mapa[i][j]
                if balioa == 0: # 0 será que la cuadrícula está vacía
                    pygame.draw.rect(screen, WHITE, (j * grid_size, i * grid_size, grid_size, grid_size))
                elif balioa == 1:
                    pygame.draw.rect(screen, BLACK, (j * grid_size, i * grid_size, grid_size, grid_size))
                pygame.draw.rect(screen, GRID_COLOR, (j * grid_size, i * grid_size, grid_size, grid_size), 1)
            
    (i,j) = pilla_pilla.posicion_perseguidor # Perseguidor de color ROJO
    pygame.draw.rect(screen, RED, (j * grid_size, i * grid_size, grid_size, grid_size))
    pygame.draw.rect(screen, GRID_COLOR, (j * grid_size, i * grid_size, grid_size, grid_size), 1)

    (i,j) = pilla_pilla.posicion_perseguido # Perseguido de color VERDE
    pygame.draw.rect(screen, GREEN, (j * grid_size, i * grid_size, grid_size, grid_size))
    pygame.draw.rect(screen, GRID_COLOR, (j * grid_size, i * grid_size, grid_size, grid_size), 1)
                

def menu():
    # Pygame hasi
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pilla-Pilla")

    # Irudiak:
    irudia = pygame.image.load("imagen_menu.png") 
    irudia = pygame.transform.scale(irudia, (botoien_dist * 4, botoien_dist*4))
    irudia_rect = irudia.get_rect()
    irudia_rect.center = (width // 2, height // 2 - botoien_dist* 1.5)

    # Beharrezko aldagaia
    running = True

    # Textuak idazteko beharrezkoa:
    izenburua = pygame.font.Font(None, 80)

    # Botoia:
    botoia_mapa_sortu = Botoia(width//2-350//2, height - 50 - botoien_dist * 3, 350, 40, BUTTON_COLOR, "Crear mapa del juego")
    botoia_partida_berria = Botoia(width//2-350//2, height - 50 - botoien_dist * 2 , 350, 40, BUTTON_COLOR, "Nueva partida")
    botoia_partida_kargatu = Botoia(width//2-350//2, height - 50 - botoien_dist , 350, 40, BUTTON_COLOR, "Cargar partida")
    botoia_irten = Botoia(width//2-350//2, height - 50, 350, 40, BUTTON_COLOR, "Salir del juego")

    # Loop orokorra
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # Exekutatzeaz bukatzeko
                running = False
                zer_egin = "terminar"
            elif event.type == pygame.MOUSEBUTTONDOWN: # Xaguaren botoiren bat sakatzen bada
                if event.button == 1: # Ezkerreko botoia sakatzen bada
                    if botoia_mapa_sortu.rect.collidepoint(event.pos):
                        running = False
                        zer_egin = "crear mapa"
                    elif botoia_partida_berria.rect.collidepoint(event.pos):
                        running = False
                        zer_egin = "nueva partida"
                    elif botoia_irten.rect.collidepoint(event.pos):
                        running = False
                        zer_egin = "terminar"
                    elif botoia_partida_kargatu.rect.collidepoint(event.pos):
                        running = False
                        zer_egin = "juego"

        # while buklearen amaieran, pantaila marraztu, textua idatzi eta aktualizatzeko
        screen.fill(WHITE)
        screen.blit(izenburua.render("Pilla - Pilla", True, BLACK),(width//2 - 145, 15))
        botoia_mapa_sortu.draw(screen)
        botoia_partida_berria.draw(screen)
        botoia_irten.draw(screen)
        botoia_partida_kargatu.draw(screen)
        screen.blit(irudia, irudia_rect)
        pygame.display.flip()

    return zer_egin


def juego(pilla_pilla):
    """
    Aquí se visualiza y ejecuta el juego
    """
    # Pygame hasi
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jugando")

    # Beharrezko hainbat aldagai
    running = True

    # Textuak idazteko beharrezkoa:
    izenburua = pygame.font.Font(None, 30)
    info_turno = pygame.font.Font(None, 30)
    instrukzioak = pygame.font.Font(None,20)

    # Botoia:
    boton_guardar = Botoia(width - 230, 325, 170, 40, BUTTON_COLOR, "Next example")
    botoia_itzuli_menura = Botoia(width - 230, height - 50, 170, 40, BUTTON_COLOR, "Go to menu")

    boton_arriba = Botoia(grid_width + (width - grid_width) // 2 - 60 // 2, height - 4 * botoien_dist, 60, 60, BUTTON_COLOR, "^")
    boton_abajo = Botoia(grid_width + (width - grid_width) // 2 - 60 // 2, height - 2 * botoien_dist, 60, 60, BUTTON_COLOR, "v")
    boton_izquierda = Botoia(grid_width + (width - grid_width) // 2 - 60 // 2 - botoien_dist , height - 3 * botoien_dist, 60, 60, BUTTON_COLOR, "<")
    boton_derecha = Botoia(grid_width + (width - grid_width) // 2 - 60 // 2 + botoien_dist , height - 3 * botoien_dist, 60, 60, BUTTON_COLOR, ">")

    # Loop orokorra
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT: # Exekutatzeaz bukatzeko
                running = False
                zer_egin = "terminar"
            elif keys[pygame.K_RETURN]: # Enter botoia sakatzerakoan
                pass
            elif keys[pygame.K_UP] and pilla_pilla.turno == pilla_pilla.modo_de_juego:
                if pilla_pilla.turno == "perseguidor" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguidor + (-1,0)):
                    pilla_pilla.posicion_perseguidor = pilla_pilla.posicion_perseguidor + np.array((-1,0))
                    pilla_pilla.turno = "perseguido"
                elif pilla_pilla.turno == "perseguido" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguido + (-1,0)):
                    pilla_pilla.posicion_perseguido = pilla_pilla.posicion_perseguido + np.array((-1,0))
                    pilla_pilla.turno = "perseguidor"
            elif keys[pygame.K_DOWN] and pilla_pilla.turno == pilla_pilla.modo_de_juego:
                if pilla_pilla.turno == "perseguidor" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguidor + (1,0)):
                    pilla_pilla.posicion_perseguidor = pilla_pilla.posicion_perseguidor + np.array((1,0))
                    pilla_pilla.turno = "perseguido"
                elif pilla_pilla.turno == "perseguido" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguido + (1,0)):
                    pilla_pilla.posicion_perseguido = pilla_pilla.posicion_perseguido + np.array((1,0))
                    pilla_pilla.turno = "perseguidor"
            elif keys[pygame.K_RIGHT] and pilla_pilla.turno == pilla_pilla.modo_de_juego:
                if pilla_pilla.turno == "perseguidor" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguidor + (0,1)):
                    pilla_pilla.posicion_perseguidor = pilla_pilla.posicion_perseguidor + np.array((0,1))
                    pilla_pilla.turno = "perseguido"
                elif pilla_pilla.turno == "perseguido" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguido + (0,1)):
                    pilla_pilla.posicion_perseguido = pilla_pilla.posicion_perseguido + np.array((0,1))
                    pilla_pilla.turno = "perseguidor"

            elif  keys[pygame.K_LEFT] and pilla_pilla.turno == pilla_pilla.modo_de_juego:
                if pilla_pilla.turno == "perseguidor" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguidor + (0,-1)):
                    pilla_pilla.posicion_perseguidor = pilla_pilla.posicion_perseguidor + np.array((0,-1))
                    pilla_pilla.turno = "perseguido"
                elif pilla_pilla.turno == "perseguido" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguido + (0,-1)):
                    pilla_pilla.posicion_perseguido = pilla_pilla.posicion_perseguido + np.array((0,-1))
                    pilla_pilla.turno = "perseguidor"

            elif event.type == pygame.MOUSEBUTTONDOWN: # Xaguaren botoiren bat sakatzen bada
                if event.button == 1: # Ezkerreko botoia sakatzen bada
                    if botoia_itzuli_menura.rect.collidepoint(event.pos):
                        running = False
                        zer_egin = "menu"
                    if boton_arriba.rect.collidepoint(event.pos) and pilla_pilla.turno == pilla_pilla.modo_de_juego:
                        if pilla_pilla.turno == "perseguidor" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguidor + (-1,0)):
                            pilla_pilla.posicion_perseguidor = pilla_pilla.posicion_perseguidor + np.array((-1,0))
                            pilla_pilla.turno = "perseguido"
                        elif pilla_pilla.turno == "perseguido" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguido + (-1,0)):
                            pilla_pilla.posicion_perseguido = pilla_pilla.posicion_perseguido + np.array((-1,0))
                            pilla_pilla.turno = "perseguidor"
                    
                    if boton_abajo.rect.collidepoint(event.pos) and pilla_pilla.turno == pilla_pilla.modo_de_juego:
                        if pilla_pilla.turno == "perseguidor" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguidor + (1,0)):
                            pilla_pilla.posicion_perseguidor = pilla_pilla.posicion_perseguidor + np.array((1,0))
                            pilla_pilla.turno = "perseguido"
                        elif pilla_pilla.turno == "perseguido" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguido + (1,0)):
                            pilla_pilla.posicion_perseguido = pilla_pilla.posicion_perseguido + np.array((1,0))
                            pilla_pilla.turno = "perseguidor"
                    
                    if boton_derecha.rect.collidepoint(event.pos) and pilla_pilla.turno == pilla_pilla.modo_de_juego:
                        if pilla_pilla.turno == "perseguidor" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguidor + (0,1)):
                            pilla_pilla.posicion_perseguidor = pilla_pilla.posicion_perseguidor + np.array((0,1))
                            pilla_pilla.turno = "perseguido"
                        elif pilla_pilla.turno == "perseguido" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguido + (0,1)):
                            pilla_pilla.posicion_perseguido = pilla_pilla.posicion_perseguido + np.array((0,1))
                            pilla_pilla.turno = "perseguidor"

                    if boton_izquierda.rect.collidepoint(event.pos) and pilla_pilla.turno == pilla_pilla.modo_de_juego:
                        if pilla_pilla.turno == "perseguidor" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguidor + (0,-1)):
                            pilla_pilla.posicion_perseguidor = pilla_pilla.posicion_perseguidor + np.array((0,-1))
                            pilla_pilla.turno = "perseguido"
                        elif pilla_pilla.turno == "perseguido" and es_posible(pilla_pilla, pilla_pilla.posicion_perseguido + (0,-1)):
                            pilla_pilla.posicion_perseguido = pilla_pilla.posicion_perseguido + np.array((0,-1))
                            pilla_pilla.turno = "perseguidor"
                    

        # while buklearen amaieran, pantaila marraztu, textua idatzi eta aktualizatzeko
        dibujar_cuadricula(pilla_pilla,screen)

        screen.blit(izenburua.render("Jugando", True, TEXT_COLOR),(width - 295, 30))
        screen.blit(instrukzioak.render("Click enter to see the next example", True, TEXT_COLOR),(width - 295, 55))
        screen.blit(info_turno.render(f"Es el turno de: {pilla_pilla.turno}",True, RED if pilla_pilla.turno == "perseguidor" else GREEN),(width-295,70))
        screen.blit(info_turno.render(f"Tu eres: {pilla_pilla.modo_de_juego}",True, TEXT_COLOR),(width-295,90))
        botoia_itzuli_menura.draw(screen)
        boton_izquierda.draw(screen)
        boton_abajo.draw(screen)
        boton_derecha.draw(screen)
        boton_arriba.draw(screen)
        pygame.display.flip()
        pilla_pilla.siguiente_movimiento()
        
    return zer_egin


def main():
    que_hacer = "menu"
    pygame.init()

    while que_hacer != "terminar":

        if que_hacer == "menu":
            que_hacer = menu()

        elif que_hacer == "crear mapa":
            que_hacer = "menu"

        elif que_hacer == "nueva partida":
            que_hacer = "menu"
        
        elif que_hacer == "cargar partida":
            que_hacer = "menu"

        elif que_hacer == "juego":
            # mapa = np.array(
            #     [[0, 0, 0, 0, 0],
            #      [0, 1, 0, 1, 0],
            #      [0, 1, 1, 1, 0],
            #      [0, 0, 0, 0, 0],
            #      [0, 0, 1, 0, 0]
            #      ])

            mapa = np.array(
                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],

                 [0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
                 [0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                 
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

            )
            p1 = PillaPilla("perseguidor",distancia_manhattan,2,mapa)
            que_hacer = juego(p1)

    pygame.quit()








if __name__ == "__main__":
    main()