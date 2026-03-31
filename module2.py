class student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def showdata(self):
        print(self.name,self.roll)
a=student("sunipa",30,89)
a.showdata()
    
