from typing import Iterable
# flake8
# change config for flake8
# async python + yield from
# coroutines
# textwrap - look
# descriptor protocol and get_attr(); descriptor how to?


# ls = [1, 2, 3, 4]
# it = iter(ls)
# it1 = iter(it)

# print(id(it) == id(it1))
# print(it is it1)    # "is"
#
# print(next(it))
# print(next(it))
# print(next(it))
#
# for i in it:
#     print(i)

#
# def func(iterbl: Iterable):
#     x = yield from iterbl
#     print("this is my print() in func - ", x)
#     return 25
#
#
# def func2():
#     ite = range(4)
#     yield from ite
#     return 40
#
#
# gen = func(func2())
# a = next(gen)    # 1
# next(gen)    # 2
# next(gen)    # 3
# next(gen)    # 4
# next(gen)    # 5


def gen():
    x = yield 'hello from generator'
    print(repr(x))
    yield 'smth'


g = gen()
print(next(g))

print(g.send("I have stopped"))
# print(next(g))


# def pool_data():
#     books = []
#
#     page = 1
#     while True:
#         res = req.get(page=page, page_size = 100)
#         books.extend(res["books"])
#         if len(res["books"] < 100):
#             break
#         page +=1
#     return books
#
#
#
# for book in pool_data():
#     process book
#




class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
       # yield from self.data

       # return iter(self.data)
        for i in self.data:
            # some logic to process i
            yield i



print(list(MyIterable([1,2, 3, 4])))