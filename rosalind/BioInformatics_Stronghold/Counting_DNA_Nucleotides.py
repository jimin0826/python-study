# rosalind BioInformatics Stronghold 
# Counting DNA Nucleotides

dna_string = input()
counting_dna = {
  'A': 0, 'C': 0, 'G': 0, 'T': 0,
}

for alphabet in dna_string :
  counting_dna[alphabet] += 1

print(
  counting_dna['A'], 
  counting_dna['C'],
  counting_dna['G'],
  counting_dna['T']
)

# print(*map(input().count, "ACGT"))