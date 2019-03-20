class Bilangan():
    def __init__(self,a=4,b=6):
        self.real=a
        self.im=b
    def display(self):
         #print (self.real, '+', self.im, 'i')
         temp=str(self.real)+'+'+str(self.im)+'i'
         return temp
    def __str__(self):
        return str(self.real)+'+'+str(self.im)+'i'
    def addNum (self, num1, num2):
        self.real=num1.real+num2.real
        self.im=num1.im+num2.im
    def addKompleks(self,obj):
        a=salf.real+obj.real
        b=salf.im+obj.im
        return Bilangan(a,b)
    def __ add__