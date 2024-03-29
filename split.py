import base64
from logging import exception
import sys, os
import shutil
from PIL import Image
from get_cord import getCord
pHeight = 171

def splitRecover(octetFile):
    print("octed file: ", octetFile)
    f = open(octetFile, "rb")
    fstr = f.read()
    print(fstr[0:50])
    try:
        width = int(fstr[9:12])
        height = int(fstr[13:17])
    except Exception:
        width = int(fstr[9:13])
        height = int(fstr[14:18])
    print(width, height)
    prefix = b'\xff\xd8\xff\xe0\x00'
    fend = octetFile.split('/')[-1]

    try:
        os.mkdir(fend)
    except Exception as e:
        print(str(e))
        pass 
    strs = fstr.split(prefix)
    for idx, i in enumerate(strs):
        if idx == 0:
            continue
        encodedZip = base64.b64encode(prefix+i)
        b64str = encodedZip.decode()
        jpgdata = base64.b64decode(b64str)
        jpgfile = fend+'/'+str(idx)+'.jpg'
        #print(jpgfile)
        g = open(jpgfile, "wb")
        g.write(jpgdata)
        g.close()
    return width, height
def generateImage(dirname, height, width, didx):
    result = Image.new("RGB", (width, height))
    path = './'+dirname+'/'

    for i in range(3,52):
        try:
            img = Image.open(path+str(i)+'.jpg')
            result.paste(img, (didx[i-3][0], didx[i-3][1]))
        except Exception as e:
            print(str(e))
            pass
    img_1 = Image.open(path+'1.jpg')
    result.paste(img_1, (0, 0))
    img_2 = Image.open(path+'2.jpg')
    result.paste(img_2, (0, 0))
    result.save('./result/'+dirname+'.jpg')

def onePage(fname, prd_ser):
    if os.path.getsize(fname) == 0:
        print(fname, 'size is 0')
        return
    w, h = splitRecover(fname)
    if w < 0:
        return
    dirname = fname.split('/')[-1]
    didx = getCord(dirname, prd_ser, h, w)
    #print(dirname)
    generateImage(dirname, h, w, didx)
    shutil.rmtree('./'+dirname)

if __name__ == "__main__":
    fname = sys.argv[1]
    prd_ser = sys.argv[2]
    onePage(fname, prd_ser)
