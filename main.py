# TERMÓMETRO PYGAME


# En esta clase es donde se desarrolla el juego o la aplicación
import pygame, sys
from pygame.locals import *

class Termometro():
    
    def __init__(self):
        #Tiene un atributo, que es la imagen
        self.custome = pygame.image.load('Images/termometro.png')
        
    def convertir(self, grados, toUnidad):
        resultado = 0
        if toUnidad == 'F':
            resultado = grados * 9/5 + 32
        elif toUnidad == 'C':
            resultado = (grados - 32) * 5/9
        else:
            resultado = grados
            
        return '{:6.1f}'.format(resultado)

class Selector():
    
    def __init__(self, unidad = 'C'):
        #La clase selector son dos dibujos, de modo que crearemos una lista de dos elementos
        self.__customes = [pygame.image.load('Images/PosC.png')]
        self.__customes.append(pygame.image.load('Images/PosF.png'))
        
        self.__tipounidad = unidad
        
    def unidad(self):
        return self.__tipounidad
    
    def custome(self):
        if self.__tipounidad == 'F':
            return self.__customes[1]
        elif self.__tipounidad == 'C':
            return self.__customes[0]

    def change(self):
        if self.__tipounidad == 'F':
            self.__tipounidad = 'C'
        else:
            self.__tipounidad = 'F'
            
class NumberInput():
    
    __value    = 0
    __strvalue = ''
    __position = [0,0]
    __size     = [0,0]
    
    def __init__(self, value = None):
        
        self.font = pygame.font.SysFont('Arial', 24)
        self.value(value)
                
    def on_event(self, event):
        if event.type == KEYDOWN:
            if event.unicode.isdigit() and len(self.__strvalue)<10:
                self.__strvalue += event.unicode
                self.value(self.__strvalue)
                print(self.__value, self.__strvalue)
            elif event.key == K_BACKSPACE:
                self.__strvalue = self.__strvalue[:-1]
                self.value(self.__strvalue)
                
    
    def render(self):
        
        textblock = self.font.render(self.__strvalue, True, (74, 74, 74))
        rect = textblock.get_rect()
        rect.left = self.__position[0]
        rect.top  = self.__position[1]
        rect.size = self.__size
        
        return (rect, textblock)
    
    def value(self, val = None):
        if val == None:
            return self.__value
        else:
            val = str(val)
            try:
                self.__value    = round(float(val),1)
                self.__strvalue = val
            except:
                print ('Fallo')

    def posX(self, val = None):
        if val == None:
            return self.__position[0]
        else:
            try:
                self.__position[0] = int(val)
            except:
                pass

    def posY(self, val = None):
        if val == None:
            return self.__position[1]
        else:
            try:
                self.__position[1] = int(val)
            except:
                pass

    def pos(self, val = None):
        if val == None:
            return self.__position
        else:
            try:
                self.__position = [int(val[0]),int(val[1])]
            except:
                pass

    def width(self, val = None):
        if val == None:
            return self.__size[0]
        else:
            try:
                self.__size[0] = int(val)
            except:
                pass

    def height(self, val = None):
        if val == None:
            return self.__size[1]
        else:
            try:
                self.__size[1] = int(val)
            except:
                pass

    def size(self, val = None):
        if val == None:
            return self.__size
        else:
            try:
                self.__size = [int(val[0]),int(val[1])]
            except:
                pass



class MainApp():
    termometro = None
    entrada    = None
    selector   = None
    
    def __init__(self):
        # Parámetros de la pantalla
        self.__screen = pygame.display.set_mode((300,415))
        pygame.display.set_caption('TERMÓMETRO PYGAME')        
        
        self.termometro = Termometro()
        
        self.entrada = NumberInput()
        self.entrada.pos((106, 58))
        self.entrada.size((133, 28 ))
        
        self.selector = Selector()
        
        
    def __on_close(self):
        pygame.quit()
        sys.exit()
    
    def start(self):
        while True:
            #Miramos los eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.__on_close()
                if event.type == MOUSEBUTTONDOWN:
                    self.selector.change()
                    grados = self.entrada.value()
                    nuevaUnidad = self.selector.unidad()
                    temperatura = self.termometro.convertir(grados, nuevaUnidad)
                    self.entrada.value(temperatura)
                    
                self.entrada.on_event(event)    
                
            self.__screen.fill((244,236,203))
            
            self.__screen.blit(self.termometro.custome, (50,34))
            
            text = self.entrada.render()
            pygame.draw.rect(self.__screen, (255,255,255), text[0])
            self.__screen.blit(text[1],self.entrada.pos())

            self.__screen.blit(self.selector.custome(), (112,153))
            
            #Actualizamos la pantalla
            pygame.display.flip()
  


if __name__ == '__main__':
    
    # Inicializamos pygame
    pygame.init()
    # Creamos la instancia
    app = MainApp()
    # Llamamos a empezar (start)
    app.start()
    





        
