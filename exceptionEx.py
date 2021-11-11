# itemsInCard = 0
#
# if itemsInCard != 2:
# 	raise Exception("Count not matching")


# itemsInCard = 0
#
# if itemsInCard != 2:
# 	pass
#
# assert (itemsInCard == 2)


# try:
# 	with open("filelog.txt", "r") as reader:
# 		reader.read()
# except:
# 	print("There is no such a file")
# print("try - catch is finished")

# try:
# 	with open("filelog.txt", "r") as reader:
# 		reader.read()
# except Exception as e:
# 	print(e)
# print("try - catch is finished")

try:
	with open("filelog.txt", "r") as reader:
		reader.read()
except Exception as e:
	print(e)
finally:
	print("cleaning up resources")
print("try - catch is finished")