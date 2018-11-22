
def generate_ant_path(number_of_ants, items, graph):
  paths = []
  for ant in range(number_of_ants):
    paths.append([choose_bin(index, graph) for item, index in enumerate(items)])
  return paths

def choose_bin(item_number, graph):

  total_pheromone = sum(graph.get(item_number))
  weights = [(path_pheromone / total_pheromone) for path_pheromone in graph.get(bin_number)]
  path_choices = range(len(graph.get(bin_number)))
  
  chosen_bin = random.choices(path_choices, weights) # randomly select a bin (path) to take
  return chosen_bin
