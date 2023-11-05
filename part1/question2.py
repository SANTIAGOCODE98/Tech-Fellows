def swapper(t):
  return t[1],t[0]

def run_swapper(list_of_tuples):
  return list(map(swapper, list_of_tuples))