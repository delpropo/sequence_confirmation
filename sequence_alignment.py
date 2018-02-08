from Bio import pairwise2
from Bio.SubsMat.MatrixInfo import blosum62
from Bio.pairwise2 import format_alignment
from import_sequences import test_data

test2 = "ATGAGAGAG"
test1 = test2 + "ATCGCGA" + test2

alignment = pairwise2.align.localds(test1, test2, blosum62, -10, -0.5)

for i in alignment:
    print(format_alignment(*i))


import_from_email(test_data)