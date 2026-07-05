Divisible_by_5 = lambda value : value % 5 == 0

def main():

    value = int(input("Enter a number : "))

    ret = Divisible_by_5(value)

    print(f"Is {value} divisiible by 5 : ",ret)

if __name__ == "__main__":
    main()