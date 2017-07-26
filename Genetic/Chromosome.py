import sys
import random
from random import randint

# Define one solution of the problem
class Chromosome:

    def __init__(self, size):
        random.seed() # Uses the timestamp as a seed
        self.genes = []
        self.fitness = sys.float_info.max # Set the fitnes at the maximum possible value
        self.size = size
        tab = []
        # Construct an array containing all cities indexes
        for i in range(0, size):
            tab.append(i)

        # choose a city randomly, append it to the solution and delete it from temp tab
        while len(tab) > 0:
            tab_pt = tab[random.randint(0, len(tab)-1)]
            self.genes.append(tab_pt)
            tab.remove(tab_pt)

    # Evaluate function that set the fitness
    def evaluate(self, tsp):
        self.fitness = 0
        for i in range(0, self.size-1):
            self.fitness += tsp.length(self.genes[i], self.genes[i + 1])
        self.fitness += tsp.length(self.genes[self.size - 1], self.genes[0])

    # Defines how the chromosome mutate
    def mutate(self):
        rdm = randint(0, self.size-1)
        rdm2 = randint(0, self.size-1)
        while rdm == rdm2:
            rdm2 = randint(0, self.size - 1)
        rmd_gene = self.genes[rdm]
        self.genes[rdm] = self.genes[rdm2]
        self.genes[rdm2] = rmd_gene

    # Return a string containing the ordered indexes of the cities and the current fitness
    def toString(self):
        str2 = ""
        for i in range(0, self.size):
            str2 += repr(self.genes[i])
        str2 += " fitness : " + repr(self.fitness)
        return str2
