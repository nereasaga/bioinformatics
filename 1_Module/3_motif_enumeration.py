from utils import hamming_distance, neighbors, countD

def motif_enumeration(dna, k, d):
    patterns = set()
    first_string = dna[0]

    for i in range(len(first_string) - k + 1):
        pattern = first_string[i:i+k]
        neighborhood = neighbors(pattern, d)
        for neighbor in neighborhood:
            is_motif = True
            if all(countD(string, neighbor, d) > 0 for string in dna[1:]):
                patterns.add(neighbor)
    return patterns

dna = ["CTTGATACCGACAAGCCTAATTGCG", "AATGCCTCGTCCCAGCTTTCTATTC", "TCTAGTTGCTTGCATAAAGATGATG", "TAGGCCTGGTCCAGTCCCAGTCCCT", "CCAAGACGACCAGACTAGCGTTTGA", "TCTAGGAGTGTGAATCTAGCCCACA"]

# print(motif_enumeration(dna, 5, 2))
print(" ".join(motif_enumeration(dna, 5, 2)))
        
