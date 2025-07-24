text = "GCTAGCT"

# find reverse complement of a nucleotid pattern
def reverse_complement(pattern):
    pattern2 = pattern.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    pattern2 = pattern2[::-1]
    pattern3 = pattern2.upper()
    return pattern3

print(reverse_complement(text))


