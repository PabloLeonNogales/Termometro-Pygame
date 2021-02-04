# APLICACIÓN TERMÓMETRO
import pygame, sys
from pygame.locals import *

class Termometro():
    
    def __init__(self):
        # Cargamos la imagen en la variable 'costume'
        self.costume = pygame.image.load('Images/termometro.png')
        
    def convertir (self):
        
        if self.pos_selector = 0:
            resultado = (grados - 32) * 5/9
        elif self.pos_selector = 1:
            resultado = grados+9/5 + 32
        
        return '{:6.2f}'.format(resultado)
            
            
    
class Entrada():
    
    __valor = 0
    __strvalor = ''
    
    def __init__(self):
        # La clase Entrada es un Font, por tanto vamos a crear el Font
        self.font  = pygame.font.SysFont('Arial', 30)
        
    def event_input(self,evento):
        
        if evento.unicode.isdigit() or evento.unicode == '.':
            try:
                temporal = self.__strvalor + evento.unicode
                self.__valor = float(temporal)
                self.__strvalor = temporal
            except:
                pass
        elif evento.key == K_BACKSPACE:
            self.__strvalor = self.__strvalor[:-1]
            try:
                self.__valor = float (self.__strvalor)
            except:
                pass
            print(self.__valor, self.__strvalor)
            

    def render(self):
        texto = self.font.render(self.__strvalor, True, (74, 74, 74))
        rect = texto.get_rect()
        widthRect = rect[2]
        heightRect = rect[3]
        return texto
    
class Selector():

    pos_selector = 0
    
    def __init__(self):
        #La clase selector son dos dibujos, de modo que crearemos una lista de dos elementos
        self.seleccion = [pygame.image.load('Images/PosC.png')]
        self.seleccion.append(pygame.image.load('Images/PosF.png'))
        
        self.__unidad = 'C'
    
    def cambiar(self):
        
        if self.pos_selector == 0:
            self.pos_selector = 1
        else:
            self.pos_selector = 0

class Principal():
    
    def __init__(self):
        # Parámetros de la pantalla
        self.__screen = pygame.display.set_mode((300,415))
        pygame.display.set_caption('TERMÓMETRO PYGAME')
        
        #La pantalla ya está pintada. Ahora vamos a pintar el resto de cosas
        self.termometro = Termometro()
        self.entrada    = Entrada()
        self.selector   = Selector()

    def __cerrar(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        
        while True:
            #Miramos los eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__cerrar()    
                elif event.type == KEYDOWN:
                    self.entrada.event_input(event)
                elif event.type == MOUSEBUTTONDOWN:
                    self.selector.cambiar()
            
            #Hacemos el color d ela pantalla
            self.__screen.fill((244,236,203))
            #Situamos el Termometro
            self.__screen.blit(self.termometro.costume, (30,30))
            #Ahora pintaremos un rectángulo (bordes negros), donde irán los números
            pygame.draw.rect(self.__screen, (0,0,0), [80, 50, 180, 35], 2)
            #Y ahora lo situamos el Font
            texto = self.entrada.render()
            self.__screen.blit(texto, (85,50))
            #Y ahora dibujamos el selector
            self.__screen.blit(self.selector.seleccion[self.selector.pos_selector], (105,200))
            
            pygame.display.flip()



if __name__ == '__main__':
    
    #Inicializamos Pygame
    pygame.init()
    #Creamos la pantalla principal
    PantallaInicio = Principal()
    #Ejecutamos Start
    PantallaInicio.start()