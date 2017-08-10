import sys
import re

filename = sys.argv[1]
print 'Processing file: '+filename

o = open(filename + '_seed', 'w')
i = open(filename)

# TODO the way ordering works now is really flimsy, redo it later, because
# it requires a theoryfile for every category
with i, o:
    # get curriculum attribute, same for every line
    curriculum = sys.argv[2]
    curriculum = str.lower(curriculum)
    # variables for determining order
    category_order = 0
    context_order = 0
    for line in i:
        # get attributes for tuple
        category = str.lower(re.match('(.*)/', line).group(1))
        context = str.lower(re.match('.*/(.*)', line).group(1))
        context = context.strip()
        # if context is a theory file
        if re.match('.*\.html', context):
            # increase category order for new category
            category_order += 1
            # reset context order, it's a new category
            context_order = 0
            # write tuple for theory file
            o.write('Globalgraph.create!(curriculum: \''+curriculum
                    +'\', category: \''+category
                    +'\', context: \'category_introduction'
                    +'\', category_order: '+str(category_order)
                    +', context_order: '+str(context_order)+')\n')
        # else line is a directory
        else:
            # increase context order, still in the same category
            context_order += 1
            o.write('Globalgraph.create!(curriculum: \''+curriculum
                    +'\', category: \''+category
                    +'\', context: \''+context
                    +'\', category_order: '+str(category_order)
                    +', context_order: '+str(context_order)+')\n')
