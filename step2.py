from Bio import SeqIO

for record in SeqIO.parse("sequence.fasta", "fasta"):
    print("sequence ID:", record.id)
    print("sequence length:", len(record.seq))
    print("sequence:", record.seq)


