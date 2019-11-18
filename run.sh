./har-tools -x /tmp/manga $1
f=0
imgfolder="/tmp/manga/dre-a*"
#if [ -d "/tmp/manga/dre-aka-f.papy.co.jp" ]; then
#  imgfolder="/tmp/manga/dre-aka-f.papy.co.jp"
#elif [ -d "/tmp/manga/dre-aws-p.papy.co.jp" ]; then
#  imgfolder="/tmp/manga/dre-aws-p.papy.co.jp"
#else
#  imgfolder="/tmp/manga/dre-aws-f.papy.co.jp"
#fi
for file in $(ls $imgfolder/filesv/sc/contents/)
do
  f=$file
done

rm $imgfolder/filesv/sc/contents/$f/6s/0/*_*
python3 ./main.py $imgfolder/filesv/sc/contents/$f/6s/0/ $f
zip -qj  1.zip ./result/*
rm -rf ./result
rm -rf /tmp/manga
