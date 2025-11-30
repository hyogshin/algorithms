class ExamRoom:

    def __init__(self, n: int):
        self.n = n
        self.occupied = []

    def seat(self) -> int:
        if not self.occupied:
            self.occupied.append(0)
            return 0
        
        max_dist = self.occupied[0]
        pos = 0
        # in between
        for i in range(len(self.occupied) - 1):
            a = self.occupied[i]
            b = self.occupied[i+1]
            d = (b - a) // 2
            if d > max_dist:
                max_dist = d
                pos = a + d

        
        # last bit
        if self.n - 1 - self.occupied[-1] > max_dist:
            max_dist = self.n - 1 - self.occupied[-1]
            pos = self.n - 1
        
        bisect.insort(self.occupied, pos)
        
        return pos
        

    def leave(self, p: int) -> None:
        self.occupied.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)