#!/usr/bin/env bash

# NOTE: call from the curriculum folder you want to process, will overrite
# previous graph seed file

ls ./**/**/*.txt | python ~/Documents/persProj/ma_loader/graph_in.py

rm ../../math_affirm/db/seeds/graph_seed.rb
find . -name '*.txt_seed' -exec cat {} >> ../../math_affirm/db/seeds/graph_seed.rb \;
