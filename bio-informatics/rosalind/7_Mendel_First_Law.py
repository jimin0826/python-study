f = open('input.txt', 'r')
sets = f.readlines()
f.close()

for population in sets:
    k, m, n = map(float, population.split())
    t = k+m+n
    pk = k/t
    pm = m/t
    pn = n/t

    prob = 1
    prob -= pn*((n-1)/(t-1))
    prob -= 2*pn*(m/(t-1))*0.5
    prob -= pm*((m-1)/(t-1))*0.25
    print(prob)