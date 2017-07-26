from threading import Thread
from tkinter import *
from math import *
from Genetic.Genetic import Genetic

class Tsp(Frame, Thread):
    def __init__(self, nb_city, pop_size, best_pourcentage, crossover_rate, mutation_rate, iterations_max):
        Thread.__init__(self)
        print("Succesful launch of TSP with nb_city = "+ repr(nb_city) + " pop_size = "+ repr(pop_size) + " best_pourcentage = "+ repr(best_pourcentage) + " crossover_rate = "+ repr(crossover_rate)+ " mutation_rate = "+ repr(mutation_rate))
        # set the algorithm variables
        self.cities = []
        self.nb_city = nb_city
        self.pop_size  = pop_size
        self.best_pourcentage = best_pourcentage
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.iterations_max = iterations_max
        def call_back(*args):
            tmp=0
        # set the window for tsp
        self.fen = Tk()
        self.fen.title('TSP')
        self.height = 900
        self.width = 900
        self.canvas = Canvas(self.fen, width=self.width, height=self.height, background='white')
        self.start_button = Button(self.fen)
        self.start_button.config(text='Start', command=self.run)
        self.start_button.pack()
        self.label_nb_city = Label(self.fen, text="Nb City : " + repr(self.nb_city))
        self.label_nb_city.pack()
        self.label_pop_size = Label(self.fen, text="Population size : " + repr(self.pop_size))
        self.label_pop_size.pack()
        self.label_best_pourcentage = Label(self.fen, text="Bests pourcentage : " + repr(self.best_pourcentage))
        self.label_best_pourcentage.pack()
        self.label_crossover_rate = Label(self.fen, text="Crossover Rate : " + repr(self.crossover_rate))
        self.label_crossover_rate.pack()
        self.label_mutation_rate = Label(self.fen, text="Mutation Rate : " + repr(self.mutation_rate))
        self.label_mutation_rate.pack()
        self.iterations = IntVar()
        self.iterations.set(0)
        self.iterations.trace("w", call_back)
        self.fitness = IntVar()
        self.fitness.set(0)
        self.fitness.trace("w", call_back)
        self.label_iterations_max = Label(self.fen, text="Iterations Max : " + repr(self.iterations_max))
        self.label_iterations_max.pack()
        self.label_current_iter = Label(self.fen, text="Current Iterations : " + repr(self.iterations.get()))
        self.label_current_iter.pack()
        self.label_fitness = Label(self.fen, text="Current fitness : " + repr(self.fitness.get()))
        self.label_fitness.pack()
        self.status = StringVar()
        self.status.set("READY")
        self.status.trace("w", call_back)
        self.label_status = Label(self.fen, text=self.status.get())
        self.label_status.pack()
        self.build() # Build a polygon of the response

        self.fen.update()
        self.fen.update_idletasks()

    # Launch the gentic algorithm
    def run(self):
        gen = Genetic(self.nb_city, self.pop_size, self.best_pourcentage, self.crossover_rate, self.mutation_rate, self.iterations_max, self)
        self.status.set("RUNNING")
        self.label_status.pack()
        if gen.run() == 0: # Launch the algorithm
            self.status.set("RUNNING")
        else:
            self.status.set("FAILURE")

    # Draw the new solution
    def draw_sol(self, chromosome, iteration):
        self.canvas.delete("all")
        self.canvas.pack()
        self.iterations = iteration
        self.label_current_iter.pack()
        self.fitness = chromosome.fitness
        self.label_fitness.pack()
        width = 900
        height = 900
        path = []
        for i in range(0,self.nb_city):
            path += self.cities[chromosome.genes[i]]
        path += self.cities[chromosome.genes[0]]
        self.canvas.create_line(path, width=1)
        self.canvas.pack()

    # Build a polygon with the cities
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

    # Calculate the best path (using the circle path 0->1->2->3->...->n->0)
    def calc_best_length(self):
        length = 0
        for i in range(0,self.nb_city-1):
            length += self.length(i, i+1)
        length += self.length(self.nb_city-1, 0)
        return length
