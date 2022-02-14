./har-tools -x /tmp/manga $1
f=0
imgfolder="/tmp/manga/dre-a*"
for file in $(ls $imgfolder/filesv/sc/contents/)
do
  f=$file
  echo $f
done

rm $imgfolder/filesv/sc/contents/$f/6s/0/*_*
echo "$imgfolder/filesv/sc/contents/$f/6s/0/ $f"
python3 ./main.py $imgfolder/filesv/sc/contents/$f/6s/0/ $f
zip -qj  1.zip ./result/*
rm -rf ./result
rm -rf /tmp/manga
