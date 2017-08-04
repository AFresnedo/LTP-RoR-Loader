# this module holds the functions to process multiple sections of a problem
# file for Math Affirm

# processSolution method, which processes a single solution and its hints
    o.write('#SOLUTION TUPLE' + "\n")
    o.write('Problem.Solution.create!(typ: "')
    # use regex to extract type from input file
            typ = re.search(r'type=(.*):', line).group(1)
            o.write(typ + '", text: "')
            break
