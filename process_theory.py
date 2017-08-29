import json
import re
import sys

# ~, home, lancaster, Documents, persProj, ma_files
fillerPathLength = 6
# filename is a theory.html file
for filename in sys.stdin:
    filename = filename.strip()
    print "Processing theory file: "+filename
    # get directory path and filename
    match = re.search('(.*)\/(.*\.html)', filename)
    # save directory path for referencing problems
    # first 6 are useless, atm TODO do not depend on shell path
    dirPath = match.group(1)
    dirPieces = dirPath.split('/')
    curriculum = str.lower(dirPieces[fillerPathLength])
    category = str.lower(dirPieces[fillerPathLength+1])
    # if there is a context
    if len(dirPieces) == fillerPathLength+3:
        context = str.lower(dirPieces[fillerPathLength+2])
    # else theoryfile IS the context, as an introduction
    elif len(dirPieces) == fillerPathLength+2:
        context = 'category_introduction'
    else:
        raise "undefinable context"
    localName = match.group(2)
    o = open(filename + '_theory_seed', 'w')
    i = open(filename)
    with i, o:
        # goto beginning of theory text
        for line in i:
            if ':btheo:' in line:
                break
        if ':btheo:' not in line:
            raise ":btheo: not found"
        # write Theory tuple
        # add comment seperation for seed file organization
        o.write('#THEORY TUPLE FOR' +filename+ "\n")
        # TODO replace filename with local filename
        o.write('Theory.create!(curriculum: \''
                +curriculum+'\', category: \''
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
        if ':etheo:' not in line:
            raise ":etheo: not found"
        o.write(')\n')
