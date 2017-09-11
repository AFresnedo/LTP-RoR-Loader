#!/usr/bin/env bash

# step 1: create the seed files

# first part creates (and outputs through pipe) a list of all the files in
# curriculum's directory, subdirectories, and those subdirectories' directories

# second part has perl print a list of all the files that don't have "theory"
# in them and that gets piped as output into python's stdin

# third part: see python scripts for math-affirm-loader
ls $files/**/**/*.html | perl -nle 'print if /(?<!theory)[0-9]+.html/' | python $loader/process_problem.py $pythonFillerPathLength

# step 2: grab all the _seed files and concatenate them into a large seed file
rm $seeds/problem_seed.rb
find $files -name '*.html_seed' -exec cat {} >> $seeds/problem_seed.rb \;
# also add to gigantic seed file
find $files -name '*.html_seed' -exec cat {} >> $seeds/all.rb \;
