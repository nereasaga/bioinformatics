def find_clumps(genome, k, L, t):
    clumps = set()
    freq = {}
    
    # Freq in 1st window
    window = genome[0:L]
    for i in range(L - k + 1):
        pattern = window[i:i+k]
        freq[pattern] = freq.get(pattern, 0) + 1

    # add k-mers where >= 3 in 1st window
    for pattern, count in freq.items():
        if count >= t:
            clumps.add(pattern)

    # Move window
    for i in range(1, len(genome) - L + 1):
        # remove k-mer
        first_kmer = genome[i-1 : i-1 + k]
        freq[first_kmer] -= 1
        if freq[first_kmer] == 0:
            del freq[first_kmer]

        # add k-mer
        last_kmer = genome[i + L - k : i + L]
        freq[last_kmer] = freq.get(last_kmer, 0) + 1

        # check if meets condition
        if freq[last_kmer] >= t:
            clumps.add(last_kmer)

    return clumps

with open('./Genomes_data/E_coli.txt', 'r') as file:
    genome = file.read().strip()

k = 9
L = 500
t = 3

clumps = find_clumps(genome, k, L, t)
print(len(clumps))

