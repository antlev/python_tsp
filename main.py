from Genetic import Genetic
from Tsp import Tsp
from tkinter import *


def main():
    """ Main function. """
    # target = "Hello, World !"
    # pop_size = 10
    # best_pourcentage = 0.30
    # crossover_rate = 0.70
    # mutation_rate = 0.5
    # gen = Genetic(target, pop_size, best_pourcentage, crossover_rate, mutation_rate)
    #
    # iterations = 1000
    # best_fitness_exp =0
    # gen.start(iterations, best_fitness_exp)



    app = Tsp(60)


    app.run()

if __name__ == '__main__':
    main()