import random

def generate_construction_graph(bins, items):
  '''Create a dictionary of length 'items' whereby keys correspond to the 
  the item 1,...,200. Value pairs are lists of pheromone levels to each bin whereby
  the index of the list is the corresponding bin e.g. index[2] is pheromone leading to bin 3. 
  
  Arguments:
    bins {int} -- number of bins in the problem space
    items {int} -- number of items with weight in the problem space

  Returns:
    {dictionary} -- construction graph of problem space
  '''

  d = {}
  for i in range(items):
    d.update({i: [random.uniform(0,1) for _ in range(bins)]})
  return d

def generate_item_weights(bins, items):
  if bins == 50:
    weights = [((i+1)*random.randrange(1, 201))/2 for i in range(items)] # BBP2
  else:
    weights = [random.randrange(1, 201) for _ in range(items)] # BBP1
  return weights