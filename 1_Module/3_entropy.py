import math

nucleotides = ['A', 'C', 'G', 'T']

# calculate entropy of column
def entropy_column(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

#calculate total entropy of profile matrix
def total_entropy(p_matrix):
    return sum(entropy_column(col) for col in p_matrix)

# build profile matrix from sequences
def build_p_matrix(sequences):
    k = len(sequences[0])
    profile = []
    for i in range(k):
        column = [seq[i] for seq in sequences]
        total = len(column)
        counts = [column.count(nuc) / total for nuc in nucleotides]
        profile.append(counts)
    return profile



motifs = [
    "TCGGGGGTTTTT",
    "CCGGTGACTTAC",
    "ACGGGGATTTTC",
    "TTGGGGACTTTT",
    "AAGGGGACTTCC",
    "TTGGGGACTTCC",
    "TCGGGGATTCAT",
    "TCGGGGATTCCT",
    "TAGGGGAACTAC",
    "TCGGGTATAACC",
]

profile = build_p_matrix(motifs)
# calc total entropy
entropy = total_entropy(profile)

for i, col in enumerate(profile):
    print(f"Position {i+1}:")
    for nuc, prob in zip(nucleotides, col):
        print(f"{nuc}: {prob:.3f}")

print(entropy)


# profile = [
#     [0.7, 0.2, 0.0, 0.1],
#     [0.2, 0.2, 0.0, 0.6],
#     [0.0, 0.0, 1.0, 0.0],
#     [0.0, 0.0, 1.0, 0.0],
#     [0.1, 0.0, 0.9, 0.0],
#     [0.1, 0.0, 0.9, 0.0],
#     [0.0, 0.9, 0.1, 0.0],
#     [0.5, 0.1, 0.0, 0.4],
#     [0.8, 0.1, 0.0, 0.1],
#     [0.7, 0.1, 0.0, 0.2],
#     [0.3, 0.3, 0.0, 0.4],
#     [0.4, 0.0, 0.0, 0.6],
# ]