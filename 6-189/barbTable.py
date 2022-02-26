"""This exercise is proposed by me (gbarberini), as way to say goodbye to thinkpython2, gonna miss you Allen, very nice book!

In the end of the book there is a section called Apendix B.Analysis of Algorithms, that will be further discussed in another Allen book, but I decided to already warm up the concept of Hashtables, so here it goes:

Implement a new type of HashTable called BarbTable and a new kind of dictionary called Barbonary (yeahhhhh), where this new dictionary can be pseudo-hashed (not sure if it is possible to hash for every case) as a key for the new HashTable.

While:
    * Avoiding to use things not explained in the book

Lets try this out!"""

#My sollution was to adapt Allen's HashMap a little bit

class LinearMap:
    def __init__(self):
        self.items = []

    def add(self, k, v):
        if type(k) == type(Barbonary()):
            k = k.copy()
        self.items.append((k, v))

    def get(self, k):
        for key, val in self.items:
            if key == k:
                return val
        raise KeyError

class BetterMap:
    def __init__(self, n=100):
        self.maps = []
        for i in range(n):
            self.maps.append(LinearMap())
 
    def find_map(self, k):
        if type(k) == type(Barbonary()):
            index = k.header() % len(self.maps)
            return self.maps[index]
        else:
            index = hash(k) % len(self.maps)
            return self.maps[index]

    def add(self, k, v):
        m = self.find_map(k)
        m.add(k, v)

    def get(self, k):
        m = self.find_map(k)
        return m.get(k)

class BarbTable:
    def __init__(self):
        self.maps = BetterMap(2)
        self.num = 0

    def get(self, k):
        return self.maps.get(k)

    def add(self, k, v):
        if self.num == len(self.maps.maps):
             self.resize()
        self.maps.add(k, v)
        self.num += 1

    def resize(self):
        new_maps = BetterMap(self.num * 2)
        for m in self.maps.maps:
            for k, v in m.items:
                new_maps.add(k, v)
        self.maps = new_maps

class Barbonary(dict):
    def header(self):
        cur_hash = 1
        for k, v in self.items():
            if type(v) == type(list()) or type(v) == type(dict()):
                cur_hash *= ((hash(k)-1))*self.barbHash(v)
                continue
            cur_hash *= ((hash(k)-1))*hash(v)
            #-1 here to make sure that a inverse dict will not have the same hash
        return cur_hash

    def barbHash(self, v):
        fhash = 1
        for item in v:
            if type(item) == type(list()) or type(item) == type(dict()):
                fhash *= self.barbHash(item)
                continue
            fhash *= hash(item)
        return fhash

'''Testing'''
if __name__ == '__main__':

    d = Barbonary() 
    h = BarbTable()
    v = []

    h.add(d, v)
    print(h.get(d))

    h.get(d).append("test")
    print(h.get(d))

    h.get(d).append("test2")
    print(h.get(d))

    d2 = Barbonary()
    print(h.get(d2))

    d.setdefault("3", "test3")
    print(h.get(d2))
    print(d)

    try:
        h.get(d)
    except:
        del d["3"]
        print(d)
        print(h.get(d))

    d = Barbonary()
    d[3] = []
    d[3].append("ola mutchachosoooos819246817926481989)#&@(*!&*%ˆ&@!%$9")

    b = Barbonary()
    b[3] = []
    b[3].append("ola mutchachosoooos819246817926481989)#&@(*!&*%ˆ&@!%$9")

    h.add(d, "its d bro")
    print(h.get(d))
    print(h.get(b))

    b[4] = []
    try:
        print(b)
        print(h.get(b))
    except:
        del b[4]
        print(b)
        print(h.get(b))
