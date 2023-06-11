class Stack():
    # TODO: create a new empty stack
    def __init__(self, size):
        self.STACK_SIZE = size
        self.stack = []

    # TODO: push items onto the stack
    def push(self, item):
        if len(self.stack) >= self.STACK_SIZE:
            print(f'Stack is full, data {item} not added')
        else:
            self.stack.append(item)

    # TODO: check is stack isEmpty
    def is_empty(self):
        return len(self.stack) == 0
    
    # TODO: reverse the stack
    def reverse(self):
        word = "".join(self.stack)
        
        for index in range(0, len(self.stack)):
            print(self.stack[index])


    # TODO: pop an item in the stack
    def _pop(self):
        if self.is_empty():
            print('The stack is empty')
        else:
            p = self.stack.pop()
            print( p)

    # TODO: print the stack content
    def __str__(self):
        s = ''
        for i in range(len(self.stack) - 1, -1, -1):
            s = s + self.stack[i] +'\n'
        return s
    
# TODO: create stack of 4
stack =  Stack(4)
stack.push("a")
stack.push("m")
stack.push("o")
stack.push("r")
print(stack.__str__())

stack.reverse()

