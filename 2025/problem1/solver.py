
class Solver:
    def __init__(self, text):
        self.nums = []
        self.signs = []
        self._ProcessText(text)

    def _ProcessText(self, text):
        for i in range(len(text)-1):
            self.nums.append(int(text[i].strip()))
        self.signs = list(text[-1].strip())

    def Solve1(self):
        sum = self.nums[0]
        for i in range(1, len(self.nums)):
            sum += self.nums[i] if (self.signs[i-1] == '+') else (-self.nums[i])
        return sum
    
    def Solve2(self):
        sum = self.nums[0]
        new_signs = list(reversed(self.signs))
        for i in range(1, len(self.nums)):
            sum += self.nums[i] if (new_signs[i-1] == '+') else (-self.nums[i])
        return sum
    
    def Solve3(self):
        sum = 10 * self.nums[0] + self.nums[1]
        new_signs = list(reversed(self.signs))
        for i in range(2, len(self.nums), 2):
            num = 10 * self.nums[i] + self.nums[i+1]
            sum += num if (new_signs[(i//2) - 1] == '+') else (-num)
        return sum
