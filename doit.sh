#!/bin/bash
# set -xv
shopt -s extglob

if [ -z "$2" ]
  then
    yamldir="yaml"
  else
    yamldir="$2"
fi
echo "processing $1 from yaml directory $yamldir"

prepend="common.yml"
outdir="out"

base="$1"
infile="$1.yml"
#wireviz $infile
gvfile="$1.gv"

cp "./$yamldir/$infile" .

# run the main program
wireviz --prepend-file "$prepend" "$infile"

# see this topic about spreading out the spacing
# https://github.com/formatc1702/WireViz/issues/174
# edit this line to change ranksep
#   graph [bgcolor=white fontname=arial nodesep=0.33 rankdir=LR ranksep=2]
# sed --in-place='' "s/ranksep=2/ranksep=6/" "$gvfile"
sed -i '' "s/ranksep=2/ranksep=6/" "$gvfile"


# Now regenerate the output files
# except, making the new html file isn't so easy
dot -Tpng -O "$gvfile" 
dot -Tsvg -O "$gvfile" 
dot -Tpdf -O "$gvfile" 

# these are all the output files
bomfile="$1.bom.tsv"
pngfile="$1.png"
svgfile="$1.svg"

pngfile2="$1.gv.png"
svgfile2="$1.gv.svg"
pdffile2="$1.gv.pdf"

htmlfile="$1.html"

# move them to the output dir
mv "$gvfile"    ./"$outdir"
mv "$bomfile"   ./"$outdir"
mv "$pngfile"   ./"$outdir"
mv "$pngfile2"  ./"$outdir"
mv "$svgfile"   ./"$outdir"
mv "$svgfile2"  ./"$outdir"
mv "$pdffile2"  ./"$outdir"
mv "$htmlfile"  ./"$outdir"

# delete temporary copy of yaml input file
rm "$infile"

