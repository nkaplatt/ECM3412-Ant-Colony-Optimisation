import random

def generate_ant_paths(number_of_ants, items, graph):
  '''[summary]
  
  Arguments:
    number_of_ants {int} -- [description]
    items {list} -- [description]
    graph {dictionary} -- [description]
  
  Returns:
    [type] -- [description]
  '''

  paths = []
  for ant in range(number_of_ants):
    paths.append([choose_bin(index, graph) for index, item in enumerate(items)])
  return paths

def choose_bin(item_number, graph):
  '''[summary]
  
  Arguments:
    item_number {[type]} -- [description]
    graph {[type]} -- [description]
  
  Returns:
    {int} -- [description]
  '''
  total_pheromone = sum(graph.get(item_number))
  weights = [(path_pheromone / total_pheromone) for path_pheromone in graph.get(item_number)]
  path_choices = range(len(graph.get(item_number)))
  chosen_bin = random.choices(path_choices, weights) # randomly select a bin (path) to take, returns as a list
  return chosen_bin[0] # to just return the int

def evaporate_pheromone(graph, e_rate):
  '''Reduces the amount of pheromone each path has by a certain percentage
  
  Arguments:
    graph {dictionary} -- construction graph of problem space
    e_rate {float} -- evaporation rate of pheromones
  
  Returns:
    [dictionary] -- construction graph of problem space with updated pheromones
  '''

  for item_number, pheromone_values in graph.items():
    graph[item_number] = [p*e_rate for p in pheromone_values]
  return graph

def update_pheromone_fitness(path, fitness_of_path, problem_graph):
  '''[summary]
  
  Arguments:
    path {[type]} -- [description]
    fitness_of_path {[type]} -- [description]
    problem_graph {[type]} -- [description]
  
  Returns:
    [type] -- [description]
  '''

  for index, choice in enumerate(path):
    problem_graph.get(index)[choice] += fitness_of_path # doing *= converges all pheromones to 0 and errors out
  return problem_graph

def evaluate_fitness(path, items, bins):
  '''Function determines how good a path is taken by an Ant.
  
  Arguments:
    bins {int} -- number of bins in problem
    path {list}
    items {list} -- 
  
  Returns:
    [float] -- 100 divided by the difference of largest minus smallest weight
  '''
  bins = [0]*bins # list of bins with weight initialised at 0
  for path_choice, item in zip(path, items): # iterate through items and add to chosen bin
    bins[path_choice] += item
  return (max(bins) - min(bins)), bins