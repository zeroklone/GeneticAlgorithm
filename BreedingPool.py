from Population import Population
from SelectionStrategies import SelectionStrategies
from RecombinationStrategies import RecombinationStrategies
from ReinsertionStrategies import ReinsertionStrategies
import random

class BreedingPool:
    def main(self):
        herd = Population(10)
        selection = SelectionStrategies()
        recombination = RecombinationStrategies()
        reinsertion = ReinsertionStrategies()
        herd.main()
        generations = 10
        # Display the first generation
        print "Generation 1"
        for individual in range(1, len(herd.population)):
            print '--> ' .join(herd.population[individual]),
            print ' = ',herd.objective_values[individual], 'km'

        x = herd.objective_values
        population = herd.population
        for count in range(generations):
            [population,x] = selection.sort_by_fitness(population,x)
            breeding_pair = selection.tournament(population, x)

            children = recombination.crossover(breeding_pair[0], breeding_pair[1])

            new_generation = reinsertion.tournament(children[0], children[1], population)
            x[8] = herd.get_total_distance(children[0], herd.city_names, herd.routes)
            x[9] = herd.get_total_distance(children[1], herd.city_names, herd.routes)

            population = new_generation
            print "Generation ",count +2
            for individual in range(len(herd.population)):
                print '--> ' .join(population[individual]),
                print ' = ',x[individual], 'km'

            print 'Ave',sum(x[1:])/len(x[1:])
if __name__ =='__main__':
    object_breeding_pool = BreedingPool()
    object_breeding_pool.main()