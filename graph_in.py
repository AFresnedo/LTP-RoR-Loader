import sys
import re

for filename in sys.stdin:
    filename = filename.strip()
    # get directory path and filename
    match = re.search('(.*/).+.txt', filename)
    # save directory path for referencing problems
    dirPath = match.group(1)
        # create seed_file for file
    o = open(filename + '_seed', 'w')
    # open source file
    i = open(filename)
    with i, o:
        # add comment seperation for seed file organization
        o.write('#GRAPH TUPLES FROM '+filename+"\n")
        # write graph tuple(s)
        batch_number = 0
        for line in i:
            # remove formatting characters
            line = line.strip()
            makeup_flag = 'false'
            # if it is a whitespace-only line, begin new batch
            if line == '':
                batch_number += 1
            # if it is a problem file line
            elif re.match('.*theory.*\.html', line) is None:
                # check if makeup, remove makeup flag
                if line[:1] == '+':
                    makeup_flag = 'true'
                    line = line[1:]
                # find problem_id
                o.write('p = Problem.find_by(filename: \''+dirPath+line+'\')\n')
                # write graph tuple
                # (filename, context, batch_number, makeup, foreign_key_problem_id)
                batch = str(batch_number)
                makeup = str(makeup_flag)
                o.write('Graph.create!(typ: \'prob\', context: \''+dirPath
                        +'\', batch: '+batch+', makeup: '+makeup
                        +', file_id: p.id)\n')
            # must be theory file line
            else:
                batch = str(batch_number)
                o.write('Graph.create!(typ: \'theory\', context: \''
                        +dirPath+'\', batch: '+batch+', file_id: 0, '
                        +'makeup: false)\n')
