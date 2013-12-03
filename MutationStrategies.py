import random

class MutationStrategies:
    def basic_shuffle(self, child):
        mutation = random.randint(1,4) # TO DO: Make this range variable
        if mutation == 2:
            mutation_position = random.randint(2,11) # TO DO: Make this range variable
            items = child[mutation_position:mutation_position+3]
            random.shuffle(items)
            child[mutation_position:mutation_position+3] = items
        return child