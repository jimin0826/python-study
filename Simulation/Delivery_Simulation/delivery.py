import numpy as np
import math
import random

size_width = 3000
size_height = 3000
Order_Interval = 300

def nextTime(rateParameter):
  random.seed()
  return -math.log(1.0 - random.random()) / rateParameter

def generate_store_location(n) :
  store_location = []
  for x_section in range(n):
    for y_section in range(n):
      while(True):
        x, y = random.random(), random.random()
        if(x > x_section/n  and x < (x_section+1)/n and 
          y > y_section/n and y < (y_section+1)/n) :
          store_location.append((size_width * x, size_height * y))
          break
  return store_location

def generate_order_time(Time_Duration) :
  order_time = []
  cur_time = 0
  while(True):
    generate_interval = nextTime(1/Order_Interval)
    if(cur_time + generate_interval < Time_Duration):
      order_time.append(cur_time+generate_interval)
      cur_time += generate_interval
    else:
      break
  return order_time


def generate_order_location(n) :
  mu, sigma = 1500, 300
  order_locations = []
  for _ in range(n):
    x = random.gauss(mu, sigma)
    y = random.gauss(mu, sigma)
    while(True):
      if(x > 0 and x < size_width and y > 0 and y < size_height):
        order_locations.append((x, y))
        break
      else:
        x = random.gauss(mu, sigma)
        y = random.gauss(mu, sigma)

  return order_locations

def main() :
  random_store_location = generate_store_location(3)
  random_order_time = generate_order_time(3600)
  random_order_location = generate_order_location(len(random_order_time))
  print(random_order_location)

main()