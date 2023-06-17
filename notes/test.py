from uu import Error
from exceptiongroup import catch


class MyIterator():
    def __init__(self, collection) -> None:
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration
        else:
            num = self.index
            self.index += 1
            return self.collection[num]
        

def negate_all(iterable):
    for n in iterable:
        print("Negating", n)
        yield -n



ls = [1, 2]

gen = negate_all(ls)

it = iter(ls)

my_it = MyIterator(ls)

print('hello')
