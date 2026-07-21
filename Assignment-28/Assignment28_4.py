def main():

    SourceFile = input("Enter the Source File(Existing File) Name : ")
    fobj1 = open(SourceFile, "r")

    NewFile = input("Enter the New File Name : ")
    fobj2 = open(NewFile, "w")

    for line in fobj1 :
        fobj2.write(line)

    fobj1.close()
    fobj2.close()

    print(f"Contents of {SourceFile} copied to {NewFile}.")

if __name__ == "__main__":
    main()