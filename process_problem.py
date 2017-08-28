import json
import processing_funcs
import re
import sys

# TODO fix syntax if needed, what is pluralized? Comment or Comments? does it
# depend on the association type?
# p = Problem.create!(filename: , text: )
# p.answer(values: , module: )
# s = p.solutions.create!(typ: , text: )
# s.hints.create!(text: )
# p.metadata(curriculum: , category: , context: , diff: , src: )

# filename is problem.html file
for filename in sys.stdin:
    filename = filename.strip()
    print "Processing file: "+filename
    # get directory path and filename
    match = re.search('(.*)\/(.*\.html)', filename)
    # save directory path for referencing problems
    dirPath = match.group(1)
    dirPieces = dirPath.split('/')
    # get category
    category = str.lower(dirPieces[1])
    # get context
    context = str.lower(dirPieces[2])
    # get in-directory filename
    localName = match.group(2)
    # create new, or overrite, file to write seed code into
    o = open(filename + '_seed', 'w')
    # open source file
    i = open(filename)
    with i, o:
        # Problem tuple
        # move through the file, searching for start of Problem statement
        for line in i:
            # stop moving when beginning of problem text found
            if ':bprb:' in line:
                break
        assert ':bprb:' in line
        # write Problem tuple
        # add comment seperation for seed file organization
        o.write('#PROBLEM TUPLE FOR '+filename+"\n")
        # write beginning of create command for the tuple going to Problem
        o.write('p = Problem.create!(filename: \''+localName
                +'\', category: \''+category
                +'\', context: \''+context
                +'\', text: ')
        # fill in text attribute
        text = ''
        for line in i:
            # break when end of problem statement reached
            if ':eprb:' in line:
                # write string with escaped quotes, etc
                o.write(json.dumps(text))
                break
            # the following is a placeholder for dealing with figures, if needed
                #  if '<img src' in line:
                #    do something
            # append line to string
            text += line
        assert ':eprb:' in line
        # finish writing text attribute for Problem
        o.write(')\n')

        # TODO multiple modules, not yet implemented in MAM
        # Answer tuple
        for line in i:
            if ':bans:' in line:
                break
        # write beginning of create command for p.Answer tuple
        o.write('#ANSWER TUPLE FOR PROBLEM P' + "\n")
        # get problem tuple from database (doesn't seem to work otherwise)
        o.write('p.answer = Answer.new(values: "')
        # write answer value(s)
        for line in i:
            # end of problem statement reached
            if ':eans:' in line:
                break
            # skip extra <p> and </p> tags
            if 'p>' in line:
                None
            # write values as a string
            else:
                o.write(line.strip())
        # end writing answer value(s)
        assert ':eans:' in line
        o.write('", interface: "')
        # find interface text
        for line in i:
            if ':bansinf:' in line:
                break
        assert ':bansinf:' in line
        # write interface
        for line in i:
            if ':eansinf:' in line:
                break
            if 'p>' not in line:
                o.write(line.strip() + ' ')
        o.write('")\n')

        # Solution(s) tuple(s) and Hint(s) tuple(s)
        # TODO update to curriculum instead of outdated category
        typ = None
        # go to first solution
        for line in i:
            if ':bsol:' in line:
                try:
                    typ = re.search(r'type=(.*):', line).group(1)
                except AttributeError:
                    typ = 'unknown'
                break
        assert ':bsol:' in line
        # process solution(s) and their hints
        processing_funcs.processChunk(i, o, typ)

        # Metadata tuple, TODO update for curriculum->category->...
        # note that category is already found because of processCHunk
        # write beginning of metadata tuple for problem p
        o.write('#METADATA TUPLE FOR PROBLEM P\n')
        o.write('p.metadata = Metadata.new(category: "')
        # write category
        for line in i:
            # end of category reached
            if ':ecat:' in line:
                break
            # write until end of category
            o.write(line.strip())
        # next attribute
        o.write('", context: "')
        # goto context block
        for line in i:
            # found context
            if ':bcontext:' in line:
                break
        # for all context
        for line in i:
            # end of context block
            if ':econtext:' in line:
                break
            # write context block
            o.write(line.strip())
        # next attribute
        o.write('", diff: ')
        # goto difficulty block
        for line in i:
            # found difficulty
            if ':bdif:' in line:
                break
        # for all difficulty
        for line in i:
            # end of difficulty block
            if ':edif:' in line:
                break
            # write difficulty block
            o.write(line.strip())
        # next attribute
        o.write(', source: "')
        # goto source block
        for line in i:
            # found source
            if ':bsource:' in line:
                break
        # for all source
        for line in i:
            # end of source block
            if ':esource:' in line:
                break
            # write source block
            o.write(line.strip())
        # finish metadata tuple
        o.write('")\n')
