CheckLength = lambda str : len(str) > 5

def main():

    n = int(input("Enter number of elements : "))

    string_list = list()

    for i in range(n):
        str = (input("Enter a string : "))
        string_list.append(str)

    FData = list(filter(CheckLength , string_list))
    print("List of Odd Numbers is : ",FData)


if __name__ == "__main__":
    main()