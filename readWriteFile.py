file = open('test.txt')
# print(file.read(4))       #real all the contents of file

#read one single line at a time readline()
# print(file.readline())
# print(file.readline())
# print(file.readline())

#print line by line using readline method
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

#print line by line using readlines method
for line in file.readlines():
    print(line)


file.close()