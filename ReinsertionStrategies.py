import random
class ReinsertionStrategies:
    def tournament(self, child1, child2, population):
        # Choose a breeding point from the top 4 members
        length = len(population)-1
        # print population

        index1 = random.randint(length-3,length)
        index2 = random.randint(length-3,length)
        while (index1 == index2):
            index1 = random.randint(length-3,length)
            index2 = random.randint(length-3,length)
        population[index1] = child1
        population[index2] = child2

        return population
