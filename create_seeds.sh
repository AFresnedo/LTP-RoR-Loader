#!/usr/bin/env bash

# step 1: create the seed files

# first part creates (outputs through pipe) a list of all the files in
# LIFETOMATH directorys, subdirectories, and those subdirectories' directories

# second part has perl print a list of all the files that don't have "theory"
# in them and that gets piped as output into python's stdin

# third part: see python scripts for math-affirm-loader
ls ../ma_files/LIFETOMATH/**/**/*.html | perl -nle 'print if /(?<!theory)[0-9]+.html/' | python ~/Documents/persProj/ma_loader/problem_input.py

# step 2: grab all the _seed files and concatenate them into a large seed file
rm ../ma_files/LIFETOMATH/curriculum_seed.rb
find ../ma_files/LIFETOMATH -name '*.html_seed' -exec cat {} >> ../ma_files/LIFETOMATH/curriculum_seed.rb \;
