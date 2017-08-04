def processLine():
    o.write(line.strip())

i = open('test_input.txt')
o = open('test_output.txt', 'w')
with i, o:
    for line in i:
        if line.strip() == '3':
            break
    o.write(line.strip())
    processLine()
    o.write('\nit worked?')
