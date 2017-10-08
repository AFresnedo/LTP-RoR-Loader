def processModules(i, o):
    # while modules remain
    # determine type of module
    # call appropraite methods
    None

# process a single fill-in-the-boxes module
def processDefaultModule(i, o):
    # process answer
    # process interface
    None

def processMultipleChoice(i, o):
    # process answer list
    # process question
    None

def processCheckboxes(i, o):
    # process answer list
    # process question
    None

    #  # Answer tuple
    #  # write beginning of create command for p.Answer tuple
    #  o.write('#ANSWER TUPLE FOR PROBLEM P' + "\n")
    #  # get problem tuple from database (doesn't seem to work otherwise)
    #  o.write('p.answer = Answer.new(values: "')
    #  # write answer value(s)
    #  for line in i:
        #  # end of problem statement reached
        #  if ':eans:' in line:
            #  break
        #  o.write(line.strip())
    #  # end writing answer value(s)
    #  assert ':eans:' in line
    #  o.write('", interface: "')
    #  # find interface text
    #  for line in i:
        #  if ':bansinf:' in line:
            #  break
    #  assert ':bansinf:' in line
    #  # write interface
    #  for line in i:
        #  if ':eansinf:' in line:
            #  break
        #  if 'p>' not in line:
            #  o.write(line.strip() + ' ')
    #  o.write('")\n')
