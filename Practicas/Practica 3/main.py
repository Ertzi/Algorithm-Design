import pygame
import numpy as np
from algoritmos_evaluacion import A_star

# Algunas variables:

# Tamaño de cada cuadricula
grid_size = 30*5
n = 5 # Tamaño del tablero n x n

grid_width, grid_height = n * grid_size, n * grid_size
width = grid_width + 300 # Para tener instrucciones / botones / informacion sobre el juego
height = grid_height


# Colores:
WHITE = (238,238,210)
BLACK = (186,202,68)
GRID_COLOR = (200, 200, 200) # Karratuen arteko kolorea eta pantaila atzeko kolorea
TEXT_COLOR = (0,0,0)
BUTTON_COLOR = (200, 200, 200)
GREEN = (0, 255, 0)
RED =(255,0,0)












mapa_default = np.array([[]],dtype = int)
class PillaPilla:
    """
    Clase para guardar las partidas. Las diferentes partidas se guardarán aquí y 
    """

    def __init__(self,funcion_evaluacion,profundidad_minmax,mapa,funcion_evaluacion_2 = None):
        # Constantes durante la ejecucion: 
        self.funcion_evaluacion = funcion_evaluacion
        self.funcion_evaluacion_2 = funcion_evaluacion_2 # Para las partidas maquina vs maquina
        self.profundidad_minmax = profundidad_minmax # Profundidad de las ramas en las que se evaluara el juego
        self.mapa = mapa # Tiene que ser un array de NUMPY
        self.n = len(self.mapa)
        self.evolucion_partida = [] # Aquí guardaremos el historial de la partida

        # Variables durante la ejecucion:
        self.posicion_perseguidor = np.array((0,0)) # Tiene que ser un array de NUMPY
        self.posicion_perseguido = np.array((self.n - 1, self.n - 1)) # Tiene que ser un array de NUMPY
        self.turno = "Turno perseguidor" # Siempre empieza el perseguidor a jugar

    def conseguir_posiciones_iniciales(self):
        """
        Al ejecutarse, se abre pygame y pide al jugador que elija las posiciones iniciales 
        """
        pass

    def siguiente_mofimiento(self):
        """
        Aquí se hará el juego. Es decir, se moveran las posiciones de los jugadores en base al turno
        """
        if self.turno == "Turno perseguidor":
            pass
        else:
            pass
    
    def pedir_movimiento(self):
        """
        Esta función pedira un input al jugador (persona real) y 
        """

    def minmax(self, turno_perseguidor,profundidad):
        """
        Sirve para mover a la maquina a la siguiente casilla utilizando el algoritmo 
        minmax y la función de evaluación. Tiene como inputs: 
        - Cuál es el turno de la máquina: (turno_perseguidor = True / False)
        - 
        """
        if (profundidad == 0 or self.posicion_perseguido == self.posicion_perseguidor):
            return self.funcion_evaluacion(self.mapa)
        
        elif turno_perseguidor: # turno_perseguidor == nodo min (tiene que atrapar)
            min = float("inf")
            caminos = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in caminos:
                    turno_anterior = self.posicion_perseguidor
                    self.posicion_perseguidor = self.posicion_perseguidor + np.array((dx,dy))
                    valor = self.minmax(turno_perseguidor = False, profundidad=profundidad-1)  
                    if valor < min:
                        min = valor
                        if profundidad == self.profundidad_minmax:
                            mejor_posicion = self.posicion_perseguidor
                    self.posicion_perseguidor = turno_anterior
            if profundidad == self.profundidad_minmax:
                self.posicion_perseguidor = mejor_posicion
            else:
                return min
            
        elif not turno_perseguidor: # not turno_perseguidor == nodo max (tiene que huir)
            max = float("-inf")
            caminos = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx,dy in caminos:
                turno_anterior = self.posicion_perseguido
                self.posicion_perseguido = self.posicion_perseguido + np.array((dx,dy))
                valor = self.minmax(turno_perseguidor = True, profundidad=profundidad-1)  
                if valor > max:
                    max = valor
                    if profundidad == self.profundidad_minmax:
                        mejor_posicion = self.posicion_perseguido
                self.posicion_perseguido = turno_anterior
            if profundidad == self.profundidad_minmax:
                self.posicion_perseguido = mejor_posicion
            else:
                return max
            
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
    botoien_dist = height//10
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

    # Loop orokorra
    while running:
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            if event.type == pygame.QUIT: # Exekutatzeaz bukatzeko
                running = False
                zer_egin = "terminar"
            elif keys[pygame.K_RETURN]: # Enter botoia sakatzerakoan
                pass
            elif event.type == pygame.MOUSEBUTTONDOWN: # Xaguaren botoiren bat sakatzen bada
                if event.button == 1: # Ezkerreko botoia sakatzen bada
                    if botoia_itzuli_menura.rect.collidepoint(event.pos):
                        running = False
                        zer_egin = "menu"
                    

        # while buklearen amaieran, pantaila marraztu, textua idatzi eta aktualizatzeko
        dibujar_cuadricula(pilla_pilla,screen)

        screen.blit(izenburua.render("Jugando", True, TEXT_COLOR),(width - 295, 30))
        screen.blit(instrukzioak.render("Click enter to see the next example", True, TEXT_COLOR),(width - 295, 55))
        botoia_itzuli_menura.draw(screen)
        pygame.display.flip()
        
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
            mapa = np.array(
                [[0, 0, 0, 1, 0],
                 [0, 1, 0, 1, 0],
                 [0, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 1, 0, 0]
                 ])
            p1 = PillaPilla(1,5,mapa)
            que_hacer = juego(p1)

    pygame.quit()








if __name__ == "__main__":
    main()