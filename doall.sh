#!/bin/bash
# set -xv
shopt -s extglob

if [ -z "$1" ]
  then
    yamldir="yaml"
  else
    yamldir="$1"
fi
echo "processing all files from yaml directory $yamldir"

FILES="./$yamldir/*.yml"

for f in $FILES;
do
  b=$(basename -s .yml $f )
  ./doit.sh "$b" "$yamldir"
done
