import os
import gffutils
import pandas as pd
from tqdm import tqdm 
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import argparse

_CSV_HEADER = ['GeneID','Chrom','Start','End','Strand','Promoter']

def create(args):
    fn = args.gff # gffutils.example_filename(gff_path)
    db = gffutils.create_db(fn, dbfn='gff.db', force=True, keep_order=True,\
        disable_infer_genes=True, disable_infer_transcripts=True,\
        merge_strategy='merge', sort_attribute_values=True)
    return db

def genome_dict(genome_fasta_path):
    genome = dict()
    for record in SeqIO.parse(genome_fasta_path, 'fasta'):
        genome[record.id] = record.seq
    return genome

def get_utr5(db, gene):
    for i in db.children(gene, featuretype='mRNA', order_by='start'):
        print(i)

def get_utr3(db, gene):
    pass


def extract(args):
    promoter_length = args.length
    utr_head_length = args.utr_head
    genome_path = args.genome
    gff_db_path = args.gff
    output_file = args.output
    genome = genome_dict(genome_path)
    # db = create_db(gff_path)
    db = gffutils.FeatureDB(gff_db_path, keep_order=True)
    index = 0
    # promoter_seq = pd.DataFrame(columns=['GeneID','Chrom','Start','End','Strand','Promoter'])
    promoter_seq_list = []
    for f in tqdm(db.all_features(featuretype='gene', order_by="seqid"), \
                  total = len(list(db.all_features(featuretype='gene', order_by="seqid"))), \
                  ncols = 80, desc = "Promoter Processing:"):
        chrom = f.chrom
        geneid = f.id
        strand = f.strand
        if f.strand == "+":
            gene_seq = f.sequence(genome_path, use_strand=True)
            p_start = f.start - int(promoter_length) - 1
            if p_start < 0 :
                continue
            p_end = f.start + utr_head_length - 1
            promoter = genome[f.chrom][p_start:p_end]
            # print(promoter)
        elif f.strand == "-":
            gene_seq = f.sequence(genome_path, use_strand=True)
            p_start = f.end - utr_head_length
            p_end = f.end + int(promoter_length)
            promoter = genome[f.chrom][p_start:p_end].reverse_complement()
            # print(promoter)
        p_start_in_genome = p_start
        p_end_in_genome = p_end
        # promoter_seq.loc[index] = [geneid,chrom,p_start_in_genome,p_end_in_genome,strand,promoter]
        # index += 1
        it = [geneid,chrom,p_start_in_genome,p_end_in_genome,strand,promoter]
        promoter_seq_list.append(dict((_CSV_HEADER[i],it[i]) for i in range(len(_CSV_HEADER))))
    promoter_seq = pd.DataFrame.from_dict(promoter_seq_list)
    promoter_seq.to_csv(output_file, sep=',', index=False)

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='sub-command help')
# create subcommand 
parser_create = subparsers.add_parser('create', help='create annotation database')
parser_create.add_argument('-g', '--gff', type=str, help='genome annotation file')
parser_create.set_defaults(func=create)
# extract subcommand
parser_extract = subparsers.add_parser('extract', help='extract promoter in genome or gene')
parser_extract.add_argument('-l', '--length', type=int, help='promoter length before TSS')
parser_extract.add_argument('-g', '--gff', type=str, help='gff binary database created before')
parser_extract.add_argument('-u', '--utr_head', type=int, help='utr5 length after TSS')
parser_extract.add_argument('-f', '--genome', type=str, help='genome fasta')
parser_extract.add_argument('-o', '--output', type=str, help = 'output csv file path')
parser_extract.add_argument('-v', '--version', help = 'promoterExtract version', action = "store_true")
parser_extract.set_defaults(func=extract)
args = parser.parse_args()
args.func(args)



'''
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--length', type=int, help='promoter length before TSS')
    parser.add_argument('-u', '--utr_head', type=int, help='length after TSS')
    parser.add_argument('-f', '--genome', type=str, help='genome fasta')
    parser.add_argument('-g', '--gff', type=str, help='genome annotation file')
    parser.add_argument('-o', '--outdir', type=str, help='output directory')
    args = parser.parse_args()
    get_promoter(args.length, args.utr_head, args.genome, args.gff, args.outdir)
'''                                             
