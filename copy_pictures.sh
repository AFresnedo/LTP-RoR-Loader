#!/usr/bin/env bash

# remove old pictures
echo Removing $ma/public/FIGS
rm -r $ma/public/FIGS/*

# copy pictures from source
echo Copying $curriculum figures into $ma/public/FIGS
find $pic_files/**/**/FIGS/* -type f -exec cp -r {} $ma/public/FIGS/ \;
