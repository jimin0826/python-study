import sys

dna_string = sys.stdin.readline().strip()
rna_string = ''

for i in range(len(dna_string)):
  if (dna_string[i] == 'T'):
    rna_string += 'U'
  else:
    rna_string += dna_string[i]
  
print(rna_string)