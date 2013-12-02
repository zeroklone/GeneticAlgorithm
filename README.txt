READ ME
THIS CODE WAS WRITTEN BY MOTSE MARUMO LEHATA.
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
Feel free to copy and seed, as long as you give others that same right when you share you work. If you plan on making money from this software, I expect my fair share (TIA).

0. DESCRIPTION:
This module attempts to solve the Travelling Salesman problem (http://en.wikipedia.org/wiki/Travelling_salesman_problem) by implementing a genetic algorithm in Python

1. POPULATION:
Input
A list of all cities an the the paths between them is provided as a CSV file
Representation
A member of the population is represented as a directed graph in string form.

2. BREEDING POOL
2.1 Selection
The module makes use of tournament selection to populate the breeding pool. The x fittest members of a population are selected as potential parents. From there y breeding pairs are randomly selected.
To Do: Provide a choice of selection strategies

2.2 Recombination/Crossover
The simplest form of recombination is used, take a substring from each parent and combine then to make child. Some code is added to avoid duplicate nodes in a single child. Each breeding pair currently produces to unique offspring.
To Do: Provide a choice of recombination strategies

2.3 Reinsertion
The module makes use of tournament selection to insert offspring into a population . The x least fittest members of a population are selected as potential candidates for replacement. Y candidates are then randomly selected and replaced with the newly created offspring
To Do: Provide a choice of reinsertion

2.4 Mutation
Right now mutation just consists of shuffling a substring of a child before it is reinserted into the population. The actual purpose of mutation is to prevent premature convergance by introducing genetic diversity, right now I don't see this happening.

3. THINGS I STILL NEED TO DO:
Before I can even think of improving the BreedingPool class I need to fix a lot of minor things
	- Logically structure the entire module
	- Actually follow the Python Style Guide
	- Fix all the parts where I hardcoded values
	- I introduced some redundacy by using 'hacks' when i ran into trouble, I need to fix that.