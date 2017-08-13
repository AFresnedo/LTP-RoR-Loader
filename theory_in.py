import json
import re
import sys

# filename is a theory.html file
for filename in sys.stdin:
    filename = filename.strip()
    print "Processing file: "+filename
    # get directory path and filename
    match = re.search('(.*)\/(.*\.html)', filename)
    # save directory path for referencing problems
    dirPath = match.group(1)
    dirPieces = dirPath.split('/')
    category = str.lower(dirPieces[1])
    if len(dirPieces) == 3:
        context = str.lower(dirPieces[2])
    elif len(dirPieces) == 2:
        context = 'category_introduction'
    else:
        assert False
    localName = match.group(2)
    o = open(filename + '_theory_seed', 'w')
    i = open(filename)
    with i, o:
        # goto beginning of theory text
        for line in i:
            if ':btheo:' in line:
                break
        assert ':btheo:' in line
        # write Theory tuple
        # add comment seperation for seed file organization
        o.write('#THEORY TUPLE FOR' +filename+ "\n")
        # TODO replace filename with local filename
        o.write('Theory.create!(category: \''
                +category+'\', context: \''
                +context+'\', filename: \''
                +localName+'\', text: ')
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
        o.write(')\n')
