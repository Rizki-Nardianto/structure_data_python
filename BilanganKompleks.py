class BilanganKompleks:
    def __init__(self,a=4,b=6):
        self.real=a
        self.im=b
    def display(self):
         #print (self.real, '+', self.im, 'i')
         temp=str(self.real)+'+'+str(self.im)+'i'
         return temp
    def __str__(self):
        return str(self.real)+'+'+str(self.im)+'i'