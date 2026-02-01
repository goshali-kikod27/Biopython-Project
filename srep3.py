from Bio.Blast import NCBIXML

with open("blast_result.xml") as handle:
    blast_record = NCBIXML.read(handle)

print("Query length:", blast_record.query_length)

for alignment in blast_record.alignments[:5]:  # top 5 hits
    for hsp in alignment.hsps:
        print("Title:", alignment.title)
        print("Length:", alignment.length)
        print("E-value:", hsp.expect)
        print("Identities:", hsp.identities)
        print("-" * 40)
        