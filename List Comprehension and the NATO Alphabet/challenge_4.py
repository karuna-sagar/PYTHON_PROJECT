with open("Day_26 List Comprehension and the NATO Alphabet/file1.txt") as data1:
    data_1 = data1.readlines()
    print(data_1)
with open("Day_26 List Comprehension and the NATO Alphabet/file2.txt") as data2:
    data_2 = data2.readlines()
    print(data_2)
result = [int(num)for num in data_1 if num in data_2]
print(result)