dna1 = str(input('Please input DNA sequence'))
compliment = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
dna2 = ''.join(compliment[b] for b in dna1[::-1])
print(dna2) 

    
