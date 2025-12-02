def distance(strand_a, strand_b):
    if not len(strand_a) == len(strand_b):
        raise ValueError("Strands must be of equal length.")

    distance = 0
    for index, nucleotide in enumerate(strand_a):
        if not nucleotide == strand_b[index]:
            distance += 1
    return distance
