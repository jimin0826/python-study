# Computing GC Content
import os

f = open('input.txt', mode='rt', encoding='utf-8')
textData = f.read()
dna_datas = textData.replace('\n', '').split('>')[1:]
n = len('Rosalind_1970')

max_index = 0
max_percent = 0

for i in range(len(dna_datas)):
  sum = dna_datas[i][n:].count('C')
  sum += dna_datas[i][n:].count('G')
  p = sum/len(dna_datas[i][n:])
  if(p > max_percent):
    max_index = i
    max_percent = p

print(max_percent* 100, dna_datas[max_index][:n])