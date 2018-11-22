
def choose_bin(item, item_weight, bin_weights, construction_graph):

  total_pheromone = sum(construction_graph.get(item))
  weights = [(path_pheromone / total_pheromone) for path_pheromone in construction_graph.get(bin_number)]
  path_choices = range(len(construction_graph.get(bin_number)))
  
  chosen_bin = random.choices(path_choices, weights) # randomly select a bin (path) to take
  bin_weights[chosen_bin] += item_weight

  return bin_weights