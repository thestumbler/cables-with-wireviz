#!/bin/bash
# This is from
# https://stackoverflow.com/questions/1787356/use-imagemagick-to-place-an-image-inside-a-larger-canvas

newextent=620x186

#newextent=2560x1440
#back="#DEDEF6"
#back="#1f1f1f"
back="white"
#back="#eacda1"
#back="#f3bf10"
#convert -resize $newsize -background $back -gravity center \
convert -background $back -gravity center \
  "$1" -extent $newextent \
  "$2"

