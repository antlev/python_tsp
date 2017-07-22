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

        self.cities = []

    def run(self):
        self.fen.mainloop()
        self.draw()

    def draw_sol(self, chromosome):
        width = 900
        height = 900
        canvas = Canvas(self.fen, width=width, height=height, background='white')
        canvas.create_polygon(chromosome, fill="magenta", outline="yellow", width=3)
        canvas.pack()

    def draw(self):
        width = 900
        height = 900
        pi = 3.14
        canvas = Canvas(self.fen, width=width, height=height, background='white')
        teta = 0
        r = 250
        while teta < 360:
            self.cities.append([r*sin(teta*pi/180)+500,r*cos(teta*pi/180)+500])
            teta += 360/self.nb_city
        canvas.create_polygon(self.cities, fill="magenta", outline="yellow", width=3)
        canvas.pack()

    def distance(self,x1, x2):
        return sqrt((self.cities[x2][0] - self.cities[x1][0]) * (self.cities[x2][0] - self.cities[x1][0]) + (self.cities[x2][1] - self.cities[x1][1]) * (self.cities[x2][1] - self.cities[x1][1]))


        # canvas.pack()