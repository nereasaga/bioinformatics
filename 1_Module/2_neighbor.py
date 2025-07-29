def neighbor(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}
    neighborhood = set()
    suffix_neighbors = neighbor(pattern[1:], d)
    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in "ACGT":
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)
    return neighborhood

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must have the same length")
    
    distance = 0 
    for a, b in zip(s1, s2):
        if a != b:
            distance += 1
    return distance

result = neighbor("ATGTGTTGA", 2)

print(" ".join(sorted(result)))