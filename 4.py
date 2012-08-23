a, b = [i for i in open('rosalind4.txt').read().split('\n') if i]

print " ".join([str(i+1) for i in range(0, len(a)) if a[i:i+len(b)] == b])
