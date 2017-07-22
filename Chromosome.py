import string
import sys
from string import ascii_letters
import random
from random import randint

from Tsp import Tsp

class Chromosome:

    def __init__(self, size):
        random.seed()
        self.genes = []
        self.fitness = sys.float_info.max
        self.size = size
        tab = []
        for i in range(0, size):
            tab.append(i)

        while len(tab) > 0:
            tab_pt = tab[random.randint(0, len(tab))]
            self.genes.append(tab_pt)
            tab.remove(tab_pt)


    def evaluate(self, tsp):
        fitness = 0
        for i in range(0, self.size):
            fitness += tsp.distance(self.genes[i], self.genes[i+1])
        self.fitness = fitness

    def mutate(self):
        rdm = randint(0, self.size-1)
        rdm2 = randint(0, self.size-1)
        while rdm == rdm2:
            rdm2 = randint(0, self.size - 1)
        rmd_gene = self.genes[rdm]
        self.genes[rdm] = self.genes[rdm2]
        self.genes[rdm2] = rmd_gene

    def toString(self):
        str2 = ""
        for i in range(0, self.size):
            str2 += repr(self.genes[i])
        str2 += " fitness : " + repr(self.fitness)
        return str2
