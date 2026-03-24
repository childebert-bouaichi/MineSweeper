from tkinter import *

class Interface:

    def __init__(self):
        self.matrice = []
        self.hauteur = 10
        self.largeur = 10
        self.screen = Tk()
        self.screen.minsize(300,300)
        self.screen.title("Démineur")


    def grid(self):
        
        self.matrice = [[0 for i in range(self.hauteur)] for j in range(self.largeur)]
        for k in self.matrice:
            bouton = Button(self.screen)
            bouton.grid()
        
            
        
        self.screen.mainloop()


test = Interface()
test.grid()

        