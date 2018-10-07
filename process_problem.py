import json
import answer_module
import sol_hint
import re
import sys

# NOTE script template format, in order of appearance
# :bt: denotes problem title
# :bprb: denotes problem statement, all html expected including <p>
# multiple answer modules possible, following two comments
# :bans: denotes answer; non-defaults typed by :type=mc:, :type=cb:
# :bansinf: denotes answer
# multiple solution/hint combos possible
# :btype: denotes solution type
# :bsol: denotes solution statement
# :bhint: denotes hint, script needs to exclude <li> </li>
# :bdiff: denotes difficulty integer, 1-7
# :bsource: denotes source, a string

# p = Problem.create!(filename: , text: )
# p.answer(values: , module: )
# s = p.solutions.create!(typ: , text: )
# s.hints.create!(text: )
# p.metadata(curriculum: , category: , context: , diff: , src: )

fillerPathLength = int(sys.argv[1])
# filename is problem.html file
for filename in sys.stdin:
    filename = filename.strip()
    print "Processing problem file: "+filename
    # get directory path and filename
    match = re.search('(.*)\/(.*\.html)', filename)
    # save directory path for referencing problems
    dirPath = match.group(1)
    dirPieces = dirPath.split('/')
    # get curriculum
    curriculum = str.lower(dirPieces[fillerPathLength])
    # get category
    category = str.lower(dirPieces[fillerPathLength+1])
    # get context
    context = str.lower(dirPieces[fillerPathLength+2])
    # get in-directory filename
    localName = match.group(2)
    # create new, or overrite, file to write seed code into
    o = open(filename + '_seed', 'w')
    # open source file
    i = open(filename)
    with i, o:
        # write Problem tuple
        # add comment seperation for seed file organization
        o.write('#PROBLEM TUPLE FOR '+filename+"\n")
        # write beginning of create command for the tuple going to Problem
        o.write('p = Problem.create!(filename: "'+localName
                +'", curriculum: "'+curriculum
                +'", category: "'+category
                +'", context: "'+context
                +'", title: "')
        # move through the file, searching for start of title
        for line in i:
            # stop moving when beginning of problem title found
            if ':bt:' in line:
                break
        assert ':bt:' in line
        # write title
        for line in i:
            if ':et:' in line:
                break
            o.write(line.strip())
        assert ':et:'
        # move through the input, searching for start of Problem statement
        for line in i:
            # stop moving when beginning of problem text found
            if ':bprb:' in line:
                break
        assert ':bprb:' in line
        o.write('", text: ')
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

        # process all following answer modules
        # while not :bsol: send a chunk to processAnswers

        # process answer module(s) and end when :btype: is found
        answer_module.processAnswers(i, o)

        # get type and continue
        typ = None
        for line in i:
            if ':etype' in line:
                break
            # get the type
            typ = line.strip()
        assert 'etype:' in line

        # Solution(s) tuple(s) and Hint(s) tuple(s)
        # TODO update to curriculum instead of outdated category
        # go to first solution
        for line in i:
            if ':bsol:' in line:
                break
        assert ':bsol:' in line
        # process solution(s) and their hints
        sol_hint.processChunk(i, o, typ)

        # Metadata tuple, TODO update for curriculum->category->...
        # note that category is already found because of processCHunk
        # write beginning of metadata tuple for problem p
        o.write('#METADATA TUPLE FOR PROBLEM P\n')
        o.write('p.metadata = Metadata.new(diff: "')
        # sol_hint ends at start of diff block
        for line in i:
            # break loop if end of difficulty block
            if ':ediff:' in line:
                break
            # write difficulty block
            o.write(line.strip())
        # next attribute
        o.write('", source: "')
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
