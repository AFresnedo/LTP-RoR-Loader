#!/usr/bin/env bash

# NOTE use seeder.sh to call this shell file

python $loader/process_globalgraph.py $files/globalgraph.txt $curriculum

rm $seeds/globalgraph_seed.rb
find $files -name 'globalgraph.txt_seed' -exec cat {} >> $seeds/globalgraph_seed.rb \;
find $files -name 'globalgraph.txt_seed' -exec cat {} >> $seeds/all.rb \;
