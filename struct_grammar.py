print("######################## if #########################")
num = 1
if num % 2 == 0:
    print("number is even")
elif num % 2 == 1:
    print("number is odd")
else:
    print("error number")
    print("double check the number")

print("######################## match #########################")

match num:
    case _ if num % 2 == 0:
        print("number is even")
    case _ if num % 2 == 1:
        print("number is odd")
    case _:
        print("error number")
        print("double check the number")

status = 200
match status:
    case 200:
        print("ok")
    case 404 | 403:
        print("bad request")
    case _:
        print("server error")

print("######################## while #########################")

num = 3
while num > 0:
    print(num)
    num -= 1

print("######################## for #########################")

for ele in range(5):
    print(ele)
    if ele == 2:
        print("break")
        break

# 推导式
list1 = [i for i in range(5)]
print(list1)
