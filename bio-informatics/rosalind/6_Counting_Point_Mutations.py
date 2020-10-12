# Counting Point Mutations
# Evolution as a Sequence of Mistakes

def main():
  DNA1 = input()
  DNA2 = input()
  hamming_distance = 0

  for i in range(len(DNA1)):
    if(DNA1[i] != DNA2[i]):
      hamming_distance += 1
  print(hamming_distance)

main()