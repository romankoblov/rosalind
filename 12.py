import itertools
a = [i for i in open('rosalind12.txt').read().split("\n") if i]
 
         
  
# determine the numerical overlap between two strings a,b
def overlap(a, b):
    best = 0
    for i in xrange(1, min(len(a), len(b))+1):
        if b.startswith(a[-i:]):
            best = i
    return best

def ol(a, b):
    return a+b[overlap(a, b):]  

print sorted([reduce(ol, i) for i in itertools.permutations(a)], key=lambda x:len(x))[0]
