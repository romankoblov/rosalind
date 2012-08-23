a = open('rosalind1.txt').read()
print len([i for i in a if i=='A']), len([i for i in a if i=='C']), len([i for i in a if i=='G']), len([i for i in a if i=='U'])

