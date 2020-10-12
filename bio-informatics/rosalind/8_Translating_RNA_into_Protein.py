# Translating RNA into Protein

protein_dict = {
  'UUU': 'F',     'CUU': 'L',      'AUU': 'I',      'GUU': 'V',
  'UUC': 'F',      'CUC': 'L',      'AUC': 'I',      'GUC': 'V',
  'UUA': 'L',      'CUA': 'L',      'AUA': 'I',      'GUA': 'V',
  'UUG': 'L',      'CUG': 'L',      'AUG': 'M',      'GUG': 'V',
  'UCU': 'S',      'CCU': 'P',      'ACU': 'T',      'GCU': 'A',
  'UCC': 'S',      'CCC': 'P',      'ACC': 'T',      'GCC': 'A',
  'UCA': 'S',      'CCA': 'P',      'ACA': 'T',      'GCA': 'A',
  'UCG': 'S',      'CCG': 'P',      'ACG': 'T',      'GCG': 'A',
  'UAU': 'Y',      'CAU': 'H',      'AAU': 'N',      'GAU': 'D',
  'UAC': 'Y',      'CAC': 'H',      'AAC': 'N',      'GAC': 'D',
  'UAA': 'Stop',   'CAA': 'Q',      'AAA': 'K',      'GAA': 'E',
  'UAG': 'Stop',   'CAG': 'Q',      'AAG': 'K',      'GAG': 'E',
  'UGU': 'C',      'CGU': 'R',      'AGU': 'S',      'GGU': 'G',
  'UGC': 'C',      'CGC': 'R',      'AGC': 'S',      'GGC': 'G',
  'UGA': 'Stop',   'CGA': 'R',      'AGA': 'R',      'GGA': 'G',
  'UGG': 'W',      'CGG': 'R',      'AGG': 'R',      'GGG': 'G',
}

f = open('input.txt', mode='rt', encoding='utf-8')
rna_string = f.read().strip()
f.close()

protein = ''
for triple in range(len(rna_string)//3):
  protein_code = protein_dict[rna_string[triple*3 : triple*3+3]]
  if (protein_code != 'Stop'):
    protein += protein_code

print(protein)

