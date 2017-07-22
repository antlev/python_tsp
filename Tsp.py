from tkinter import *
from math import *
from Genetic import Genetic

# Importation des librairies nécéssaire au bon fonctionnement du programme.
# Tkinter pour l'interface graphique
# urllib pour les schémas internet
# os pour dialoguer avec le systeme
import tkinter as tk
import urllib as url
import os

class Tsp(Frame):
    def __init__(self, nb_city):
        print("CONSTRUCTOR TSP !!!!")

        '''constructeur'''
        self.nb_city = nb_city
        self.fen = Tk()
        self.fen.title('TSP')

        self.bou_action = Button(self.fen)
        self.bou_action.config(text='build', command=self.build)
        self.bou_action.pack()

        self.bou_quitter = Button(self.fen)
        self.bou_quitter.config(text='Quitter', command=self.fen.quit)
        self.bou_quitter.pack()

        self.height =  900
        self.width = 900
        self.canvas = Canvas(self.fen, width=self.width, height=self.height, background='white')

        self.cities = []
        self.build()

        pop_size = 16
        best_pourcentage = 0.70
        crossover_rate = 0.70
        mutation_rate = 0.1
        gen = Genetic(nb_city, pop_size, best_pourcentage, crossover_rate, mutation_rate, self)

        iterations = 1000
        best_fitness_exp = 0
        gen.start(iterations, best_fitness_exp)



    def draw_sol(self, chromosome):
        print("DRAX SOL!!!!")
        self.canvas.pack()
        width = 900
        height = 900
        path = []
        for i in range(0,self.nb_city):
            path += self.cities[chromosome.genes[i]]

        self.canvas.create_polygon(path, fill="magenta", outline="yellow", width=3)
        self.canvas.pack()

    def build(self):
        center = 300
        pi = 3.14
        teta = 0
        r = 250
        while teta < 360:
            self.cities.append([r*sin(teta*pi/180)+center,r*cos(teta*pi/180)+center])
            teta += 360/self.nb_city
        self.canvas.create_polygon(self.cities, fill="magenta", outline="yellow", width=3)
        self.canvas.pack()

    def distance(self,x1, x2):
        tmp = self.cities[x1][1]
        return sqrt((self.cities[x2][0] - self.cities[x1][0]) * (self.cities[x2][0] - self.cities[x1][0]) + (self.cities[x2][1] - self.cities[x1][1]) * (self.cities[x2][1] - self.cities[x1][1]))


        # canvas.pack()