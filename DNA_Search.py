from enum import IntEnum
from typing import Tuple, List

# Representing a nucleotide as a simple IntEnum with four cases.
Nucleotide: IntEnum = IntEnum('Nuecleotide', ('A', 'C', 'G', 'T'))

# Codons are tuple of three Nucleotides.
# A gene is a list of Codons.

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes

# Our Imaginary Gene str
gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"

# Function to convert our str to a Gene


def string_to_Gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):  # dont run off end
            return gene
        # initialize codon out of three nucleotides
        codon: Codon = (Nucleotide[s[i]],
                        Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)  # add codon to gene
        return gene


# converting gene_str to Gene
my_gene: Gene = string_to_Gene(gene_str)


# Linear search - Finding a particular codon in our gene
def linear_search(gene: Gene, key_codon: Codon) -> bool:
    for codon in gene:
        if codon == key_codon:
            return True
    return False


# performing Linear search Two codons to see if they have our Original Codon
acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

# Note that even if the codons are same but of different arrangement, it wont equate to True.
print(linear_search(my_gene, acg))  # True
print(linear_search(my_gene, gat))  # False

print(acg in my_gene)
