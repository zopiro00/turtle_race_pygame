import pygame, sys, random


class Runner():
    
    __customes = ("turtle","fish","prawn","moray","octopus")
    
    def __init__(self, x=0, y=0):
        self.custome = pygame.image.load("sources/{}.png".format(self.__customes[random.randint(0,4)]))
        self.position = [x,y]
        self.name = "Tortuga"
        
    def avanzar(self):
        self.position[0] += random.randint(1,6)
        
class Game():
    runners = []
    __posY = (160,200,240,280)
    __names = ("speedy","Lucera","Alonso","Torcuato")
    __startLine = 10
    __finishLine = 620
    
    def __init__(self):
        #Definición de pantalla
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        self.__background = pygame.image.load("sources/background.png")
        
        #Creación de jugador basado en la clase Runner 
        for i in range(4):
            theRunner = Runner(self.__startLine,self.__posY[i])
            theRunner.name = self.__names[i]
            self.runners.append(theRunner)
    def close(self):
        pygame.quit()
        sys.exit()
    def competir(self):
        GameOver = False
        
        while not GameOver:
            # Comprobación de eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            # Mover la tortuga
            for runner in self.runners:
                runner.avanzar()
                if runner.position[0] >= self.__finishLine:
                    print("{} ha ganado".format(runner.name))
                    GameOver = True
            
            # Refrescar / renderizar la pantalla
            self.__screen.blit(self.__background, (0,0))
            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            pygame.display.flip()
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.competir()