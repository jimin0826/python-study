sequence = [1, 2, 3, 4, 5]
obj_iter = iter(sequence)
while True:
  try:
    value = next(obj_iter)
  except StopIteration:
    break
  print(value)