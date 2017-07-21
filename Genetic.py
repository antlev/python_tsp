import random
from random import randint

from Chromosome import Chromosome


class Genetic:

    def __init__(self, target, pop_size, best_pourcentage, crossover_rate, mutation_rate):
        self.target = target
        self.chromosome_size = len(target)
        self.pop_size = pop_size
        self.best_pourcentage = best_pourcentage
        self.mutation_rate = mutation_rate
        self.indiv_to_cross = int(crossover_rate * pop_size)
        self.population = []
        self.new_population = []
        self.pair_selected_indiv = []
        for i in range(0,pop_size):
            self.population.append(Chromosome(self.chromosome_size))

    def evaluate(self):
        for i in range(0, self.pop_size):
            self.population[i].evaluate(self.target)
        self.order_pop()

    def order_pop(self):
        permutation = True
        passage = 0
        while permutation == True:
            permutation = False
            passage = passage + 1
            for en_cours in range(0, self.pop_size - passage):
                if self.population[en_cours].fitness > self.population[en_cours + 1].fitness:
                    permutation = True
                    # On echange les deux elements
                    self.population[en_cours], self.population[en_cours + 1] = \
                        self.population[en_cours + 1], self.population[en_cours]

    def selection(self):
        self.pair_selected_indiv.clear()
        index = randint(0, self.indiv_to_cross)
        index2 = randint(0, self.indiv_to_cross)
        while index == index2:
            index2 = randint(0, self.best_pourcentage * self.pop_size)

        self.pair_selected_indiv.append(self.population[index])
        self.pair_selected_indiv.append(self.population[index2])

    def cross(self):

        print("before cross>")
        self.show_selected_indiv()
        index = randint(0, self.chromosome_size)

        print("debug index ="+ repr(index))
        for i in range(index, self.chromosome_size):
            tmp = self.pair_selected_indiv[0].genes[i]
            self.pair_selected_indiv[0].genes[i] = self.pair_selected_indiv[1].genes[i]
            self.pair_selected_indiv[1].genes[i] = tmp
        print("after cross>")
        self.show_selected_indiv()

    def crossover(self):
        # print("before crossover>")
        # self.show_population()
        self.new_population.clear()
        for i in range(0,self.indiv_to_cross):
            self.selection()
            self.cross()
            self.new_population.append(self.pair_selected_indiv[0])
            i+=1
            self.new_population.append(self.pair_selected_indiv[1])
            i+=1
        self.population.clear()
        for i in range(0, self.indiv_to_cross):
            self.population.append(self.new_population[i])
        for i in range(self.indiv_to_cross, self.pop_size):
            self.population.append(Chromosome(self.chromosome_size))
        # print("after crossover>")
        # self.show_population()

    def mutate(self):
        for i in range(0,self.pop_size):
            if random.uniform(0, 1) < self.mutation_rate:
                self.population[i].mutate()

    def show_population(self):
        print("--------------- Population ---------------")
        for i in range(0, self.pop_size):
            print("indiviual " + repr(i) + " " + self.population[i].toString())

    def show_selected_indiv(self):
        print("--------------- selected_ind ---------------")
        for i in range(0, 2):
            print("indiviual " + repr(i) + " " + self.pair_selected_indiv[i].toString())

    def start(self, iterations_max, best_fitness_exp):
        iter = 0
        self.evaluate()


        while self.population[0].fitness != best_fitness_exp or iter >= iterations_max:
            self.crossover()
            self.mutate()
            self.evaluate()
            self.show_population()
            iter += 1

