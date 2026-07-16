class Demo :

    value = 10

    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B
        
    def Fun(self):
        print("Inside Fun")
        print("No1 = ",self.No1)
        print("No2 = ",self.No2)

    def Gun(self):
        print("Inside Gun")
        print("No1 = ",self.No1)
        print("No2 = ",self.No2)
    
Obj1 = Demo (11,21)
Obj2 = Demo (51,101) 

Obj1.Fun()
Obj2.Fun()
Obj1.Gun()
Obj2.Gun()

        