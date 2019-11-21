class stack:

    def __init__(self):
        self.stack = []

    def push_element(self, val):
        self.stack.append(val)

    def get_element(self):
        val = self.stack[-1]
        self.stack = self.stack[:-1]

        return val

    def __len__(self):
        return len(self.stack)

class queue:

    def __init__(self):
        self.q1 = stack()
        self.q2 = stack()

    def enqueue(self, val):
        self.q1.push_element(val)

'''
We make this function for dequeue an expensive function by having all elements pushed in q2 while we pop up the elements in q1 unless q1 is empty
we then use a loop to push these back to q1 until there is only one element in stack q2 

we then further return the last value in q2. For no elements in our queue, the base condition will return an immediate string.
'''
    def dequeue(self):

        if len(self.q1) == 0:
            return "No Elements"

        while len(self.q1)>0:
            self.q2.push_element(self.q1.get_element())

        while len(self.q2)>1:
            self.q1.push_element(self.q2.get_element())

        return self.q2.get_element()

#driver code

obj = queue()
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)

print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
print(obj.dequeue())
