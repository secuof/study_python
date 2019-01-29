class fourcal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def sub(self):
        result = self.first / self.second
        return result
a = fourcal()
b = fourcal()
inputa = int(input())
inputb = int(input())
a.setdata(inputa, inputb)
sum = a.sum()
mul = a.mul()
div = a.div()
sub = a.sub()
print ("SUM:", sum)
print ("Multiplication:",mul)
print ("Division:",div)
print ("Subtraction:",sub)