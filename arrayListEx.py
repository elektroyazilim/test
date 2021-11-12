# arrayList example

values = [1, 5, 9.9, "test"]
print(f"{values}" + " tipi : " + str(type(values)));

print("First element : ", values[0])
print("Last element : ", values[-1])

values = [1, 5, 9.9, "test"]
print(values)
print(values[1:3], " : 1. ve 2. indexli eleman alınır son index dahil edilmez.")
print(values[:3], "İlk 3 elemanı alır; 0,1,2")
print(values[:], "Tüm elemanlar gelir, baştan sona")
print(values[1:], "1.index ten sona kadar gelir")
print(values[::-1], "Dizi elemanlarını tersten getirir.")

values = [1, 5, 9.9, "test"]
print(values)
values.insert(2, 0)

print(values)
values.append(10)
print(values)

values = [1, 5, 0, 9.9, 'test', 10];
print(values)
values[2]= 33;
print(values)

values = [1, 5, 33, 9.9, 'test', 10]
print(values)
values.remove(33);
print(values)

values = [1, 5, 33, 9.9, 'test', 10]
print(values)
del values[-1]
print(values)
