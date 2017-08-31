#!/usr/bin/env bash

curriculum=LIFETOMATH
files=~/Documents/persProj/ma_files/LIFETOMATH
ma=~/Documents/persProj/math_affirm
backups=~/Documents/persProj/ma_files/backup_FIGS
# TODO properly process figs so that you don't need 3 copies of everything

# remove old pictures
rm -r $ma/public/answers/FIGS/*
rm -r $ma/public/problems/FIGS/*
rm -r $ma/public/theories/FIGS/*

# copy pictures from source
find $files/**/**/FIGS/* -type f -exec cp -r {} $ma/public/answers/FIGS/ \;
find $files/**/**/FIGS/* -type f -exec cp -r {} $ma/public/problems/FIGS/ \;
find $files/**/**/FIGS/* -type f -exec cp -r {} $ma/public/theories/FIGS/ \;
