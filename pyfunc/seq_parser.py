'''

by xlc time:2018-06-27 18:07:30
'''
import sys
#sys.path.append('D:/svn_codes/source/public_fun')
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])


if __name__ == '__main__':
    f = open(main_path+'/datasets/gbbct111.seq', 'r', encoding='utf-8')
    
