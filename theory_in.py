import json
import re
import sys

for filename in sys.stdin:
    filename = filename.strip()
    print "Processing file: "+filename
    o = open(filename + '_theory_seed', 'w')
    i = open(filename)
    with i, o:
        for line in i:
            if ':btheo:' in line:
                break
        assert ':btheo:' in line
        # write Theory tuple
        # add comment seperation for seed file organization
        o.write('#THEORY TUPLE' + "\n")
        o.write('Theory.create!(filename: "'+filename+'", text: "')
        # fill in text attribute
        text = ''
        for line in i:
            # break when end of problem statement reached
            if ':etheo:' in line:
                # write string representing text with escaped quoted, etc
                o.write(json.dumps(text))
                break
            # TODO placeholder for dealing with figures, if needed
            #  if '<img src' in line:
                #  o.write('"')
                #  # do something
            text += line
        assert ':etheo:' in line
        o.write('")'+ "\n")
