import base64
import sys, os
from PIL import Image

def splitRecover(octetFile):
    fstr = octetFile.read()
    prefix = b'\xff\xd8\xff\xe0\x00'
    fend = fname.split('/')[-1]
    os.mkdir(fend)
    strs = fstr.split(prefix)
    cord = ''
    for idx, i in enumerate(strs):
        if idx == 0:
            cord = i
            continue
        encodedZip = base64.b64encode(prefix+i)
        b64str = encodedZip.decode()
        jpgdata = base64.b64decode(b64str)
        g = open(fend+'/'+str(idx)+'.jpg', "wb")
        g.write(jpgdata)
        g.close()
    cords = str(cord).split('|')
    print(len(cords))
    print(cords)
    di = {}
    for idx, cor in enumerate(cords):
        if idx < 2:
            continue
        di[int(cor.split(',')[1][0:4])] = idx-1
    sorted_cords = [(k,di[k]) for k in sorted(di.keys())]
    print(sorted_cords)
if __name__ == "__main__":
    fname = sys.argv[1]
    f = open(fname, "rb")
    splitRecover(f)

"""
tmp_page = page number
prd_ser = 419575
	var max_loop = 20;
	for(var i=0; i<x; i++){
		var num = i+1;
		var seed = parseInt(tmp_page)+parseInt(prd_ser);
		if( seed % max_loop == 0 ){
			seed = Math.abs(tmp_page-prd_ser)+(max_loop+1);
		}
		var k = parseInt(((num*seed)+(tmp_page/max_loop)) % max_loop);
		for( var j=k-1; j>=0; j-- ){
			ar_number = f_shuffle_r(ar_number,j,i,y);
		}
	}
	
	var total = x*y;
	var ar_didx = new Array(total);
	for( var i=0; i<y; i++ ){
		for( var j=0; j<x; j++ ){
			var d_stx = diff_w+(j*width);
			var d_sty = diff_h+(i*height);
			var number = ar_number[i][j];
			ar_didx[number] = new Array(2);
			ar_didx[number]["0"] = d_stx;
			ar_didx[number]["1"] = d_sty;
		}
	}

	// 上の処理内で描画してしまうと、データの取得順で並び順がばれてしまう。初期配置の順番で描画していく
	for(var i=0;i<total;i++){
		src = f_get_data(ar_idx[i],data);
		f_div_draw(i,parseInt(ar_didx[i][0])+parseInt(dst),ar_didx[i][1],width,height,ctx,src);
	}
"""