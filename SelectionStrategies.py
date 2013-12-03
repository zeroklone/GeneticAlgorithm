import random
class SelectionStrategies:
    def sort_by_fitness(self, population, fitness_functions):
        # Sort the population by fitness
        fitness_functions, population = zip(*sorted(zip(fitness_functions, population)))
        fitness_functions, population = (list(t) for t in zip(*sorted(zip(fitness_functions, population))))

        return [population, fitness_functions]

    def tournament(self, population, fitness_functions):

        # Choose a breeding point from the top 4 members
        index1 = random.randint(0,3)
        index2 = random.randint(0,3)
        while (index1 == index2):
            index1 = random.randint(0,3)
            index2 = random.randint(0,3)
        # print index1, index2
        parent1 = population[index1]
        parent2 = population[index2]

        return parent1,parent2    # these two will reproduce