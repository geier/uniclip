# uniclip
:clipboard: copy unicode characters to your clipboard


# install

install xclip and [choose](https://github.com/geier/choose)
download and unpack: ftp://ftp.unicode.org/Public/9.0.0/ucdxml/ucd.all.flat.zip
run
```
python generate_unicode_file.py > unicode_complete.txt
mkdir -p ~/.local/share/uniclip/
mv unicode_complete.txt ~/.local/share/uniclip/
```
copy uniclip to a folder in your path and you are good to go


