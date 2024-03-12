class Stack:
    def __init__(self, size):
        self.size = size
        self.S_I = []

    def is_empty(self):
        return len(self.S_I) == 0

    def display(self):
        print(self.S_I)

    def is_full(self):
        return len(self.S_I) == self.size

    def push(self, I):
        if not self.is_full():
            self.S_I = self.S_I + [I]
        else:
            print("Stack is full")

    def pop(self):
        if not self.is_empty():
            data = self.S_I[-1]
            del self.S_I[-1]
            return data
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            print('peek is:', self.S_I[-1])
            return self.S_I[-1]
        else:
            print("Stack is empty")

    def get_size(self):
        return len(self.S_I)

    def pop_n(self,n): #n개만큼 pop
        pop_n1 =[]
        for i in range(n):
            if not self.is_empty():
                data = self.S_I[-1]
                del self.S_I[-1]
                pop_n1 = pop_n1 + [data]
            else:
                print(f'Stack is empty: {i+1}th pop failed')
        return pop_n1




stack_ex = Stack(7)

stack_ex.display()
print(stack_ex.is_empty())
stack_ex.pop()
stack_ex.push(1)
stack_ex.display()
print(stack_ex.is_empty())
print(stack_ex.is_full())
stack_ex.push(2)
stack_ex.push(3)
stack_ex.push(4)
stack_ex.push(5)
stack_ex.push(6)
stack_ex.push(7)
stack_ex.display() #[1, 2, 3, 4, 5, 6, 7]
print(stack_ex.peek()) #peek is: 7
print(stack_ex.is_full())
stack_ex.push(6) #Stack is full
stack_ex.display()
stack_ex.pop_n(3) #[1, 2, 3, 4]
stack_ex.display()
stack_ex.pop_n(5) #Stack is empty: 5th pop failed
stack_ex.display()
