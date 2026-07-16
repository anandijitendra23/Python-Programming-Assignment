class Arithmetic : 

    def __init__(self):

        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first value : "))
        self.Value2 = int(input("Enter second value : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try :
            return self.Value1 /  self.Value2
        
        except ZeroDivisionError as zobj :
            print("Exception occured due to second operand is zero : ",zobj)
        return None
       
Obj1 = Arithmetic()
Obj2 = Arithmetic()

print("Enter Details of Object 1")
Obj1.Accept()
print("Addition is : ",Obj1.Addition())
print("Subtraction is : ",Obj1.Substraction())
print("Multiplication is : ",Obj1.Multiplication())
print("Division is : ",Obj1.Division())
print()

print("Enter Details of Object 2")
Obj2.Accept()
print("Addition is : ",Obj2.Addition())
print("Subtraction is : ",Obj2.Substraction())
print("Multiplication is : ",Obj2.Multiplication())
print("Division is : ",Obj2.Division())
