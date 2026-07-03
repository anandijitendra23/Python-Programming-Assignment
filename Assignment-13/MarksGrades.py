def Grades(marks):

    if marks >= 75:
        return "Distinction"
    elif marks >= 60:
        return "First Class"
    elif marks >= 50:
        return "Second Class"
    else:
        return "Fail"

def main():
    
    m = int(input("Enter marks : "))

    ret = Grades(m)
    print("Grades = ",ret)


if __name__ == "__main__":
    main()