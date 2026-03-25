
import tkinter as tk
from tkinter import Tk, Button, Frame


class Minesweeper:
    def __init__(self):
        self.screen = Tk()
        self.screen.title("Mines Weeper 💣")
        self.screen.minsize(800, 850)
        
        self.largeur = 10
        self.hauteur = 10

        self.matrice = [[0 for _ in range(self.hauteur)] for _ in range(self.largeur)]

        self.creer_grille()
        
        self.frame = Frame(self.screen)
        self.frame.pack()
        self.play_button = Button(self.frame, text=" jouer ")
        self.play_button.pack()
        

        self.difficulty_buttonup = Button(self.frame, text=" diff + ")
        self.difficulty_buttonup.pack()
        self.difficulty_buttondwn = Button(self.frame, text=" diff - ")
        self.difficulty_buttondwn.pack()
   
    def creer_grille(self):
        
        frame_grille = Frame(self.screen)
        frame_grille.pack(expand=True)

        for i in range(self.largeur):
            for j in range(self.hauteur):
                bouton = Button(frame_grille, width=2, height=1)
                bouton.grid(row=i, column=j)


    def run(self):
        self.screen.mainloop()


if __name__ == "__main__":
    jeu = Minesweeper()
    jeu.run()