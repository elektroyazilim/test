num = 5;

while num > 0:
	print(num)
	num -= 1;
#print("while loop finished")

num = 5;

while num > 0:
	if num != 3:
		print(num)
	num -= 1;
#print("while loop finished")


num = 5;

# while num > 0:
# 	if num == 3:
# 		break;
# 	print(num)
# 	num -= 1;
# print("while loop finished")

num = 6;

while num > 0:
	num -= 1
	if (num % 2):
		continue
	print(num)

print("while loop finished")