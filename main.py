from split import onePage
import sys, os
from os import listdir 
from os.path import isfile, join
if __name__ == "__main__":
    dirname = sys.argv[1]
    prd_ser = sys.argv[2]
    files = [dirname+f for f in listdir(dirname) if isfile(join(dirname, f))]
    if os.path.isdir('result') == False:
        os.mkdir('result')
    for f in files:
        onePage(f, prd_ser)
    print('total pages', len(files))
        