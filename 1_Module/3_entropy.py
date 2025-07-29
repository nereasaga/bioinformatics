import math

# calculate entropy of column
def entropy_column(probs):
    return -sum(p * math.log2(p) for p in probs if p > 0)

#calculate total entropy of profile matrix
def total_entropy(p_matrix):
    return sum(entropy_column(col) for col in p_matrix)

profile = [
    [0.7, 0.2, 0.0, 0.1],
    [0.2, 0.2, 0.0, 0.6],
    [0.0, 0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0, 0.0],
    [0.1, 0.0, 0.9, 0.0],
    [0.1, 0.0, 0.9, 0.0],
    [0.0, 0.9, 0.1, 0.0],
    [0.5, 0.1, 0.0, 0.4],
    [0.8, 0.1, 0.0, 0.1],
    [0.7, 0.1, 0.0, 0.2],
    [0.3, 0.3, 0.0, 0.4],
    [0.4, 0.0, 0.0, 0.6],
]

# calc total entropy
entropy = total_entropy(profile)
print(entropy)
