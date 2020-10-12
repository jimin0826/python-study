# Complementing a Strand of DNA

import sys

dna_string = sys.stdin.readline().strip()
result = ''
for i in reversed(dna_string):
  if(i == 'A'):
    result += i.replace('A', 'T', 2)
  elif(i == 'T'):
    result += i.replace('T', 'A', 2)
  elif(i == 'C'):
    result += i.replace('C', 'G', 2)
  else:
      result += i.replace('G', 'C', 2)
print(result)