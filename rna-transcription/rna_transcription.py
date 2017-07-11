def to_rna(from_dna):
    dna = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    for letter in from_dna:
        if letter not in dna:
            return ''
    return ''.join(dna[rna] for rna in from_dna)
