import sys, os

bash_input = sys.argv[1]
o = open('seed_' + bash_input, 'w+')
# create tuple for problem statement
i = open(bash_input)
with i:
    for line in i:
        if line.strip() == ':btheo:':
            break
    # write beginning of create command for the tuple going to Problem
    o.write('#THEORY TUPLE' + "\n")
    o.write('Theory.create!(filename: "'+bash_input+'", text: "')
    for line in i:
        # end of problem statement reached
        if line.strip() == ':etheo:':
            break
        # TODO placeholder for dealing with figures, if needed
        #  if '<img src' in line:
            #  o.write('"')
            #  # do something
        o.write(line.strip()+' ')
    o.write('")'+ "\n")
