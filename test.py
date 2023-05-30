from typing import List

class StrLenIterator:

    def __init__(self,l:List[str]):
        self.data = l
        self.id = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.id < len(self.data):
            r = (self.data[self.id], len(self.data[self.id]))
            self.id += 1
            return r
        else:
            raise StopIteration
        

l = ["in","bocca","al","lupo"]
it = StrLenIterator(l)
for x in it:
    print(x,end=" ")