import re
# this module holds the functions to process multiple sections of a problem
# file for Math Affirm

def processChunk(i, o, typ):
    # process solution
    processSolution(i, o, typ)
    # find first hint
    hintFound = False
    for line in i:
        if ':bhint:' in line:
            hintFound = True
            break
    assert ':bhint:' in line
    # while hint(s) remaining for this solution
    while hintFound:
        # process hint
        processHint(i, o)
        # check if hints still remain
        for line in i:
            # if more hints remain for this solution, find next
            if ':bhint:' in line:
                break
            # no hints remaining for this solution
            if ':bsol:' in line:
                # other solutions remain, recursive call
                typ = re.search(r'type=(.*):', line).group(1)
                processChunk(i, o, typ)
                # finish hints/solutions
                hintFound = False
                break
            if ':bcat:' in line:
                # end of hints/solutions in problem
                hintFound = False
                break

# pre: file iterator is on line with :bsol: WARNING: NO CHECK
def processSolution(i, o, typ):
    # write seperation comment for seed file organization
    o.write('#SOLUTION TUPLE FOR PROBLEM P\n')
    # write start of solution tuple for problem P (defined in problem_input)
    o.write('S = P.Solution.create!(typ: "')
    # use regex to extract type from input file
    # write solution type attribute
    o.write(typ + '", text: "')
    # write solution text attribute
    for line in i:
        # break when end of sol's text found
        if ':esol:' in line:
            break
        # write solution's text, TODO escape quotes
        o.write(line.strip()+' ')
    # finish writing text attribute
    o.write('")'+ "\n")

# pre: file iterator is on line with :esol: (of relevant solution)
def processHint(i, o):
    o.write('#HINT TUPLE FOR SOLUTION S\n')
    o.write('S.Hint.create!(text: "')
    for line in i:
        if ':ehint:' in line:
            break
        # placeholder for dealing with figures, if needed
        #  if '<img src' in line:
        # TODO escape quotes
        o.write(line.strip()+' ')
    o.write('")'+ "\n")
