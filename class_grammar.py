class Klass:

   # member_var = 1

    @classmethod
    def func1(self):
        print("class method")

    @staticmethod
    def func2():
        print("static method")

    @property
    def func3(self):
        return self.__var_name

    @func3.setter
    def func3(self, value):
        self.__var_name = value

print(Klass.func1())
print(Klass.func2())
k = Klass()
k.func3 = "Hello"
print(k.func3)

