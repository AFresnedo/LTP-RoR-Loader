#!/usr/bin/env bash

# NOTE: call from the curriculum folder you want to process, will overrite
# previous theory seed file

# step 1: create the seed files

# first part creates (and outputs through pipe) a list of all the files in
# curriculum's directory, subdirectories, and those subdirectories' directories

# second part has perl print a list of all the files that have "theory"
# in them and that gets piped as output into python's stdin

# third part: see python scripts for math-affirm-loader
ls ./**/**/*.html | perl -nle 'print if /(?<!theory)[0-9]+.html/' | python ~/Documents/persProj/ma_loader/problem_input.py

# step 2: grab all the _seed files and concatenate them into a large seed file
rm ../../math_affirm/db/seeds/curriculum_seed.rb
find . -name '*.html_seed' -exec cat {} >> ../../math_affirm/db/seeds/curriculum_seed.rb \;
