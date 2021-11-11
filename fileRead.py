# file = open("text.txt")
#
# print(file.read(7))
#
# file.close()

# file = open("text.txt")
#
# print(file.read(7))
# print(file.readline())
# print(file.readline())
#
# file.close()


# file = open("text.txt")
#
# line = file.readline()
# while line != "":
# 	print(line)
# 	line = file.readline()
#
# file.close()

file = open("text.txt")

for line in file.readlines():
	print(line)

file.close()

