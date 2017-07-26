from tkinter import *
from math import *
from Genetic import Genetic

class Tsp(Frame):
    def __init__(self, nb_city):
        # set the window
        self.fen = Tk()
        self.fen.title('TSP')
        self.height = 900
        self.width = 900
        self.canvas = Canvas(self.fen, width=self.width, height=self.height, background='white')
        self.bou_action = Button(self.fen)
        self.bou_action.config(text='build', command=self.build)
        self.bou_action.pack()
        # set the algorithm variables
        self.nb_city = nb_city
        self.cities = []
        self.build()
        pop_size = 16
        best_pourcentage = 0.70
        crossover_rate = 0.70
        mutation_rate = 0.01
        gen = Genetic(nb_city, pop_size, best_pourcentage, crossover_rate, mutation_rate, self)

        iterations = 100000
        best_fitness_exp = 0
        gen.start(iterations, best_fitness_exp) # Launch the algorithm

    # Draw the new solution
    def draw_sol(self, chromosome):
        self.canvas.delete("all")
        self.canvas.pack()
        width = 900
        height = 900
        path = []
        for i in range(0,self.nb_city):
            path += self.cities[chromosome.genes[i]]
        path += self.cities[chromosome.genes[0]]
        self.canvas.create_line(path, width=1)
        self.canvas.pack()

    def build(self):
        center = 300
        pi = 3.14
        teta = 0
        r = 250
        while teta < 360:
            self.cities.append([r*sin(teta*pi/180)+center,r*cos(teta*pi/180)+center])
            teta += 360/self.nb_city
        self.canvas.create_polygon(self.cities, fill="blue", outline="red", width=3)
        self.canvas.pack()

    # return the distance between 2 cities using their indexes
    def length(self, x1, x2):
        tmp = self.cities[x1][1]
        return sqrt((self.cities[x2][0] - self.cities[x1][0]) * (self.cities[x2][0] - self.cities[x1][0]) + (self.cities[x2][1] - self.cities[x1][1]) * (self.cities[x2][1] - self.cities[x1][1]))

    def calc_best_length(self):
        length = 0
        for i in range(0,self.nb_city-1):
            length += self.length(i, i+1)
        length += self.length(self.nb_city-1, 0)
        return length
