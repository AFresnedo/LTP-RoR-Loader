import processing_funcs
import sys, os
bash_input = sys.argv[1]

# TODO fix syntax if needed, what is pluralized? Comment or Comments? does it
# depend on the relation type?
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
    # move through the file
    for line in i:
        # stop moving when beginning of problem text found
        if line.strip() == ':bprb:':
            break
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
        o.write(line.strip()+' ')
    # finish writing text attribute for Problem
    o.write('")'+ "\n")

    # TODO Problem.Answer tuple

    # move through file until first solution begins
    for line in i:
        if ':bsol:' in line:
            break
    # process solution/hint chunks until metadata section is reached
    # TODO update to curriculum instead of outdated category
    while ':bcat:' not in line.strip():
        processing_funcs.processChunk(i, o)
