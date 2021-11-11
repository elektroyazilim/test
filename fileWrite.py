# with open("text.txt") as file:
# 	print(file.read())

# with open("text.txt", "r") as reader:
# 	content = reader.readlines()
# 	print(content)
# 	with open("text.txt","w") as writer:
# 		for line in reversed(content):
# 			writer.write(line)

with open("text.txt", "r") as reader:
	content = reader.readlines()
	print(content)
	with open("text.txt","w") as writer:
		writer.writelines(reversed(content))