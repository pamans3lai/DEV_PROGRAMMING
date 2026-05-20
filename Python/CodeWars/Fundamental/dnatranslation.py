# https://www.codewars.com/kata/554e4a2f232cdd87d9000038/train/python
# tanggal: 20 Mei 2026


def DNA_strand(dna):
    trans = str.maketrans("ATTGC", "TAACG")
    output = dna.translate(trans)
    return output

# def DNA_strand(dna):
   # mapping = {"A": "T", "T": "A", "G": "C", "C": "G"}
   # output = "".join(mapping[base] for base in dna)
   # return output
