READ ME
THIS CODE WAS WRITTEN BY MOTSE MARUMO LEHATA.
	This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
	Feel free to copy and seed, as long as you give others that same right when you share you work. If you plan on making money from this software, I expect my fair share (TIA).

This module attempts to solve the Travelling Salesman problem (http://en.wikipedia.org/wiki/Travelling_salesman_problem) by implementing a genetic algorithm in Python

Population
	Input
	A list of all cities an the the paths between them is provided as a CSV file
	Representation
	A member of the population is represented as a directed graph in string form.

Breeding Pool
	Selection
	The module makes use of tournament selection to populate the breeding pool. The x fittest members of a population are selected as potential parents. From there y breeding pairs are randomly selected.
	To Do: Provide a choice of selection strategies

	Recombination/Crossover
	The simplest form of recombination is used, take a substring from each parent and combine then to make child. Some code is added to avoid duplicate nodes in a single child. Each breeding pair currently produces to unique offspring.
	To Do: Provide a choice of recombination strategies

	Reinsertion
	The module makes use of tournament selection to insert offspring into a population . The x least fittest members of a population are selected as potential candidates for replacement. Y candidates are then randomly selected and replaced with the newly created offspring
	To Do: Provide a choice of selection strategies


