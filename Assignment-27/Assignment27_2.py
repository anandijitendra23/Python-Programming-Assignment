class BankAccount :
    ROI = 10.5

    def __init__(self,Name ,Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder : ",self.Name)
        print("Baalance : ",self.Amount)

    def Deposit(self):
        amt = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + amt
        print("Amount deposited successfully.")

    def Withdraw(self):
        amt = float(input("Enter amount to withdraw : "))

        if self.Amount >= amt :
            self.Amount = self.Amount - amt
            print("Withdrawal Successful. ")

        else:
            print("Insufficient Balance.")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest
    
def main():
    Obj1 = BankAccount("Amit",100000)
    Obj2 = BankAccount("Raj",50000)

    print("--------Account-1---------")
    Obj1.Display()
    Obj1.Deposit()
    Obj1.Withdraw()
    print("Interest = ",Obj1.CalculateInterest())
    Obj1.Display()

    print()

    print("--------Account-2---------")
    Obj2.Display()
    Obj2.Deposit()
    Obj2.Withdraw()
    print("Interest = ",Obj2.CalculateInterest())
    Obj2.Display()

if __name__ == "__main__":
    main()

        


