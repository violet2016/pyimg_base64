import base64
import sys
if __name__ == "__main__":
    fname = sys.argv[1]
    with open(fname, "rb") as f:
        fstr = f.read()
        prefix = b'\xff\xd8\xff\xe0\x00'
        strs = fstr.split(prefix)
        for idx, i in enumerate(strs):
            if i != 0:
                encodedZip = base64.b64encode(prefix+i)
                b64str = encodedZip.decode()
                jpgdata = base64.b64decode(b64str)
                g = open(fname+str(idx)+'.jpg', "wb")
                g.write(jpgdata)
                g.close()