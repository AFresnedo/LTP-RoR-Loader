import re
# this module holds the functions to process multiple sections of a problem
# file for Math Affirm

def processChunk(i, o):
    processSolution(i, o)
    processHint(i, o)

# pre: file iterator is on line with :bsol: WARNING: NO CHECK
def processSolution(i, o):
    # write seperation comment for seed file organization
    o.write('#SOLUTION TUPLE FOR PROBLEM\n')
    # write start of solution tuple for problem P (defined in problem_input)
    o.write('S = P.Solution.create!(typ: "')
    # use regex to extract type from input file
    typ = re.search(r'type=(.*):', i.next()).group(1)
    # write solution type attribute
    o.write(typ + '", text: "')
    # write solution text attribute
    for line in i:
        # break when end of sol's text found
        if line.strip() == ':esol:':
            break
        # write solution's text
        o.write(line.strip()+' ')
    # finish writing text attribute
    o.write('")'+ "\n")

# pre: file iterator is on line with :esol: (of relevant solution)
def processHint():
    # go until next solution OR next category (TODO: next curriculum)
    while (':bcat:' not in line.strip()) and (':bsol:' not in line.strip()):
        o.write('#HINT TUPLE FOR SOLUTION\n')
        o.write('S.Hint.create!(text: "')
        for line in i:
            if line.strip() == ':ehint:':
                break
            # placeholder for dealing with figures, if needed
            #  if '<img src' in line:
            o.write(line.strip()+' ')
        o.write('")'+ "\n")
