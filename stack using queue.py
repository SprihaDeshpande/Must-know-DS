# Create a blue print for queue
class queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        val = self.queue[0]
        self.queue = self.queue[1:]
        return val

    def __len__(self):
        return len(self.queue)


# The type of data structure we need to implement
class stack:

    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()

    def push1(self, val):
        self.q1.enqueue(val)

'''making this function an expensive one to pop elements, we enqueue values in q2 untill we do not have any elements in q1 along with simultaneously dequeueing the same.
    enqueue back all elements in q1 and till we are left with only one element in q2
    return the last element in q2
    
    If array is empty, return immediately indicating no values present.
'''
    def pop1(self):
        if len(self.q1) == 0:
            return "No values"

        while len(self.q1)>0:
            self.q2.enqueue(self.q1.dequeue())

        while len(self.q2)>1:
            self.q1.enqueue(self.q2.dequeue())

        return self.q2.dequeue()


#driver code

obj = stack()
obj.push1(1)
obj.push1(2)
obj.push1(3)
print(obj.pop1())
print(obj.pop1())
print(obj.pop1())
val = obj.pop1()
print(val)



