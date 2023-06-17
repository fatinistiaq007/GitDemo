#read the file and store all the lines in list
#reverse the list and write back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines()    #[ay, b, c444 hhhh, d, ettrrtr  tttrrtr]
    reversed(content)
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

