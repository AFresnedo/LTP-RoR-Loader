# function called on first line of answer module and runs until first line of
# solution
def processAnswers(i, o):
    # for all text in answer module(s)
    for line in i:
        # check for beginning of solution module and exit iff found
        if ':btype:' in line:
            break
        # find :bans: line
        elif ':bans:' in line:
            # check for type, use default if missing
            if 'mc' in line:
                processMultipleChoice(i, o)
            elif 'cb' in line:
                processCheckboxes(i, o)
            else:
                processDefault(i, o)

# process a single fill-in-the-boxes answer set
def processDefault(i, o):
    # process answer values
    o.write('#ANSWER TUPLE FOR PROBLEM P\n')
    o.write('p.answer = Answer.new(values: "')
    for line in i:
        if ':eans:' in line:
            break
        o.write(line.strip())
    assert ':eans:' in line
    # process interface
    o.write('", interface: "')
    for line in i:
        if ':bansinf:' in line:
            break
        assert ':bansinf:' in line
        for line in i:
            if ':eansinf:' in line:
                break
            o.write(line.strip() + ' ')
        o.write('")\n')

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
