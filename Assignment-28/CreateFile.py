def main():
    try:
        fobj = open("Demo.txt","w")                 
        print("File gets opened")

        fobj.write("Marvellous Infosystems\n")
        fobj.write("Jay Ganesh ...\n")
        fobj.write("Python Programming\n")
        fobj.write("Welcome to Python")

        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present in current directory")

if __name__ == "__main__":
    main()
