##################### 基础 ###########################
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
print(s[-1]) # last char
print(s[-2:]) # last two chars
print(s[1:4:2]) # step 2
print(s[::-1]) # reverse string

print("###########################")
print("abc".count("a")) # count occurrences of 'a'
print("abc".isalnum())

print("abc".isalpha())
print("adb".startswith("a"))
print(",".join("abc"))
print("a,b,c".split(","))

print("###########################")
print(str(123))
print(int("123"))

#################### 函数 ###########################