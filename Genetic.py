import random
from random import randint
import sys
import time
from Chromosome import Chromosome

class Genetic():
    # Constructor, set all the variable needed
    def __init__(self, nb_city, pop_size, best_pourcentage, crossover_rate, mutation_rate,iterations, tsp):
        random.seed() # Use timestamp as seed
        self.chromosome_size = nb_city # Define  the chromosome size
        self.pop_size = pop_size # Define the population size
        self.bests = int(pop_size * best_pourcentage) # Define the max index of the individual that is consider as best
        self.mutation_rate = mutation_rate # Define the mutation rate
        self.tsp = tsp
        self.indiv_to_cross = int(crossover_rate * pop_size)
        self.population = [] # Store the population
        self.best_fitness  = sys.float_info.max # Stores the score of the best individual
        self.minimum_fitness = tsp.calc_best_length()
        self.new_population = [] # List used to build the new population
        self.pair_selected_indiv = [] # A pair of indiv filled by selection function
        self.iterations_max = iterations
        for i in range(0,pop_size):
            self.population.append(Chromosome(self.chromosome_size)) # init a population

    # Evaluate a population and print it a new best solution is found
    def evaluate(self, iter):
        for i in range(0, self.pop_size):
            self.population[i].evaluate(self.tsp)
        self.order_pop()
        if self.population[0].fitness < self.best_fitness:
            self.best_fitness = self.population[0].fitness
            print("New best solution found ! iterations : " + repr(iter))
            self.show_population()
            if self.best_fitness == self.minimum_fitness:
                print("Youpi ! !")
                self.tsp.build()
                time.sleep(5)
                exit(0)

    # Order the population using their fitness
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
    # Select 2 chromosome
    def selection(self):
        self.pair_selected_indiv.clear()
        index = randint(0, self.bests)
        index2 = randint(0, self.bests)
        while index == index2:
            index2 = randint(0, self.indiv_to_cross)
        self.pair_selected_indiv.append(self.population[index])
        self.pair_selected_indiv.append(self.population[index2])

    # do a crossover between 2 chromosomes
    # http://www.rubicite.com/Tutorials/GeneticAlgorithms/CrossoverOperators/PMXCrossoverOperator.aspx
    def cross(self):
        # print("before cross")
        # for j in self.pair_selected_indiv:
        #     print(j.genes)
        child1 = self.chromosome_size*[None]
        child2 = self.chromosome_size*[None]
        index = randint(0, self.chromosome_size-1)
        index2 = randint(index, self.chromosome_size)
        # print("index 1 : " +repr(index))
        # print("index 2 : " +repr(index2))

        # 1) copy all the genes that are between both indexes
        for i in range(index, index2):
            child1[i] = self.pair_selected_indiv[0].genes[i]
        # 2) PMX crossover
        for i in range(index, index2):
            val = self.pair_selected_indiv[1].genes[i]
            index_tmp = i
            val2 = val
            if val not in child1:
                while True:
                    val2 = self.pair_selected_indiv[0].genes[index_tmp]
                    index_tmp = self.pair_selected_indiv[1].genes.index(val2)
                    if index_tmp not in range(index,index2):
                        child1[index_tmp] = val
                        break
        # 3) copying values that were not copied
        for i in range(0,self.chromosome_size):
            if child1[i] == None:
                child1[i] = self.pair_selected_indiv[1].genes[i]

        tmp = self.pair_selected_indiv[0]
        self.pair_selected_indiv[0] = self.pair_selected_indiv[1]
        self.pair_selected_indiv[1] = tmp


        # 1) copy all the genes that are between both indexes
        for i in range(index, index2):
            child2[i] = self.pair_selected_indiv[0].genes[i]
        # 2) PMX crossover
        for i in range(index, index2):
            val = self.pair_selected_indiv[1].genes[i]
            index_tmp = i
            val2 = val
            if val not in child2:
                while True:
                    val2 = self.pair_selected_indiv[0].genes[index_tmp]
                    index_tmp = self.pair_selected_indiv[1].genes.index(val2)
                    if index_tmp not in range(index,index2):
                        child2[index_tmp] = val
                        break
        # 3) copying values that were not copied
        for i in range(0,self.chromosome_size):
            if child2[i] == None:
                child2[i] = self.pair_selected_indiv[1].genes[i]

        self.pair_selected_indiv[0].genes = child1
        self.pair_selected_indiv[1].genes = child2
        # print("after cross")
        # for j in self.pair_selected_indiv:
        #     print(j.genes)

    # Defines the crossover
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

    # Call mutate on each gene
    def mutate(self):
        for i in range(0,self.pop_size):
            if random.uniform(0, 1) < self.mutation_rate:
                self.population[i].mutate()

    # Print population
    def show_population(self):
        print("nb_city:"+repr(self.chromosome_size)+"pop_size:"+repr(self.pop_size)+" bests:"+repr(self.bests)+" indiv_to_cross:"+repr(self.indiv_to_cross)+" mutation_rate:"+repr(self.mutation_rate)+" iterations_max:"+repr(self.iterations_max))
        print("-------------------------- Population --------------------------")
        for i in range(0, self.pop_size):
            print("indiviual " + repr(i) + " " + self.population[i].toString())
        self.tsp.draw_sol(self.population[0])
        self.tsp.fen.update_idletasks()
        self.tsp.fen.update()

    # Defines the genetic algorithm
    def run(self):
        time.sleep((10))
        iter = 0
        self.evaluate(iter)
        while self.population[0].fitness > self.minimum_fitness and iter < self.iterations_max:
            self.crossover()
            self.mutate()
            iter += 1
            self.evaluate(iter)
            # self.show_population()
        print("STOP BY ITERATIONS")
        self.show_population()

