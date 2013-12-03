import random

class MutationStrategies:
    def basic_shuffle(self, child):
        mutation = random.randint(1,16) # TO DO: Make this range variable
        if mutation == 2:
            mutation_position = random.randint(2,9) # TO DO: Make this range variable
            items = child[mutation_position:mutation_position+5]
            random.shuffle(items)
            child[mutation_position:mutation_position+3] = items
            print "Mutation occurred"
        return child