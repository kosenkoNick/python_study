# 2 ways to create iterable object - __getitem__() or iterator protocol
# methods, that were imported are a part of this module now
# magic mock - ??? mocker: MockerFixture - ??? monkey patch
# unittest.mock - ???
# fixture, setup, tier-down
# flaky tests
# code isolation

class MyIterable:

    def __iter__(self):
        return iter([1,2,3])


from typing import Iterable


print(isinstance(MyIterable(), Iterable))
print(list(MyIterable()))



class MyNotIterable:
    data = [1,2,3]

    # def __getitem__(self, item):
    #     return self.data[item]


Iterable.register(MyNotIterable)  # virtual subclass


print(isinstance(MyNotIterable(), Iterable))
print(list(MyNotIterable()))

try:
    iter(MyNotIterable())
except:
    ...
