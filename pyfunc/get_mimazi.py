'''

by xlc time:2018-06-27 10:54:43
'''
import sys
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])
import pandas as pd
import numpy as np
from pandas import DataFrame

def load_mimazi(path=main_path+'/knowledge/anji_mimazi.txt'):
    rslt_dct = {}
    f = open(path, 'r', encoding='utf-8').readlines()
    data = [i.strip().split('\t') for i in f]
    for i in data:
        rslt_dct[i[1]] = i[0]
    return rslt_dct

def load_name():
    knowledge = pd.read_excel('../knowledge/氨基酸介绍及密码子.xlsx', sheetname=1)
    df = knowledge[['中文名称', '符号与缩写']]
    chi_sx = {}
    sx_chi = {}
    df_lst = np.array(df).tolist()
    for i in df_lst:
        chi_name = i[0].replace('\xa0', '')
        suoxie = i[1].replace('\xa0', ' ').strip()
        suoxie = suoxie.split(' 或 ')[0]
        chi_sx[chi_name] = suoxie
        sx_chi[suoxie] = chi_name
    return chi_sx, sx_chi
    
if __name__ == '__main__':
    knowledge = pd.read_excel('../knowledge/氨基酸介绍及密码子.xlsx', sheetname=0)
    kg_lst = np.array(knowledge).tolist() #转化为列表
    head_dct = [] # 获取第二个碱基
    for i in range(1, len(kg_lst[0])-1):
        head_dct.append(kg_lst[0][i])
    # 创建新的`数据表`
    columns_lst = ['one'] + head_dct + ['last']
    new_kg_df = DataFrame(kg_lst[1:], columns=columns_lst)
    anji_mima = [] # 氨基酸+密码子
    for i in range(new_kg_df.shape[0]):
        one_data = new_kg_df.iloc[i]
        first = one_data['one']
        last = one_data['last']
        anji = one_data[1:-1] # 氨基酸名称
        for j in range(len(anji)):
            s_mima = head_dct[j]
            mimazi = first + s_mima + last
            sub_rslt = anji[j] + '\t' + mimazi
            anji_mima.append(sub_rslt)
    f = open('../knowledge/anji_mimazi.txt', 'w', encoding='utf-8')
    for i in anji_mima:
        f.write(i + '\n')
    f.close()
