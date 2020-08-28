from enum import IntEnum
from typing import Tuple, List

# Representing a nucleotide as a simple IntEnum with four cases.
Nucleotide: IntEnum = IntEnum('Nuecleotide', ('A', 'C', 'G', 'T'))

# Codons are tuple of three Nucleotides.
# A gene is a list of Codons.

Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]  # type alias for codons
Gene = List[Codon]  # type alias for genes
