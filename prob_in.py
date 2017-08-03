# This script takes a relative file path to a prob_num and creates 5 types
# of tuples: problem, answer(s), solution(s), hint(s), and metadata
import sys, os
import re
bash_input = sys.argv[1]
# if simultaneous reading/writing needed, use + s.a. 'w+'
o = open('seed_' + bash_input, 'w')
# create tuple for problem statement
i = open(bash_input)
with i,o:
    for line in i:
        if line.strip() == ':bprb:':
            break
    # write beginning of create command for the tuple going to Problem
    o.write('#PROBLEM TUPLE' + "\n")
    o.write('Problem.create!(filename: "'+bash_input+'",'+' text: "')
    for line in i:
        # end of problem statement reached
        if line.strip() == ':eprb:':
            break
        # TODO placeholder for dealing with figures, if needed
        #  if '<img src' in line:
            #  o.write('"')
            #  # do something
        o.write(line.strip()+' ')
    o.write('")'+ "\n")

# TODO check for multiple answer modules
# create tuple for answers
o = open('seed_' + bash_input, 'a')
i = open(bash_input)
with i,o:
    for line in i:
        if line.strip() == ':bans:':
            break
    # write beginning of create command for the tuple going to Answer
    o.write('#ANSWER TUPLE' + "\n")
    o.write('Answer.create!(filename: "'+bash_input+'",'+' values: "')
    # write answer value(s)
    for line in i:
        # end of problem statement reached
        if line.strip() == ':eans:':
            break
        # remove extra <p> and </p> tags
        if 'p>' in line:
            print line
        # write values as a string
        else:
            numList = str([x for x in line.strip().split('|')])
            o.write(numList[1:len(numList)-1])
    o.write('", interface: "')

# TODO determine if html should remain in interface
# write answer template
o = open('seed_' + bash_input, 'a')
i = open(bash_input)
with i,o:
    for line in i:
        if line.strip() == ':bansinf:':
            break
    for line in i:
        if line.strip() == ':eansinf:':
            break
        o.write(line.strip()+' ')
    o.write('")'+ "\n")

# TODO multiple solutions, use applicaitons/liquids/liquid16 as testfile
# write solution tuple(s)
o = open('seed_' + bash_input, 'a')
i = open(bash_input)
with i,o:
    for line in i:
        if ':bsol:' in line:
            # write boilerplate for tuple
            o.write('#SOLUTION TUPLE' + "\n")
            o.write('Solution.create!(filename: "'+bash_input+'",'+' typ: "')
            # use regex to extract type from input file
            typ = re.search(r'type=(.*):', line).group(1)
            o.write(typ + '", text: "')
            break
    # write contents
    for line in i:
        if line.strip() == ':esol:':
            break
        o.write(line.strip()+' ')
    o.write('")'+ "\n")

# TODO multiple hints, but Robert has setup MAM (Math Affirm Markup) so that
# types of hints follow types of solutions (for example 1 graphical solution
# + 2 graphical hints, 1 numerical solution + 1 numerical hint)
# write hint tuple
o = open('seed_' + bash_input, 'a')
i = open(bash_input)
with i,o:
    for line in i:
        if line.strip() == ':bhint:':
            break
    # write beginning of create command for the tuple going to hint
    o.write('#HINT TUPLE' + "\n")
    o.write('Hint.create!(filename: "'+bash_input+'",'+' text: "')
    for line in i:
        # end of problem statement reached
        if line.strip() == ':ehint:':
            break
        # TODO placeholder for dealing with figures, if needed
        #  if '<img src' in line:
            #  o.write('"')
            #  # do something
        o.write(line.strip()+' ')
    o.write('")'+ "\n")

# write any metadata
o = open('seed_' + bash_input, 'a')
i = open(bash_input)
with i,o:
    # find category
    for line in i:
        if line.strip() == ':bcat:':
            break
    #  write boilerplate
    o.write('#METADATA TUPLE' + "\n")
    o.write('PrbMetaData.create!(filename: "'+bash_input+'", category: "')
    # write category
    for line in i:
        # end of category reached
        if line.strip() == ':ecat:':
            break
        # write until end of category
        o.write(line.strip())
    # next attribute
    o.write('", context: "')
    # goto context block
    for line in i:
        # found context
        if line.strip() == ':bcontext:':
            break
    # for all context
    for line in i:
        # end of context block
        if line.strip() == ':econtext:':
            break
        # write context block
        o.write(line.strip())
    # next attribute
    o.write('", diff: ')
    # goto difficulty block
    for line in i:
        # found difficulty
        if line.strip() == ':bdif:':
            break
    # for all difficulty
    for line in i:
        # end of difficulty block
        if line.strip() == ':edif:':
            break
        # write difficulty block
        o.write(line.strip())
    # next attribute
    o.write(', source: "')
    # goto source block
    for line in i:
        # found source
        if line.strip() == ':bsource:':
            break
    # for all source
    for line in i:
        # end of source block
        if line.strip() == ':esource:':
            break
        # write source block
        o.write(line.strip())
    # finish metadata tuple
    o.write('")'+ "\n")
