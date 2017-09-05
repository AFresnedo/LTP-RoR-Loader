#!/usr/bin/env bash

# remove old pictures
rm -r $ma/public/FIGS/*

# copy pictures from source
find $pic_files/**/**/FIGS/* -type f -exec cp -r {} $ma/public/FIGS/ \;
