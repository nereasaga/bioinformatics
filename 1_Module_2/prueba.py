def hamming_distance(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

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

def frequent_words_with_mismatches(text, k, d):
    freq_map = {}
    n = len(text)

    for i in range(n - k + 1):
        pattern = text[i:i + k]
        print(f"\nOriginal pattern: {pattern}")
        neighborhood = neighbors(pattern, d)
        print(f"Neighbors ({len(neighborhood)}): {sorted(neighborhood)}")

        for neighbor in neighborhood:
            freq_map[neighbor] = freq_map.get(neighbor, 0) + 1

    print("\n--- Final Frequency Map ---")
    for kmer, count in sorted(freq_map.items()):
        print(f"{kmer}: {count}")

    max_count = max(freq_map.values())
    return [pattern for pattern, count in freq_map.items() if count == max_count]


text = "ACGTACTTATA"
k = 3
d = 1
result = frequent_words_with_mismatches(text, k, d)
print("\nMost frequent k-mers with up to 1 mismatch:")
print(result)