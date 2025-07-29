# 1st MODULE

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

# Most frequent k-mers in genome
def frequency_table(text, k):
    freq_map = {}
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        if pattern not in freq_map:
            freq_map[pattern] = 1
        else:
            freq_map[pattern] += 1
    return freq_map

# max value in frequency map
def max_map(freq_map):
    return max(freq_map.values())

# most freq k-mers + return as list
def better_frequent_words(text, k):
    frequent_patterns = []
    freq_map = frequency_table(text, k)
    max_count = max_map(freq_map)

    for pattern in freq_map:
        if freq_map[pattern] == max_count:
            frequent_patterns.append(pattern)

    return frequent_patterns

# find number of times a pattern appears in genome
def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

# find pattern positions in genome (i)
def find_pattern_positions(pattern, genome):
    positions = []
    pattern_length = len(pattern)
    genome_length = len(genome)
    
    for i in range(genome_length - pattern_length + 1):
        substring = genome[i:i+pattern_length]
        if substring == pattern:
            positions.append(i)
    positions_str = ' '.join(str(pos) for pos in positions)
    return positions_str

# find reverse complement of a pattern
def reverse_complement(pattern):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return ''.join(complement[nuc] for nuc in reversed(pattern))

# 2nd MODULE

# find GC skew in genome
def skew(text):
    skew_value = 0
    skew_list = [0]

    for nucleotide in text:
        if nucleotide == "G":
            skew_value += 1
        elif nucleotide == "C":
            skew_value -= 1
        skew_list.append(skew_value)
    return skew_list

# find min and max positions of skew in genome
def min_skew_position(text):
    skew_values = skew(text)
    min_value = min(skew_values)
    positions = [i for i, value in enumerate(skew_values) if value == min_value]
    return positions

def max_skew_position(text):
    skew_values = skew(text)
    max_value = max(skew_values)
    positions = [i for i, value in enumerate(skew_values) if value == max_value]
    return positions

# find hamming distance between 2 strings
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Strings must have the same length")
    
    distance = 0 
    for a, b in zip(s1, s2):
        if a != b:
            distance += 1
    return distance

# find all positions of pattern in text with at most d mismatches
def pattern_matching(text, pattern, d):
    positions = []
    k = len(pattern)
    for i in range(len(text) - k + 1):
        substring = text [i:i+k]
        if hamming_distance(pattern, substring) <= d:
            positions.append(i)

    return positions

# count t of pattern in text with at most d mismatches
def countD(text2, pattern, d):
    count = 0
    k = len(pattern)
    for i in range(len(text2) - k + 1):
        substring = text2[i:i+k]
        if hamming_distance(pattern, substring) <= d:
            count += 1
    return count

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