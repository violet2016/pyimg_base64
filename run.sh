./har-tools -x /tmp/manga $1
f=0
for file in $(ls /tmp/manga/dre-aka-p.papy.co.jp/filesv/sc/contents/)
do
  f=$file
done

rm /tmp/manga/dre-aka-p.papy.co.jp/filesv/sc/contents/$f/6s/0/*_*
python3 ./main.py /tmp/manga/dre-aka-p.papy.co.jp/filesv/sc/contents/$f/6s/0/ $f
zip -qj  1.zip ./result/*
rm -rf ./result
rm -rf /tmp/manga
