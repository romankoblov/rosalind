a = open('rosalind8.txt').read().split('\n')
data = {}

seq = None
for i in a:
    if i.startswith('>'): 
        seq = i.split('_')[2]
    else:
        if seq in data: 
            data[seq] += i
        else:
            data[seq] = i

a,b = sorted([(seq, round(len([i for i in data[seq] if i in ['C', 'G']])/float(len(data[seq])) * 100, 2)) for seq in data], key=lambda x:x[1])[::-1][0]
print 'Rosalind_Sequence_%s' % a
print "%s%%" % str(b)
