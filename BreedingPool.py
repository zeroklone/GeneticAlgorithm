from Population import Population
from SelectionStrategies import SelectionStrategies
from RecombinationStrategies import RecombinationStrategies
from ReinsertionStrategies import ReinsertionStrategies
import random

class BreedingPool:
    def main(self):
        herd = Population(30)
        selection = SelectionStrategies()
        recombination = RecombinationStrategies()
        reinsertion = ReinsertionStrategies()
        herd.main()
        generations = 100
        # Display the first generation
        print "Generation 1"
        # for individual in range(1, len(herd.population)):
        #     print '--> ' .join(herd.population[individual]),
        #     print ' = ',herd.objective_values[individual], 'km'

        x = herd.objective_values
        population = herd.population
        for count in range(generations):
            population,x = selection.sort_by_fitness(population,x)
            parent1, parent2 = selection.tournament(population, x)

            child1,child2 = recombination.crossover(parent1, parent2)

            fitness_of_child1 = herd.get_total_distance(child1, herd.city_names, herd.routes)
            fitness_of_child2 = herd.get_total_distance(child2, herd.city_names, herd.routes)
            population,x = reinsertion.tournament(child1, child2, population, x, fitness_of_child1, fitness_of_child2)



            print "Generation ",count +2
            for individual in range(len(herd.population)):
                # print '--> ' .join(population[individual]),
                # print ' = ',x[individual], 'km'
                print ' ',x[individual],
            print 

            # print 'Ave',sum(x[1:])/len(x[1:])
if __name__ =='__main__':
    object_breeding_pool = BreedingPool()
    object_breeding_pool.main()