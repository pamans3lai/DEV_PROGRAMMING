class KekeuatanDua:
    def __init__(self, max_eksponen):
        self.max = max_eksponen
        self.n = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

for val in KekeuatanDua(3):
    print(val)
