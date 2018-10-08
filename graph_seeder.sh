#!/usr/bin/env bash

# NOTE: call from the curriculum folder you want to process, will overrite
# previous graph seed file

ls $files/**/**/*.txt | python $loader/process_graph.py $pythonFillerPathLength

rm $seeds/graph_seed.rb
find $files -name '*.txt_local_graph_seed' -exec cat {} >> $seeds/graph_seed.rb \;
find $files -name '*.txt_local_graph_seed' -exec cat {} >> $seeds/all.rb \;
