a, b = [i for i in open('rosalind3.txt').read().split('\n') if i]

print len([i for i in xrange(0, len(a)) if a[i] != b[i]])
