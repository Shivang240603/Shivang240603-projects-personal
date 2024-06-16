import torch
import random

class GeneticAlgorithm:
    def __init__(self, population_size, gene_length, mutation_rate, crossover_rate):
        self.population_size = population_size
        self.gene_length = gene_length
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.population = self.initialize_population()

    def initialize_population(self):
        # Initialize a population with random genes
        return torch.randint(0, 4, (self.population_size, self.gene_length)).float()

    def fitness(self, individual):
        # Define a fitness function
        # For simplicity, let's just sum the genes (you should replace this with your actual fitness function)
        return individual.sum().item()

    def select_parents(self):
        # Select parents based on fitness (using roulette wheel selection)
        fitness_scores = torch.tensor([self.fitness(ind) for ind in self.population])
        total_fitness = fitness_scores.sum()
        probabilities = fitness_scores / total_fitness
        parent_indices = torch.multinomial(probabilities, 2)
        return self.population[parent_indices]

    def crossover(self, parents):
        # Perform crossover to produce offspring
        if random.random() < self.crossover_rate:
            crossover_point = random.randint(1, self.gene_length - 1)
            offspring1 = torch.cat((parents[0][:crossover_point], parents[1][crossover_point:]))
            offspring2 = torch.cat((parents[1][:crossover_point], parents[0][crossover_point:]))
            return offspring1, offspring2
        else:
            return parents[0], parents[1]

    def mutate(self, individual):
        # Perform mutation on an individual
        for gene in range(self.gene_length):
            if random.random() < self.mutation_rate:
                individual[gene] = 1.0 - individual[gene]
        return individual

    def run_generation(self):
        new_population = []
        for _ in range(self.population_size // 2):
            parents = self.select_parents()
            offspring1, offspring2 = self.crossover(parents)
            new_population.append(self.mutate(offspring1))
            new_population.append(self.mutate(offspring2))
        self.population = torch.stack(new_population)

# Parameters
population_size = 70
gene_length = 7
mutation_rate = 0.03
crossover_rate = 0.4

# Create an instance of the genetic algorithm
ga = GeneticAlgorithm(population_size, gene_length, mutation_rate, crossover_rate)

# Run the genetic algorithm for a number of generations
num_generations = 20
for generation in range(num_generations):
    ga.run_generation()
    print(f"Generation {generation+1}: Best fitness = {max([ga.fitness(ind) for ind in ga.population])}")
