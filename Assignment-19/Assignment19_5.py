from functools import reduce

def ChkPrime(no):
    if no <= 1:
        return False
    
    for i in range(2,no):
        if no % i  == 0:
            return False
    
    return True

def Filter(no):
    return ChkPrime(no)

def Map(no):
    return no * 2

def Reduce(no1 , no2):
    if no1 > no2:
        return no1
    else:
        return no2
    
def main():

    num_list = list()

    n = int(input("Enter number of elements : "))

    for i in range(n):
        no = int(input("Enter element : "))
        num_list.append(no)

    FData = list(filter(Filter , num_list))
    print("List after Filter : ",FData)

    MData = list(map(Map , FData))
    print("List after Map : ",MData)

    RData = reduce(Reduce , MData)
    print("Reduce : Maximum number is = ",RData)

    

if __name__ == "__main__":
    main()