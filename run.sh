/Users/violet/workspace/py-workspace/renta/har-tools -x /tmp/manga $1
f=0
for file in $(ls /tmp/manga/dre-aka-p.papy.co.jp/filesv/sc/contents/)
do
  f=$file
done

rm /tmp/manga/dre-aka-p.papy.co.jp/filesv/sc/contents/$f/6s/0/*_*
python3 /Users/violet/workspace/py-workspace/pyimg_base64/main.py /tmp/manga/dre-aka-p.papy.co.jp/filesv/sc/contents/$f/6s/0/ $f
zip -qj  1.zip /Users/violet/workspace/py-workspace/pyimg_base64/result/*
rm -rf /Users/violet/workspace/py-workspace/pyimg_base64/result/
rm -rf /tmp/manga
