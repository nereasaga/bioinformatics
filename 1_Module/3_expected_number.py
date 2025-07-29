k = 9
L = 1000
num_sequences = 500
nucleotid_size = 4

# K-mer size per sequence
kps = L - k + 1

# Probability of a specific k-mer occurring in a sequence
match_prob = 1 / (nucleotid_size ** k)

# Expected number of occurrences of a specific k-mer in one sequence
expected_ps = kps * match_prob

# Expected number of occurrences of a specific k-mer in multiple sequences
expected_total = expected_ps * num_sequences

print(f"Expected number of occurrences of a specific {k}-mer: {expected_total:.6f}")
