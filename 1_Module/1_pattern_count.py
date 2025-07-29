text = "TACGCATTACAAAGCACA"
pattern = "AA"

# find number of times a pattern appears in genome
def pattern_count(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count += 1
    return count

print(pattern_count(text, pattern))
