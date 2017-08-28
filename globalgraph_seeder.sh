#!/usr/bin/env bash

# NOTE use seeder.sh to call this shell file

python ~/Documents/persProj/ma_loader/globalgraph_input.py globalgraph.txt $curriculum

rm ../../math_affirm/db/seeds/globalgraph_seed.rb
mv ./globalgraph.txt_seed ../../math_affirm/db/seeds/globalgraph_seed.rb
