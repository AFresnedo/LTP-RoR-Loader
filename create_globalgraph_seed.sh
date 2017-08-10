#!/usr/bin/env bash

# NOTE: call from the curriculum folder you want to process, will overrite
# previous graph seed file

# TODO replace "lifetomath" with "this directory's folder name"
curriculum=${PWD##*/}
python ~/Documents/persProj/ma_loader/globalgraph_input.py globalgraph.txt $curriculum

rm ../../math_affirm/db/seeds/globalgraph_seed.rb
mv ./globalgraph.txt_seed ../../math_affirm/db/seeds/globalgraph_seed.rb
