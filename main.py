import init
import ant

def bin_packing(number_bins, number_items, evaporation_rate, ants):
  # initialise bins, items weights and evaluations
  item_weights = init.generate_item_weights(number_bins, number_items)
  current_bin_weight = dict.fromkeys(range(0, number_bins), 0) # all bins start empty
  fitness_evaluations = 10000

  # start ant optimisation
  
  print(current_bin_weight)

def ant_optimisation(ants, number_bins, item_weights, bins):
  '''[summary]
  
  Arguments:
    number_bins {[type]} -- [description]
    number_items {[type]} -- [description]
    bins {[type]} -- [description]
  '''

  graph_of_pheromones = init.generate_construction_graph(number_bins, number_items)
  print('test')

if __name__ == '__main__':
  bin_packing(10, 200)
