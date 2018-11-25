import timeit
import sys
import init
import ant

def bin_packing(number_bins, number_items, evaporation_rate, ants, item_weights):
  # initialise bins, items weights and evaluations
  # item_weights = init.generate_item_weights(number_bins, number_items)
  fitness_evaluations = 10000
  problem_graph = init.generate_construction_graph(number_bins, number_items)
  best_fitness, best_bin_config = 0, [0]*number_bins
  i = 0

  while i < fitness_evaluations:
    optimised_fitness, problem_graph, bin_config = ant_optimisation(ants, item_weights, number_bins, problem_graph, evaporation_rate, best_fitness, best_bin_config)
    if best_fitness < optimised_fitness:
      best_fitness = optimised_fitness
      best_bin_config = bin_config
    print('iteration: {}/10000. Current best Fitness: {}.'.format(i+1, best_fitness))
    i += 1
  return best_fitness, best_bin_config

def ant_optimisation(ants, items, bins, problem_graph, evaporation_rate, best_fitness, best_bin_config):
  '''[summary]
  
  Arguments:
    ants {int} -- number of ants being used in each iteration
    items {list} -- weight of each item
    bins {list} -- list of current bins weight
    problem_graph {dictionary} -- construction graph of problem space
  '''
  ant_paths = ant.generate_ant_paths(ants, items, problem_graph)

  for path in ant_paths:
    fitness_of_path, bin_config = ant.evaluate_fitness(path, items, bins)
    problem_graph = ant.update_pheromone_fitness(path, fitness_of_path, problem_graph)
    if best_fitness < fitness_of_path:
      best_fitness = fitness_of_path
      best_bin_config = bin_config
  problem_graph = ant.evaporate_pheromone(problem_graph, evaporation_rate)
  return best_fitness, problem_graph, best_bin_config


if __name__ == '__main__':
  result_files = ['p10-e0.4-bpp2.txt', 'p10-e0.9-bpp2.txt', 'p100-e0.4-bpp2.txt', 'p100-e0.9-bpp2.txt']
  evaporation_rate = [0.4, 0.9, 0.4, 0.9]
  ants = [10, 10, 100, 100]
  item_weights = init.generate_item_weights(50, 200)
    
  for index, x in enumerate(result_files):
    f = open('results/{}'.format(result_files[index]),"a")
    f.write('Item weights: {}.\n'.format(item_weights))
    
    for i in range(5):
      result, bin_config = bin_packing(50, 200, evaporation_rate[index], ants[index], item_weights)
      f.write('Resulting configuration: {}. With fitness {}.\n'.format(bin_config, result))
    print('Resulting configuration: {}. With fitness {}.'.format(bin_config, result))