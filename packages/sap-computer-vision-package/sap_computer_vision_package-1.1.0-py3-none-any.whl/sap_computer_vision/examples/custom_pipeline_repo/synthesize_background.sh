#!/bin/bash

TRANSPARENCY=$3     # 0..100
ROTATE=$4           # 0..360
dst_dir=$5

bg_name=${1##*/}
fg_name=${2##*/}
bg_name=${bg_name:0:-4}
fg_name=${fg_name:0:-4}
result_name=${fg_name}_${bg_name}_t${TRANSPARENCY}_r${ROTATE}

fg_dir=$(dirname $2)
CONVERT_CMD=$(echo convert $2  -fuzz $TRANSPARENCY%  -rotate $ROTATE -transparent white ${dst_dir}/${result_name}.png)
eval "$CONVERT_CMD"

bg_size=`identify -format '%wx%h' "$1"`
fg_size=`identify -format '%wx%h' "${dst_dir}/${result_name}.png"`

fg_resized=${dst_dir}/${fg_name}_resized_${bg_size}_$BASHPID.png
convert -resize $bg_size ${dst_dir}/${result_name}.png $fg_resized

convert  -composite $1 "${fg_resized}" -depth 8 -gravity center "${dst_dir}/${result_name}.jpg"
convert -resize  500X500 "${dst_dir}/${result_name}.jpg" "${dst_dir}/${result_name}.jpg"
rm $fg_resized
rm ${dst_dir}/${result_name}.png
