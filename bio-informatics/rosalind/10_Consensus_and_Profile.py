# Consensus and Profile

f = open('input.txt', mode='rt', encoding='utf-8')
datas = f.read().replace('\n', '').split('>')[1:]
len_rosalind = len('Rosalind_0232')
for i in range(len(datas)):
  datas[i] = datas[i][len_rosalind:]

n = len(datas)
DNAs = ['A', 'C', 'G', 'T']
dna_len = len(datas[0])
dna_count = [{'A': 0, 'C': 0, 'G': 0, 'T': 0} for _ in range(dna_len)]

for i in range(n):
  for j in range(dna_len):
    dna_count[j][datas[i][j]] += 1

result = ''
for j in range(dna_len):
  max_dna = None
  max_count = 0
  for dna in DNAs:
    if(dna_count[j][dna] > max_count):
      max_dna = dna
      max_count = dna_count[j][dna]
  result += max_dna

print(result)
for dna in DNAs:
  print('{}: '.format(dna), end = '')
  for j in range(dna_len):
    print(dna_count[j][dna], end = ' ')
  print()