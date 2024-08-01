class Fib:          # Iterator
    def __init__(self, num) -> None:
        self.num = num
        # self.a, self.b = 0, 1
        # self.count = 0
        self.reset()

    def __iter__(self):
        # Reset the state of iteration to first data point
        # self.a, self.b = 0, 1
        # self.count = 0
        self.reset()
        return self

    def reset(self):
        self.a, self.b = 0, 1
        self.count = 0

    def __next__(self):
        if self.count < self.num:
            # Iterate to the next data point
            self.count += 1
            temp = self.a
            self.a, self.b = self.b, self.a + self.b
            return temp
        else:
            raise StopIteration


##############################

# it = Fib(10)
it = iter(Fib(10))
while True:
    try:
        print(next(it))
    except  StopIteration:
        break


