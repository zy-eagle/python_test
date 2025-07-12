print("##################### 基础 ###########################")
print("hello world!")

## keyboard input
# var = input("please input: \n")
# print(var)

var = 123
print(type(var))

print("###########################")

print('please learn "python"!')

print("""
three
multiple
quotes
""")

print('''
three 
single 
quotes
''')

print("###########################")

print(f"output: {var}")

print("###########################")

print("x" in "123x456")
print("x" not in "123x456")

print("###########################")

print("hello" + "world")
print("hello" * 3)

print("###########################")
s = "abcde"
print(s[0])
print(s[1:4])
print(s[-1])  # last char
print(s[-2:])  # last two chars
print(s[1:4:2])  # step 2
print(s[::-1])  # reverse string

print("###########################")
print("abc".count("a"))  # count occurrences of 'a'
print("abc".isalnum())

print("abc".isalpha())
print("adb".startswith("a"))
print(",".join("abc"))
print("a,b,c".split(","))

print("###########################")
print(str(123))
print(int("123"))

print("ABC" > "ABD")
# print("abc">123)
print(123.1 > 123)

print("#################### list ###########################")
list = ['a', 'b', ['c', 'd']]

print(list[0])
print(list[2][1])

print("###########################")

list[2].insert(1, 'x')
print(list)

list.insert(1, 'x')
print(list)

list.append('e')  # append 'e' to the end
print(list)

list.extend(['f', 'g'])
print(list)

list.extend("hj")
print(list)  # extend list with ['f', 'g']

print("###########################")

list.remove('a')
print(list)

print(list.pop(1))  # remove element at index 1

print(list.copy())

list.clear()
print(list)  # clear the list

print("#################### tuple ###########################")

tuple1 = ('a', 'b', 'c')
print(tuple1[0])

tuple1 = ('a', 'b', ['c', 'd'])
print(tuple1[2][1])

print("#################### set ###########################")

set1 = {1, 2, 3, (2, 3)}

set1.add(1)  # add 1, no effect since 1 already exists
print(set1)

set1.pop()
print(set1)

set1.remove(2)
print(set1)

list1 = [1, 2, 3, 4, 3, 1, 5]
set2 = set(list1)  # convert list to set
print(set2)

print("#################### dict ###########################")
dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1['a'])  # access value by key
print(len(dict1))  # get number of key-value pairs

for k, v in dict1.items():
    print(f"{k} -> {v}")  # iterate through key-value pairs

print(dict1.keys())
print(dict1.values())
print(dict1.setdefault('d', 4))

print("d" in dict1)  # check if key 'd' exists

print(dict1.popitem())  # remove and return the last inserted key-value pair
print(dict1)

dict2 = dict1.copy()  # create a shallow copy
dict1['a'] = 10
dict2['d'] = 10
print(dict1)
print(dict2)
dict2 |= dict1
print(dict2)
print(f"result:{dict2}")
print(type(None))


