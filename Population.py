import csv, random, os.path

class Population:
    def __init__(self, population_size):
        self.routes = []
        self.city_names = []
        self.population = []
        self.objective_values = []
        self.population_size = population_size

    def get_raw_data(self, filename, delim):
        with open(filename,'rb') as csv_file:
            reader = csv.reader(csv_file, delimiter=delim)
            data = []
            for row in reader:
                data.append(row)
            return data
 
    def to_string(self, csv_list):
        for row in csv_list:
            print ', ' .join(row)

    def get_route_distance(self, A, B, list_of_city_names,list_of_routes):
        # calculate the distance between point A and point B
        A,B = A.upper(), B.upper()
        # print A,' --> ',B,
        # get the index of the destination city and refer to it by its index from here on
        index_of_B = list_of_city_names.index(B)

        # now find the distance between A and B
        for row in list_of_routes:
            #print ', ' .join(row)
            if row[0] == A:
                distance = row[index_of_B]
                return int(distance)
        print "At least one of the cities you entered is invalid, returning 0!"
        return 0

    def get_total_distance(self, individual, list_of_city_names, list_of_routes): # caclulate the objective value for solution (total distance)
        number_of_cities = len(individual)
        total_distance = 0
        for count in range(1, number_of_cities -1):
            origin = individual[count]              # the city you are at
            destination = individual[count+1]       # The city you are travelling to next
            total_distance += self.get_route_distance(origin, destination, list_of_city_names,list_of_routes)
        return total_distance


    def set_first_generation(self, list_of_city_names):
        # using a list of all the cities, generate a random population of ten individuals
        # the first city in the list should be the head node of each individual
        f = open('first_generation.csv','wb')
        # print list_of_city_names
        size = self.population_size # size of the population
        for count in range(size): # generate a random route starting at the first city
            items = list_of_city_names[2:]
            random.shuffle(items) # shuffles the order of the cities, excluding the first city
            individual = list_of_city_names[:2] + items
            string = ''
            for element in individual:
                string = string +','+element
            f.write(string[1:])
            f.write('\n')
        
        f.close()

    def get_first_generation(self): # if an initial population has already been created simply read it in
        population = self.get_raw_data('first_generation.csv',',')
        return population

    def main(self):
        routes = self.get_raw_data('distances.csv',',')
        list_of_city_names = routes[0]
        del routes[0]
        # print route_distance("sku", "rust", distances)
        if os.path.isfile('first_generation.csv'): # Don't generate a new population every time the script is run
            print "first_generation.csv found."
            population = self.get_first_generation()
        else:
            print "generating first_generation.csv"
            self.set_first_generation(list_of_city_names)
            population = self.get_first_generation()

        objective_values = []
        for individual in population:   # calculate the total distance for a route
            total_distance = self.get_total_distance(individual, list_of_city_names, routes)
            # print total_distance
            objective_values.append(total_distance)

        self.routes = routes
        self.city_names = list_of_city_names
        self.population = population
        self.objective_values = objective_values


    if __name__ == "__main__":
        main()