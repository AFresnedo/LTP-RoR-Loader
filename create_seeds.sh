#!/usr/bin/env bash

# first part creates (outputs through pipe) a list of all the files in
# LIFETOMATH directorys, subdirectories, and those subdirectories' directories

# second part has perl print a list of all the files that don't have "theory"
# in them and that gets piped as output into python's stdin

# third part: see python scripts for math-affirm-loader
ls ../ma_files/LIFETOMATH/**/**/*.html | perl -nle 'print if /(?<!theory)[0-9]+.html/' | python ~/Documents/persProj/ma_loader/problem_input.py
