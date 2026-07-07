from Arithmetic import *

def main():

    Value1 = int(input("Enter first Number : "))
    Value2 = int(input("Enter second Number : "))

    ret = Add(Value1 , Value2)
    print(f"Addition : {Value1} + {Value2} = ",ret)

    ret = Sub(Value1 , Value2)
    print(f"Subtraction : {Value1} - {Value2} = ",ret)

    ret = Mult(Value1 , Value2)
    print(f"Multiplication : {Value1} * {Value2} = ",ret)

    ret = Div(Value1 , Value2)
    print(f"Division : {Value1} / {Value2} = ",ret)

if __name__ == "__main__":
    main()




