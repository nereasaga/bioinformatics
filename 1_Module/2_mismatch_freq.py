from utils import hamming_distance

# find all neighbors of a pattern with up to d mismatches, generate k-mers with d mismatches
def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}

    neighborhood = set()
    suffix_neighbors = neighbors(pattern[1:], d)

    for text in suffix_neighbors:
        if hamming_distance(pattern[1:], text) < d:
            for nucleotide in "ACGT":
                neighborhood.add(nucleotide + text)
        else:
            neighborhood.add(pattern[0] + text)

    return neighborhood

# find frequent k-mers with up to d mismatches in genome
def frequent_words_with_mismatches(text, k, d):
    freq_map = {}

    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        neighborhood = neighbors(pattern, d)
        for approx_pattern in neighborhood:
            if approx_pattern not in freq_map:
                freq_map[approx_pattern] = 1
            else:
                freq_map[approx_pattern] += 1

    max_freq = max(freq_map.values())

    return [pattern for pattern in freq_map if freq_map[pattern] == max_freq]

# find reverse complement of a pattern
def reverse_complement(pattern):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return ''.join(complement[nuc] for nuc in reversed(pattern))

# find frequent k-mers with up to d mismatches + their reverse complements
def frequent_words_mismatch_reverse(text, k, d):
    freq_map = {}

    for i in range(len(text) - k + 1):
        pattern = text[i:i + k]
        neighborhood = neighbors(pattern, d)

        for neighbor in neighborhood:
            rev_neighbor = reverse_complement(neighbor)
            freq_map[neighbor] = freq_map.get(neighbor, 0) + 1
            freq_map[rev_neighbor] = freq_map.get(rev_neighbor, 0) + 1

    max_count = max(freq_map.values())
    return [pattern for pattern, count in freq_map.items() if count == max_count]


text = "CATGCCATTCGCATTGTCCCAGTGA"
k = 7
d = 3

print(frequent_words_with_mismatches(text, k, d))

with open("./Genomes_data/Salmonella_enterica.txt", "r") as file:
    genome = ''.join(line.strip() for line in file if not line.startswith('>'))

# GC skew in 3818640, find frequent k-mers with mismatches in a window of 1000 nt
center = 3818640
window_size = 1000
half_window = window_size // 2
window_seq = genome[center - half_window : center + half_window]

kmers = frequent_words_mismatch_reverse(window_seq, k=9, d=1)
print(kmers)


# result = frequent_words_mismatch_reverse(text, k, d)
# print(" ".join(result))

# from collections import defaultdict

# def group_similar_kmers(kmers, max_distance=1):
#     groups = []
#     visited = set()

#     for i in range(len(kmers)):
#         if kmers[i] in visited:
#             continue
#         group = [kmers[i]]
#         visited.add(kmers[i])
#         for j in range(i + 1, len(kmers)):
#             if kmers[j] not in visited and hamming_distance(kmers[i], kmers[j]) <= max_distance:
#                 group.append(kmers[j])
#                 visited.add(kmers[j])
#         groups.append(group)
    
#     return groups

# kmers = [
#     'CTGCCGGCG', 'CGCCGGCAG', 'CTTCTGGCG', 'CGCCAGAAG', 
#     'TCTGGCGGT', 'ACCGCCAGA', 'GCGCTGCCG', 'CGGCAGCGC', 
#     'CGCCGCCTG', 'CAGGCGGCG', 'GCCAGCTGC', 'GCAGCTGGC'
# ]

# groups = group_similar_kmers(kmers, max_distance=2)

# for i, group in enumerate(groups):
#     print(f"Grupo {i+1}:")
#     for seq in group:
#         print(" ", seq)
# print(" ".join(group))

# pattern_positions = []

# for i in range(len(window_seq) - 9 + 1):
#     window = window_seq[i:i+9]
#     for group in groups:
#         for pattern in group:
#             if hamming_distance(window, pattern) <= 1:
#                 pattern_positions.append(i)
#                 break  


# import matplotlib.pyplot as plt

# plt.hist(pattern_positions, bins=50, color='skyblue', edgecolor='black')
# plt.title("Distribución de patrones similares en la ventana")
# plt.xlabel("Posición en la ventana (1000 nt)")
# plt.ylabel("Frecuencia")
# plt.show()



# from collections import Counter

# peak_start = 930
# peak_end = 955

# # flatten patterns from all groups into a single set
# all_patterns = set(p for group in groups for p in group)

# # create set of neighbors for all patterns with d=1
# neighbor_set = set()
# for pattern in all_patterns:
#     neighbor_set.update(neighbors(pattern, d=1))

# pattern_counts = Counter()

# # count patterns in specified peak range
# for i in range(peak_start, peak_end - 9 + 1):
#     window = window_seq[i:i+9]
#     if window in neighbor_set:
#         pattern_counts[window] += 1

# # show most common patterns in peak
# sorted_patterns = pattern_counts.most_common()
# print("Patrones más frecuentes en pico de histograma:")
# for pattern, count in sorted_patterns:
#     print(f"{pattern}: {count} veces")


print(frequent_words_with_mismatches("CATGCCATTCGCATTGTCCCAGTGA", 3, 1))