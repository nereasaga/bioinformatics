from utils import frequency_table

text= "CGGAGGACTCTAGGTAACGCTTATCAGGTCCATAGGACATTCA"
k = 3



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

print(better_frequent_words(text, k))

# def frequent_words(text, k):
#     frequent_patterns = set()     
#     count = []                     

#     
#     for i in range(len(text) - k + 1):
#         pattern = text[i:i+k]
#         c = 0
#         for j in range(len(text) - k + 1):
#             if text[j:j+k] == pattern:
#                 c += 1
#         count.append(c)

#     
#     max_count = max(count)

#     
#     for i in range(len(text) - k + 1):
#         if count[i] == max_count:
#             pattern = text[i:i+k]
#             frequent_patterns.add(pattern)

#     return frequent_patterns
