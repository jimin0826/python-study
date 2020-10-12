# Finding a Motif in DNA

f = open('input1.txt', mode='rt', encoding='utf-8')
g = open('input2.txt', mode='rt', encoding='utf-8')
s = f.read().strip()
t = g.read().strip()
f.close()
g.close()

n = len(s)
m = len(t)
locations = []

for i in range(n-m):
  if(s[i : i+m] == t):
    locations.append(i+1)

print(*locations)
