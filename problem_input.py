import processing_funcs
import re
import sys, os
bash_input = sys.argv[1]

# TODO fix syntax if needed, what is pluralized? Comment or Comments? does it
# depend on the association type?
# P = Problem.create!(filename: , text: )
# P.Answer(values: , module: )
# S = P.Solution.create!(typ: , text: )
# S.Hint.create!(text: )
# P.Metadata(curriculum: , category: , context: , diff: , src: )

# create new, or overrite, file to write seed code into
o = open('seed_' + bash_input, 'w')
# open source file
i = open(bash_input)
with i, o:
    # Problem tuple
    # move through the file, searching for start of Problem statement
    for line in i:
        # stop moving when beginning of problem text found
        if line.strip() == ':bprb:':
            break
    assert ':bprb:' in line
    # write Problem tuple
    # add comment seperation for seed file organization
    o.write('#PROBLEM TUPLE' + "\n")
    # write beginning of create command for the tuple going to Problem
    o.write('Problem.create!(filename: "'+bash_input+'",'+' text: "')
    # fill in text attribute
    for line in i:
        # break when end of problem statement reached
        if line.strip() == ':eprb:':
            break
        # the following is a placeholder for dealing with figures, if needed
            #  if '<img src' in line:
            #    do something
        # write text into text attribute
        # TODO escape quotes
        o.write(line.strip()+' ')
    assert ':eprb:' in line
    # finish writing text attribute for Problem
    o.write('")'+ "\n")

    # TODO multiple modules, not yet implemented in MAM
    # Answer tuple
    for line in i:
        if line.strip() == ':bans:':
            break
    # write beginning of create command for P.Answer tuple
    o.write('#ANSWER TUPLE FOR PROBLEM P' + "\n")
    o.write('P.Answer.create!(values: "')
    # write answer value(s)
    for line in i:
        # end of problem statement reached
        if line.strip() == ':eans:':
            break
        # skip extra <p> and </p> tags
        if 'p>' in line:
            None
        # write values as a string
        else:
            numList = str([x for x in line.strip().split('|')])
            o.write(numList[1:len(numList)-1])
    # end writing answer value(s)
    assert ':eans:' == line.strip()
    o.write('", interface: "')
    # find interface text, TODO determine if html should be removed or not
    for line in i:
        if line.strip() == ':bansinf:':
            break
    assert ':bansinf:' == line.strip()
    # write interface
    for line in i:
        if line.strip() == ':eansinf:':
            break
        o.write(line.strip()+' ')
    o.write('")'+ "\n")



    # Solution(s) tuple(s) and Hint(s) tuple(s)
    # TODO update to curriculum instead of outdated category
    typ = None
    # go to first solution
    for line in i:
        if ':bsol:' in line:
            typ = re.search(r'type=(.*):', line).group(1)
            break
    assert ':bsol:' in line
    # process solution(s) and their hints
    processing_funcs.processChunk(i, o, typ)
