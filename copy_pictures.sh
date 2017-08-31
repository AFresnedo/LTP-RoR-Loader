#!/usr/bin/env bash

files=~/Documents/persProj/ma_files/LIFETOMATH
ma=~/Documents/persProj/math_affirm
# TODO properly process figs so that you don't need 3 copies of everything

# NOTE problems, theories, view, solve

# remove old pictures
rm -r $ma/public/FIGS/*

# copy pictures from source
find $files/**/**/FIGS/* -type f -exec cp -r {} $ma/public/FIGS/ \;
