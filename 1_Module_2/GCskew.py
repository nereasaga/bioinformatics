# with open("./Genomes_data/Salmonella_enterica.txt", "r") as file:
#     text = file.read().strip()

text = "CATTCCAGTACTTCGATGATGGCGTGAAGA"

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

result = skew(text)
print(print(' '.join(str(x) for x in result)))

# find min and max positions of skew in genome
def min_skew_position(text):
    skew_values = skew(text)
    min_value = min(skew_values)
    positions = [i for i, value in enumerate(skew_values) if value == min_value]
    return positions

min_positions = min_skew_position(text)
print(" ".join(str(x) for x in min_positions))

def max_skew_position(text):
    skew_values = skew(text)
    max_value = max(skew_values)
    positions = [i for i, value in enumerate(skew_values) if value == max_value]
    return positions

max_positions = max_skew_position(text)
# print(" ".join(str(x) for x in max_positions))