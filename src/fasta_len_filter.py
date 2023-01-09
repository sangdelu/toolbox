import argparse
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="filter reads")
    parser.add_argument("fasta")
    parser.add_argument("length")
    args = parser.parse_args()
    
    res = args.fasta + ".filtered_" + str(args.length)
    records = [r for r in SeqIO.parse(args.fasta, "fasta") if len(r.seq) >= int(args.length)]
    with open(res,"w") as out_handle:
      SeqIO.write(records,out_handle,"fasta")
      

