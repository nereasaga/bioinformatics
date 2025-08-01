from utils import hamming_distance
from itertools import product

# def total_distance(seq, pattern):
#     k = len(pattern)
#     return min(hamming_distance(seq[i:i+k], pattern) for i in range(len(seq) - k + 1))

# def median_string(dna_list, k):
#     nucleotides = ["A", "C", "G", "T"]
#     min_distance = float('inf')
#     median = None

#     # generate all kmers
#     for kmer in product(nucleotides, repeat=k):
#         kmer_str = ''.join(kmer)
#         distance = sum(total_distance(seq, kmer_str) for seq in dna_list)
#         if distance < min_distance:
#             min_distance = distance
#             median = kmer_str
#     return median

# calculate distance between pattern and substring
def distance_between_pattern_and_string(pattern, string):
    k = len(pattern)
    distances = []
    for i in range(len(string) - k + 1):
        substring = string[i:i+k]
        distances.append(hamming_distance(pattern, substring))
    return min(distances)

# calculate total distance between a pattern and a dna list
def total_distance(pattern, dna_list):
    return sum(distance_between_pattern_and_string(pattern, seq) for seq in dna_list)

def median_string(dna_list, k):
    nucleotides = ['A', 'C', 'G', 'T']
    min_distance = float('inf')
    median = None

    # generate all possible kmers
    for kmer_tuple in product(nucleotides, repeat=k):
        kmer = ''.join(kmer_tuple)
        dist = total_distance(kmer, dna_list)
        if dist < min_distance:
            min_distance = dist
            median = kmer
    return median



dna_list = [
    "TCGTGGGTAAGACTGATTGTTTCAATCAGGAGATAGCACAGC",
    "TACCTCGTCAGACCTGCTTAGTTCTAACTGTGCCAGACTTCA",
    "TGAGCACCAATGCTCTACGTGAGAGTTACTGGAATGGCGATA",
    "ATTACTGGTCAGGTTAGATAGTTCGAAAGGATGCACTGACGT",
    "CATGCTGGTTTCGCTACTGTTAGAAAATTGGGTTTAGACTTG",
    "GGAATCAGTCGCCATGTATTATATTCATGTGTAAGACCTTTG",
    "ATGCTTTCCGGCAATTGTGTGAGAGATGTCCAGGAGAGACCA",
    "GGTACCCAGGTCATATAGGACTCCTTCCTAGTAAGATCCAGT",
    "TCCTTGCCGTTCCCTCTACCTGCGGTAGGCGTCAGATTTCTG",
    "GGACATAAGTGAGATCACGAGCTCTAAATTATAGGTGTAAGA"

]

print(median_string(dna_list, 6))