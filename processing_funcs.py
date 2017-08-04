import re
# this module holds the functions to process multiple sections of a problem
# file for Math Affirm

def processChunk(i, o):
    # process solution
    processSolution(i, o)
    # TODO skip if no hints to a solution? is that valid?
    # process hint(s)
    processHint(i, o)

# pre: file iterator is on line with :bsol: WARNING: NO CHECK
def processSolution(i, o):
    # find beginning of solution section
    for line in i:
        if ':bsol:' in line:
            break
    assert ':bsol:' in line
    # write seperation comment for seed file organization
    o.write('#SOLUTION TUPLE FOR PROBLEM P\n')
    # write start of solution tuple for problem P (defined in problem_input)
    o.write('S = P.Solution.create!(typ: "')
    # use regex to extract type from input file
    typ = re.search(r'type=(.*):', line).group(1)
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
def processHint(i, o):
    # goto hint section
    for line in i:
        if line.strip() == ':bhint:':
            break
    assert ':bhint:' in line
    o.write('#HINT TUPLE FOR SOLUTION S\n')
    o.write('S.Hint.create!(text: "')
    for line in i:
        if line.strip() == ':ehint:':
            break
        # placeholder for dealing with figures, if needed
        #  if '<img src' in line:
        o.write(line.strip()+' ')
    o.write('")'+ "\n")
