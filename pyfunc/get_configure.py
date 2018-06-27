import configparser
import codecs
import os
main_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
main_path = '/'.join(main_path.split('/')[:-1])

def get_configure(path=main_path+'/config/config.txt'):
    config = configparser.ConfigParser()
    config.readfp(codecs.open(path, "r", "utf-8-sig"))
    return config

if __name__ == '__main__':
    config = get_configure()
