class MinStack:
    def __init__(self):
        self.s = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.s.append(val)
        self.min = min(self.min, val)

    def pop(self) -> None:
        last = self.s.pop()
        if last == self.min:
            temp = float('inf')
            for i in self.s:
                temp = min(temp, i)
            self.min = temp
    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.min