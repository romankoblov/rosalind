a = "".join([i for i in open('rosalind9.txt').read().split("\n") if i])

for i in range(0, len(a)):
    if len(a)-i < 4: break
    for j in range(4,9):
        if a[i:i+j] == a[i:i+j][::-1].replace('A', '1').replace('T', '2').replace('C','3').replace('G','4').replace('1', 'T').replace('2', 'A').replace('3','G').replace('4', 'C'):
            print i+1, j
