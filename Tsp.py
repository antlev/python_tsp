from threading import Thread
from tkinter import *
from math import *
from Genetic import Genetic

class Tsp(Frame, Thread):
    def __init__(self, nb_city, pop_size, best_pourcentage, crossover_rate, mutation_rate, iterations_max):
        Thread.__init__(self)
        print("Succesful launch of TSP with nb_city = "+ repr(nb_city) + " pop_size = "+ repr(pop_size) + " best_pourcentage = "+ repr(best_pourcentage) + " crossover_rate = "+ repr(crossover_rate)+ " mutation_rate = "+ repr(mutation_rate))
        # set the window for tsp
        self.fen = Tk()
        self.fen.title('TSP')
        self.height = 900
        self.width = 900
        self.canvas = Canvas(self.fen, width=self.width, height=self.height, background='white')
        self.bou_action = Button(self.fen)
        self.bou_action.config(text='Start', command=self.run)
        self.bou_action.pack()
        self.bou_action = Button(self.fen)
        self.bou_action.config(text='Stop', command=self.fen.quit)
        self.bou_action.pack()
        # set the algorithm variables
        self.nb_city = nb_city
        self.cities = []
        self.pop_size  = pop_size
        self.best_pourcentage = best_pourcentage
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.iterations_max = iterations_max
        self.build()


    def run(self):
        gen = Genetic(self.nb_city, self.pop_size, self.best_pourcentage, self.crossover_rate, self.mutation_rate, self.iterations_max, self)
        gen.run() # Launch the algorithm

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
