from Population import Population
import random

class BreedingPool:
    def tournament_selection(self, population, objective_values):
        objective_values, population = zip(*sorted(zip(objective_values, population)))
        objective_values, population = (list(t) for t in zip(*sorted(zip(objective_values, population))))

        # Choose a breeding point from the top 4 members
        index1 = random.randint(0,3)
        index2 = random.randint(0,3)
        while (index1 == index2):
            index1 = random.randint(0,3)
            index2 = random.randint(0,3)
        # print index1, index2
        parent1 = population[index1]
        parent2 = population[index2]

        return [parent1,parent2, population, objective_values]    # these two will reproduce

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

        mutation = random.randint(1,4)
        if mutation == 2:
            mutation_position = random.randint(2,11)
            items = child1[mutation_position:mutation_position+3]
            random.shuffle(items)
            child1[mutation_position:mutation_position+3] = items


        return [child1, child2]

    def reinsertion(self, child1, child2, population, objective_values):
        # objective_values, population = zip(*sorted(zip(objective_values, population)))
        # objective_values, population = (list(t) for t in zip(*sorted(zip(objective_values, population))))

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


    def main(self):
        herd = Population(10)
        herd.main()
        generations = 50
        # Display the first generation
        print "Generation 1"
        for individual in range(1, len(herd.population)):
            print '--> ' .join(herd.population[individual]),
            print ' = ',herd.objective_values[individual], 'km'

        x = herd.objective_values
        population = herd.population
        for count in range(generations):
            breeding_pair = self.tournament_selection(population, x)
            population = breeding_pair[2]
            x= breeding_pair[3]

            children = self.crossover(breeding_pair[0], breeding_pair[1])

            new_generation = self.reinsertion(children[0], children[1], population, x)
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