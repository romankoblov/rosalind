import itertools
a = int(open('rosalind7.txt').read().replace("\n",''))
b = [[str(j) for j in i] for i in itertools.permutations(range(1, a+1))]
print len(b)
for i in b: print " ".join(i)
