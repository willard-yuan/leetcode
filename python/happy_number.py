class Solution:    # @param {integer} n    # @return {boolean}    def __init__(self):        pass    def addSum(self, num):        sum1 = 0        for i, bit in enumerate(str(num)):            sum1 += int(bit) * int(bit)        return sum1    def isHappy(self, n):        sums = []        Tmp = self.addSum(n)        if Tmp == 1:            return True        else:            sums.append(Tmp)        Tmp = self.addSum(Tmp)		#while bool(Tmp != 1) & bool(Tmp not in sums):        while (Tmp != 1) & (Tmp not in sums):            sums.append(Tmp)            Tmp = self.addSum(Tmp)        if Tmp == 1:            return True        else:            return Falseif __name__ == '__main__':    n = 24    solver = Solution()    boolTmp = solver.isHappy(n)    print boolTmp