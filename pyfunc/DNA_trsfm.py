'''

by xlc time:2018-06-27 14:00:10
'''
import sys
#sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
import json
from get_configure import get_configure
config = get_configure()
from get_mimazi import load_mimazi
from get_mimazi import load_name

def DNA2RNA(gene_str, D_A='DNA'):
    gene_str = gene_str.upper()
    DNA_dct = json.loads(config.get('DNA', 'relation'))
    RNA_dct = json.loads(config.get('RNA', 'relation'))
    gene_lst = [i for i in gene_str]
    if D_A == 'DNA':
        new_gene = [DNA_dct[i] for i in gene_lst]
    else:
        new_gene = [RNA_dct[i] for i in gene_lst]
    return ''.join(new_gene)

def split_seq(gene_str):
    new_lst = []
    count = 0
    while 1:
        try:
            sss = gene_str[count]
            sub_str = gene_str[count: count+3]
            new_lst.append(sub_str)
            count += 3
        except IndexError:
            break
    return new_lst

def RNA2protein(gene_str):
    protein = load_mimazi()
    return protein[DNA2RNA(gene_str, 'RNA')]

def DNA2protein(gene_sq, to_sx=False):
    # to_sx 转化为缩写字母
    DNA_string = gene_sq.upper()
    gene_sq = split_seq(DNA_string)
    gene_lst = [DNA2RNA(i, 'RNA') for i in gene_sq]
    protein_lst = [RNA2protein(i) for i in gene_lst]
    if to_sx == False:
        return protein_lst
    else:
        chi_sx = load_name()[0]
        protein_lst = [chi_sx[i] for i in protein_lst]
        return protein_lst
    
if __name__ == '__main__':
    DNA_string = 'agtctg'
    gene_sq = split_seq(DNA_string)
    gene_lst = [DNA2RNA(i, 'RNA') for i in gene_sq]
    protein_lst = [RNA2protein(i) for i in gene_lst]
    
