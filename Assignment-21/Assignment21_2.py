import threading

def Maximum(numbers):
    max_ele = max(numbers)
    print("Maximum Element from the list is : ",max_ele)

def Minimum(numbers):
    min_ele = min(numbers)
    print("Minimum Element from the list is : ",min_ele)


def main():

    numbers = list()

    n = int(input("Enter number of elements : "))
    for i in range(n):
        n = int(input("Enter element : "))
        numbers.append(n)

    t1 = threading.Thread(target = Maximum , args = (numbers ,))
    t2 = threading.Thread(target = Minimum , args = (numbers ,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from Main ")

if __name__ == "__main__":
    main()