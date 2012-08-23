a = [i for i in open('rosalind6.txt').read().split('\n') if i]

print "".join([sorted([(k, [j[i] for j in a].count(k)) for k in ('A','T','G','C')], key=lambda x:x[1])[::-1][0][0] for i in range(0, len(a[0]))])
