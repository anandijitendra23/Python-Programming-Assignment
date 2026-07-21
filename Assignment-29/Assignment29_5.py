def main():

    FileName = input("Enter File Name : ")
    string = input("Enter the string : ")

    fobj = open(FileName , "r")

    count = 0

    for lines in fobj:
            count = count + lines.count(string)        #built in count string method

    fobj.close()

    print("The frequency of the string is : ",count)


if __name__ =="__main__":
    main()