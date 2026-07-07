def DisplayEven(no , cnt) : 
     
     while cnt < 10:
        print(no ,end = "   ")
        no = no + 2
        cnt = cnt + 1

     return no
    

def main():
     num = 2
     count = 0

     ret = DisplayEven(num , count)
    


if __name__ == "__main__":
    main()