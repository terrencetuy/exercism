AMINO_ACIDS = {
    "Methionine": "AUG",
    "Phenylalanine": ["UUU", "UUC"],
    "Leucine": ["UUA", "UUG"],
    "Serine": ["UCU", "UCC", "UCA", "UCG"],
    "Tyrosine": ["UAU", "UAC"],
    "Cysteine": ["UGU", "UGC"],
    "Tryptophan": ["UGG"]
}


STOP = ["UAA", "UAG", "UGA"]


def proteins(strand):
    codon = strand[0:3]
    if len(codon) < 3 or codon in STOP:
        return []
    return [get_amino_acid(codon)] + proteins(strand[3:])


def get_amino_acid(codon):
    for amino_acid, codons in AMINO_ACIDS.items():
        if codon in codons:
            return amino_acid
    raise ValueError