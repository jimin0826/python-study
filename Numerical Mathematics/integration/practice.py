import math

def function(x) :
  return abs(math.sin(x)) 

def fun_der(x) :
  if x >= 0 :
    return math.cos(x)
  else :
    return -math.cos(x)

def trapezoidal(n, a, b) :
  result = 0
  h = (b - a) / n
  for i in range(1, n+1) :
    x_i_1 = a + h * (i-1)
    x_i = a + h * i
    result +=  h / 2 * (function(x_i_1) + function(x_i))
  return result

def simpson(n, a, b) :
  result = 0
  h = (b - a) / n
  for i in range(1, (int)(n/2)) :
    x_2i_2 = a + h * (2*i - 2)
    x_2i_1 = a + h * (2*i - 1)
    x_2i = a + h * 2 * i
    result += h / 3 * (function(x_2i_2) + function(x_2i_1) * 4 + function(x_2i))
  return result

def hermite(n, a, b) :
  result = 0
  h = (b - a) / n
  for i in range(1, n+1) :
    x_i_1 = a + h * (i-1)
    x_i = a + h * i
    result += h / 2 * (function(x_i_1) + function(x_i)) + h*h/12*(fun_der(x_i_1) - fun_der(x_i))
  return result


def Exercise() :
  a = -math.pi / 2
  b = math.pi / 2
  print("<<Trapezoidal rule>>")
  for n in [10, 20, 40, 80] :
    print("n = {} : estimated integration = {}, error = {}".format(
      n, trapezoidal(n, a, b), 2 - trapezoidal(n, a, b)))
  print("<<Simpson's rule>>")
  for n in [10, 20, 40, 80] :
    print("n = {} : estimated integration = {}, error = {}".format(
      n, simpson(n, a, b), 2 - simpson(n, a, b)))
  print("<<Hermite rule>>")
  for n in [10, 20, 40, 80] :
    print("n = {} : estimated integration = {}, error = {}".format(
      n, hermite(n, a, b), 2 - hermite(n, a, b)))
