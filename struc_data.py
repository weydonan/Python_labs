# очередь, стек, deque

# очередь, last: Nodelist\None; put; get; isempty; первый пришёл, первый ушёл

# стек Filo; push; pull

# deque Lput, Rput

class Knot:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0

    def put(self, data):
        knot = Knot(data)
        if (self.is_empty()):
            self.first = knot
            self.last = knot
            self.size += 1
        else:
            self.last.next = knot
            self.last = knot
            self.size += 1

    def is_empty(self):
        return self.first is None

    def get(self):
        if self.is_empty():
            return None
        knot_data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.size -= 1
        return knot_data


class Stack:
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0

    def push(self, data):
        knot = Knot(data)
        if (self.is_empty()):
            self.last = knot
            self.first = knot
            self.size += 1

        else:
            knot.next = self.first
            self.first = knot
            self.size += 1

    def pull(self):
        if self.is_empty():
            return None
        knot_data = self.first.data
        self.first = self.first.next
        self.size -= 1
        return knot_data

    def is_empty(self):
        if (self.first is None):
            return True
        return False


class Knot_2:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.pr = None


class Deque:
    def __init__(self):
        self.last = None
        self.first = None
        self.size = 0

    def Lput(self, data):
        knot = Knot_2(data)
        if (self.is_empty()):
            self.first = knot
            self.last = knot
            self.size += 1
        else:
            knot.next = self.first
            self.first.pr = knot
            self.first = knot
            self.size += 1

    def Rput(self, data):
        knot = Knot_2(data)
        if (self.is_empty()):
            self.last = knot
            self.first = knot
            self.size += 1

        else:
            knot.pr = self.last
            self.last.next = knot
            self.last = knot
            self.size += 1

    def is_empty(self):
        if (self.first is None or self.last is None):
            return True
        return False

    def Lget(self):
        if self.is_empty():
            return None
        knot_data = self.first.data
        self.first = self.first.next
        return knot_data

    def Rget(self):
        if self.is_empty():
            return None
        knot_data = self.last.data
        self.last = self.last.pr
        self.size -= 1
        return knot_data


q = Queue()
print("Queue\n")
for i in range(10):
    q.put(i)
print(q.is_empty())
for i in range(10):
    print(q.get())
print(q.is_empty())

print("Stack\n")
s = Stack()

for i in range(10):
    s.push(i)
print(s.is_empty())
for i in range(10):
    print(s.pull())
print(s.is_empty())

d = Deque()

for i in range(10):
    d.Rput(i)
    d.Lput(i)
print(d.is_empty())
for i in range(10):
    print(d.Rget())
    print(d.Lget())
print(d.is_empty())