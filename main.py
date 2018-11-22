import timeit
import init
import ant

def bin_packing(number_bins, number_items, evaporation_rate, ants):
  # initialise bins, items weights and evaluations
  item_weights = init.generate_item_weights(number_bins, number_items)
  fitness_evaluations = 5

  problem_graph = init.generate_construction_graph(number_bins, number_items)
  
  i = 0
  while i < fitness_evaluations:
    print('new run:', i)
    ant_optimisation(ants, item_weights, number_bins, problem_graph, evaporation_rate)
    i += 1

def ant_optimisation(ants, items, bins, problem_graph, evaporation_rate):
  '''[summary]
  
  Arguments:
    ants {int} -- number of ants being used in each iteration
    items {list} -- weight of each item
    bins {list} -- list of current bins weight
    problem_graph {dictionary} -- construction graph of problem space
  '''
  ant_paths = ant.generate_ant_paths(ants, items, problem_graph)
  for path in ant_paths:
    fitness_of_path = [ant.evaluate_fitness(path, items, bins)]
    problem_graph = ant.update_pheromone_fitness(path, fitness_of_path, problem_graph)
    problem_graph = ant.evaporate_pheromone(problem_graph, evaporation_rate)
    # print(problem_graph)


if __name__ == '__main__':
  bin_packing(3, 6, 0.9, 10)
