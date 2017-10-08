def processAnswers(i, o):
    # while answer sets remain
    # determine type of answer
    # call appropriate functions
    None

# process a single fill-in-the-boxes answer set
def processDefault(i, o):
    # process answer
    # process interface
    None

# process a single standard multiple choice
def processMultipleChoice(i, o):
    # process answer list
    # process question
    None

# process a single checkboxes version of multiple choice
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
