# can handle scoring by setting default at cirriculm graph script and
# overriding locally
import sys, os

file_input = sys.argv[1]
# TODO before calling this script for all sections, call cirriculm graph script
section = sys.argv[2]
# scoring input are int pairs of main,makeup with highest value pair being no
# hints and lowest value pair being all hints (7, 3), (5, 2), (3, 1) default
scoring_input = sys.argv[3]
o = open('seed_' + file_input, 'w+')
# create graph tuple
o.write('Graph.create!(context: "'+section+'", scoring: "'+scoring_input+'", ')
# create tuple for problem statement
i = open(file_input)
with i:
    o.write('progression: "(')
    for line in i:
        if line.strip() == '':
            o.write(') (')
        o.write(line.strip() + ' ')
    o.write(')"')
o.write(')')
o.close
