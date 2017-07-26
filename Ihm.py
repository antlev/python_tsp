from tkinter import *
from Genetic import Genetic
from math import *
from Tsp import Tsp
import time




class Ihm:

    def __init__(self):
        # set the window
        self.fen = Tk()
        self.fen.title('TSP')
        self.height =  900
        self.width = 900
        self.canvas = Canvas(self.fen, width=self.width, height=self.height, background='white')
        # Setting default variable for tsp
        self.nb_city = IntVar()
        self.pop_size = IntVar()
        self.best_pourcentage = DoubleVar()
        self.crossover_rate = DoubleVar()
        self.mutation_rate = DoubleVar()
        self.iterations_max = IntVar()
        self.nb_city.set(10)
        self.pop_size.set(16)
        self.best_pourcentage.set(0.5)
        self.crossover_rate.set(0.7)
        self.mutation_rate.set(0.05)
        self.iterations_max.set(10000)
        # To modify thos variable in the entries
        def mywarWritten(*args):
            print
            "mywarWritten", self.nb_city.get()
        self.nb_city.trace("w", mywarWritten)
        self.pop_size.trace("w", mywarWritten)
        self.best_pourcentage.trace("w", mywarWritten)
        self.crossover_rate.trace("w", mywarWritten)
        self.mutation_rate.trace("w", mywarWritten)
        self.iterations_max.trace("w", mywarWritten)
        self.bou_action = Button( self.fen, text='Lancer', command= lambda: self.run())
        self.bou_action2 = Button( self.fen, text='Quitter', command= self.fen.quit)
        self.bou_action.pack()
        self.bou_action2.pack()
        self.label = Label(self.fen, text="Nb City")
        self.label.pack()
        self.entry = Entry(self.fen, textvariable=self.nb_city, validatecommand='all')
        self.entry.pack()
        self.label = Label(self.fen, text="Population size")
        self.label.pack()
        self.entry1 = Entry( self.fen, textvariable=self.pop_size, validatecommand = 'focusout')
        self.entry1.pack()
        self.label = Label(self.fen, text="Best Pourcentage")
        self.label.pack()
        self.entry = Entry( self.fen, textvariable=self.best_pourcentage, validatecommand = 'focusout')
        self.entry.pack()
        self.label = Label(self.fen, text="Crossover Rate")
        self.label.pack()
        self.entry = Entry( self.fen, textvariable=self.crossover_rate, validatecommand = 'focusout')
        self.entry.pack()
        self.label = Label(self.fen, text="Mutation Rate")
        self.label.pack()
        self.entry = Entry( self.fen, textvariable=self.mutation_rate, validatecommand = 'focusout')
        self.entry.pack()
        self.label = Label(self.fen, text="Iterations max")
        self.label.pack()
        self.entry = Entry( self.fen, textvariable=self.iterations_max, validatecommand = 'focusout')
        self.entry.pack()

        self.fen.mainloop()

    def run(self):
        Tsp(self.nb_city.get(), self.pop_size.get(), self.best_pourcentage.get(), self.crossover_rate.get(), self.mutation_rate.get(), self.iterations_max.get())

# Main programm
def main():
    Ihm()

if __name__ == '__main__':
    main()