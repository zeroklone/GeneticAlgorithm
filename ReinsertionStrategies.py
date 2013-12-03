import random
class ReinsertionStrategies:
    def tournament(self, child1, child2, population, fitness_functions,fitness_of_child1, fitness_of_child2):
        # Choose a breeding point from the top 4 members
        length = len(population)-1
        # print population

        index1 = random.randint(length-3,length)
        index2 = random.randint(length-3,length)
        while (index1 == index2):
            index1 = random.randint(length-3,length)
            index2 = random.randint(length-3,length)
        
        print index1, index2

        population[index1] = child1
        population[index2] = child2
        fitness_functions[index1] = fitness_of_child1
        fitness_functions[index2] = fitness_of_child2 

        return population, fitness_functions
