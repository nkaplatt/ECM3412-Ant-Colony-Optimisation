
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

def generate_item_weights(items):
  return [random.randrange(1, 201) for _ in range(items)]

def bin_packing(number_bins, number_items, fitness_evaluations):
  graph = generate_construction_graph(number_bins, number_items)
  item_weights = generate_item_weights(number_items)

def ant_optimisation(number_bins, number_items):
  print('test')

if __name__ == '__main__':
  bin_packing(50, 200, 10000)
