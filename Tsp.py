from tkinter import *
from math import *

# Importation des librairies nécéssaire au bon fonctionnement du programme.
# Tkinter pour l'interface graphique
# urllib pour les schémas internet
# os pour dialoguer avec le systeme
import tkinter as tk
import urllib as url
import os


class Tsp(Frame):
    '''Application principale'''

    def __init__(self, nb_city):
        '''constructeur'''
        self.nb_city = nb_city
        self.fen = Tk()
        self.fen.title('Tkinter')

        self.bou_action = Button(self.fen)
        self.bou_action.config(text='Draw', command=self.draw)
        self.bou_action.pack()

        self.bou_quitter = Button(self.fen)
        self.bou_quitter.config(text='Quitter', command=self.fen.destroy)
        self.bou_quitter.pack()

    def run(self):
        self.fen.mainloop()
        self.draw()

    def draw(self):
        width = 900
        height = 900
        pi = 3.14
        canvas = Canvas(self.fen, width=width, height=height, background='white')

        teta = 0
        r = 250
        cities = []
        while teta < 360:
            print("teta "+repr(teta)+ " sin(teta) >" +repr(sin(teta)) +" cos(teta) >"+ repr(cos(teta)))
            cities.append((r*sin(teta*pi/180)+500,r*cos(teta*pi/180)+500))
            teta += 360/self.nb_city


        canvas.create_polygon(cities, fill="magenta", outline="yellow", width=3)
        canvas.pack()




        # canvas.pack()