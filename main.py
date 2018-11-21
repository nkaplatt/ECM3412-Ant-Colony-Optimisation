
'''
Set parameters, initialize pheromone trails;
while termination condition is not met do
  ConstructAntSolutions;
  ApplyLocalSearch (optional);
  UpdatePheromones;
'''
import random

def generate_construction_graph(bins, items):
  d = {}
  for i in range(items):
    d.update({i: [random.uniform(0,1) for _ in range(bins)]})
  return(d)

def generate_item_weights(bins, items):
  if bins == 50:
    weights = [(i*random.randrange(1, 201))/2 for i in range(items)]
  else:
    weights = [random.randrange(1, 201) for _ in range(items)]
  return weights

def bin_packing(number_bins, number_items, fitness_evaluations):
  # initialise bins and items weights
  item_weights = generate_item_weights(number_bins, number_items)
  current_bin_weight = dict.fromkeys(range(0, number_bins), 0)

  # start ant optimisation

  print(current_bin_weight)

def select_bin(bin_options):
  print('test')

def ant_optimisation(number_bins, number_items):
  graph = generate_construction_graph(number_bins, number_items)
  print('test')

if __name__ == '__main__':
  bin_packing(10, 200, 10000)
