import random
from MutationStrategies import MutationStrategies
class RecombinationStrategies:
    def crossover(self, parent1, parent2):
        dna1 = parent1[2:]
        dna2 = parent2[2:]

        child1 = dna1[5:11]
        child2 = dna2[5:11]

        for chromosone in dna2:
            if chromosone not in child1:
                child1.append(chromosone)
        for chromosone in dna1:
            if chromosone not in child2:
                child2.append(chromosone)

        child1 = parent1[:2]+child1
        child2 = parent2[:2]+child2

        mutation = MutationStrategies()
        child1 = mutation.basic_shuffle(child1)

        return [child1, child2]