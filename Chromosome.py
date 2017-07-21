import string
from string import ascii_letters
import random
from random import randint

class Chromosome:

    def __init__(self, size):
        self.genes = []
        self.fitness = size
        self.size = size
        self.letters = ascii_letters + ' !\'.,' # All letters accepted

        for i in range(0, size):
            self.genes.append(random.choice(ascii_letters))

    def evaluate(self, target):
        fitness = 0
        for i in range(0, self.size):
            if self.genes[i] != target[i]:
                fitness += 1
        self.fitness = fitness

    def mutate(self):
        self.genes[randint(0, self.size-1)] = random.choice(self.letters)

    def toString(self):
        str2 = ""
        for i in range(0, self.size):
            str2 += repr(self.genes[i])
        str2 += " fitness : " + repr(self.fitness)
        return str2
