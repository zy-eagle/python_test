add = lambda x: x + 1
print(add(1))

print("##########################")

def foo(argv1, argv2=200, argv3=None):
    print(argv1)
    print(argv2)
    print(argv3)
    return argv1 + argv2 + argv3
print(foo(100, argv3=300))

print("##########################")

## *tel 可变位置参数, 元组形式存储
## **custom 可变关键字参数，字典形式
def address_book(name, *tel, alias_name=None, **custom):
    print(name)
    print(tel)
    print(alias_name)
    print(custom)

address_book("Alice", "123-4567", "234-5678", alias_name="Alicia", email="eagle@163.com")

print("##########################")

# 函数内省属性--内置方法和属性
print(foo.__dir__())

print("##########################")

# map 高阶函数
# map(function, iterable) 返回一个迭代器
print(list(map(lambda x: x * 2, [1, 2, 3])))

# filter 高阶函数
# filter(function, iterable) 返回一个迭代器
print(list(filter(lambda x: x=="Alice" in x, ["Alice", "Bob"])))

# reduce 高阶函数
from functools import reduce
# reduce(function, iterable) 返回一个累加值
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))


# partial 高阶函数
from functools import partial
# partial(function, *args, **kwargs) 返回一个新的函数
def multiply(x, y):
    return x * y
multiply_by_2 = partial(multiply, 2)
print(multiply_by_2(3))  # 6

print("##########################")

# 装饰器示例
from functools import wraps
def time_it(func):
    import time
    @wraps(func)  # 保留原函数的元数据
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@time_it
def slow_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

print(slow_function(10))  # 测试装饰器的性能
print(slow_function.__name__)













