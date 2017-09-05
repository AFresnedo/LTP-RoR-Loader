#!/usr/bin/env bash

pic_files=$fillerPath/ma_files/LIFETOMATH
ma=$fillerPath/math_affirm

# remove old pictures
rm -r $ma/public/FIGS/*

# copy pictures from source
find $pic_files/**/**/FIGS/* -type f -exec cp -r {} $ma/public/FIGS/ \;
