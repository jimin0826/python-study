## define mathematical function ##
def f(x):
  return x*x*x + 1

h = 0.0001
x = 2

def single_step_DF(x):
  return (f(x+h/2) - f(x-h/2)) / h
