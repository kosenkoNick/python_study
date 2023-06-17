

def func(self, addit_par=0):
    print(addit_par)
    par1 = list(self)
    return par1
    # tuple, list, range, array, dict


d = {'a': 1, 'b': 0}
for temp in d:
    print(temp)

print(list(d))

list1 = [[k, d[k]] for k in d]
print(list1)

print(dir(d))

print(list(d.items()))

print(isinstance(d, object))

v = print

a = str.find
print(type(a))


class MyClass:
    def __iter__(self):
        return iter([1, 2, 3])

    x = func

    def met(self):
        ...

    @classmethod
    def met1(cls):
        cls = MyClass
        ...


a = MyClass.met
print(type(a))

print(type(MyClass.met1))



print(type(MyClass().x))
print(type(MyClass.x))  # get_attr <=> getX()

# Functions are in class. Class instances stores data (state) and access to class

print(MyClass.__getattribute__(MyClass, 'x'))
print(MyClass().__getattribute__('x'))

# Object gets class with:
# a = type(object)
# a.__getattribute__('func_name')

vara = MyClass()
MyClass.x(vara)

# method is a container, storing access to function-fabric
# for this particular method and access to instance(it will be the first parameter in function call)


m = func.__get__(vara)
print(type(m))

func(vara)

print(m(5))

print(vara.met())


vara()
