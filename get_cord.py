import sys


max_loop = 20
x = 7
y = 7

width = 120
height = 171
def f_shuffle_r(ar_number,snum,x_idx,y):
    gn = kn = int(y/2)
    if y%2 != 0:
        gn += 1
    ar_g = [None]*gn
    ar_k = [None]*kn
    g_cnt=k_cnt=0

    ar_tmp = [None]*y
    cnt = 0
    if snum%2 == 0:
        for i in range(y):
            if i%2 == 0:
                ar_g[g_cnt] = ar_number[i][x_idx]
                g_cnt+=1
            else:
                ar_k[k_cnt] = ar_number[i][x_idx]
                k_cnt+=1

        for i in range(gn):
            if i < len(ar_k) and ar_k[i] != None:
                ar_tmp[cnt] = ar_k[i]
                cnt+=1
            if ar_g[i] != None:
                ar_tmp[cnt] = ar_g[i]
                cnt+=1
    else:
        for i in range(y):
            if i < gn:
                ar_g[g_cnt] = ar_number[i][x_idx]
                g_cnt+=1
            else:
                ar_k[k_cnt] = ar_number[i][x_idx]
                k_cnt+=1

        for i in range(gn):
            if ar_g[i] != None:
                ar_tmp[cnt] = ar_g[i]
                cnt+=1
            if i < len(ar_k) and ar_k[i] != None:
                ar_tmp[cnt] = ar_k[i]
                cnt+=1

    for i in range(y):
        ar_number[i][x_idx] = ar_tmp[i]
    return ar_number


def getCord(tmp_page, prd_ser, o_height, o_width):
    diff_w = o_width%x
    diff_h = o_height%y
    cnt = 0
    ar_number = [[None for i in range(y)] for j in range(x)]
    for i in range(y):
        for j in range(x):
            ar_number[i][j] = cnt
            cnt+=1
    for i in range(y):
        ar_tmp = [None]*x
        st = x - i%x
        for j in range(x):
            if st >= x:
                st = 0
            ar_tmp[j] = ar_number[i][st]
            st += 1
        for j in range(x):
            ar_number[i][j] = ar_tmp[j]

    for i in range(x):
        ar_tmp = [None]*y
        st = y - i%y
        for j in range(y):
            if st >= y:
                st = 0
            ar_tmp[j] = ar_number[st][i]
            st += 1
        for j in range(y):
            ar_number[j][i] = ar_tmp[j]
    for i in range(x):
        num = i + 1
        seed = int(tmp_page)+int(prd_ser)
        if seed % max_loop == 0:
            seed = abs(int(tmp_page)-int(prd_ser))+(max_loop+1)

        k = int((num*seed+int(tmp_page)/max_loop) % max_loop)
        for j in range(k-1, -1, -1):
            ar_number = f_shuffle_r(ar_number,j,i,y)

    total = x*y
    ar_didx = [None]*total
    for i in range(y):
        for j in range(x):
            d_stx = diff_w+(j*width)
            d_sty = diff_h+(i*height)
            number = ar_number[i][j]
            ar_didx[number] = [None]*2
            ar_didx[number][0] = d_stx
            ar_didx[number][1] = d_sty
    return ar_didx