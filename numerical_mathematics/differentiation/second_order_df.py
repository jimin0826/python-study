
## define mathematical function ##
def f(x):
  return x*x*x + 1

h = 0.0001
x = 2

def single_step_DF(x):
  return (f(x+h/2) - f(x-h/2)) / h

def BDF2(x):
  result = 0
  result += (3 * f(x) - 4 * f(x-h) + f(x-2*h))
  return result / (2*h)

def BDF3(x):
  result = 0
  result += (11*f(x) - 18*f(x - h) + 9*f(x- 2*h) - 2*f(x - 3*h))
  return result / (6*h)

print("Single Step Derivative at x = {} >> {}, error = {}".format(x, single_step_DF(x), (12-single_step_DF(x))/12*100))
print("BDF2 Derivative at x = {} >> {}, error = {}".format(x, BDF2(x), (12-BDF2(x))/12*100))
print("BDF3 Derivative at x = {} >> {}, error = {}".format(x, BDF3(x), (12-BDF3(x))/12*100))

