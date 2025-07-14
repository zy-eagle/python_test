from sys import exception

try:
    1/0
except ZeroDivisionError as e:
    print(f"An exception occurred: {e}")

print("##########################################")

try:
    1/0
except Exception as e:
    print(f"An exception occurred: {e}")

print("##########################################")

try:
    1/0
except Exception as e:
    print(f"An exception occurred: {e}")
finally:
    print("This block always executes, regardless of an exception.")

print("##########################################")
try:
    1/0
except Exception as e:
    print(f"An exception occurred: {e}")
else:
    print("This block executes if no exception occurs.")

print("##########################################")

try:
    1/0
except Exception as e:
    print(f"An exception occurred: {e}")
except ZeroDivisionError as e:
    print(f"A specific exception occurred: {e}")

print("##########################################")

class MyException(Exception):
    """Custom exception class for demonstration purposes."""
    def __init__(self, msg):
        self.__msg = msg

    @property
    def msg(self):
        return f"Custom exception message: {self.__msg}"

try:
    raise MyException("custom error")
except MyException as e:
    print(f"A custom exception occurred: {e.msg}")
