import threading

def EvenFactor(no):
    even_sum = 0

    print("Even Factors : ")
    for i in range(1 , no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i,end = "   ")
            even_sum = even_sum + i
    print() 
    
    print(f"Sum of Even Factors of {no} is : ",even_sum)

def OddFactor(no):
    odd_sum = 0

    print("Odd Factors : ")
    for i in range(1 , no + 1):
        if no % i == 0 and i % 2 == 1:
            print(i,end = "   ")
            odd_sum = odd_sum + i
    print()
    
    print(f"Sum of Odd Factors of {no} is : ",odd_sum)



def main():

    value = int(input("Enter a number : "))

    t1 = threading.Thread(target = EvenFactor, args = (value , ))
    t2 = threading.Thread(target = OddFactor , args = (value , ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    print("Exit from Main")

if __name__ == "__main__":
    main()
