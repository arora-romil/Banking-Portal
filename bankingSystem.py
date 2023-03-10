# Banking System using oops concept and SQLITE 3
import sqlite3
con = sqlite3.connect('bankCustomer.db')
c = con.cursor()

class Bank:
    def __init__(self, bank_name, bank_ifsc):
        self.bname = bank_name
        self.code = bank_ifsc
        print(f"====== Welcome to {self.bname} Bank ======")

    def detailsBank(self):
        print(
            f"Name of the bank: {self.bname}\nIFSC code of the bank:{self.code}")

class Customer:
    def __init__(self, uuid,name, age, pnum, accnum, upicode,balance):
        self.uuid = uuid
        self.name = name
        self.age = age
        self.number = pnum
        self.accountNum = accnum
        self.upi = upicode
        self.balance = balance
        self.passbookin = []
        self.passbookout = []

    def detailsCustomer(self):
        print(
            f"Name:{self.name}\nAge:{self.age}\nPhone Number:{self.number}\nAccount Number:{self.accountNum}")

    def add(self, cash):
        rid= self.uuid
        c.execute(f"""UPDATE customers SET balance = balance + {cash} 
                     WHERE rowid = {rid} """)
        c.execute(f"INSERT INTO inpassbook VALUES ({cash} WHERE rowid = {rid})")
        con.commit()
        print(f"Your account has been credited with {cash}Rs")

    def out(self, amount):
        rid = self.uuid
        c.execute("SELECT balance FROM customers")
        bal = c.fetchall()[rid-1][0]
        if amount > bal:
            print(
                "OPPS!! You do not have sufficient balance to withdraw money from your account.")
        else:
            c.execute(f"""UPDATE customers SET balance = balance - {amount} 
                        WHERE rowid = {rid} """)
            c.execute(f"INSERT INTO outpassbook VALUES ({amount})")
            con.commit()
            print(f"Your account has been debited with {amount}Rs")

    def checkBalance(self):
        rid  = self.uuid
        c.execute("SELECT balance FROM customers")
        # print("THE BALANCE Is Rs",c.fetchall()[0][0])
        print(f"Your Account Balance is {c.fetchall()[rid-1][0]}Rs")

    def passbook(self):
        rid  = self.uuid
        c.execute(f"SELECT rowid,* FROM inpassbook")
        items = c.fetchall()
        print("YOUR IN ENTRY:")
        for item in items:
            print(item)
        c.execute("SELECT rowid,* FROM outpassbook")
        items = c.fetchall()
        print("YOUR OUT ENTRY:")
        for item in items:
            print(item)



def helpupi(ver, upil):
    for i, upi in enumerate(upil):
        if ver == upi:
            return i


if __name__ == "__main__":
    SBI = Bank("SBI", 24862)
    # HDFC = Bank("HDFC", 16200)
    c.execute("SELECT rowid,* FROM customers")
    items = c.fetchall()
# for item in items:
    Romil = Customer(items[0][0],items[0][1],items[0][2],items[0][3],items[0][4],items[0][5],items[0][6])
    Harsh = Customer(items[1][0],items[1][1],items[1][2],items[1][3],items[1][4],items[1][5],items[1][6])
    Asmit = Customer(items[2][0],items[2][1],items[2][2],items[2][3],items[2][4],items[2][5],items[2][6])
    Rishabh = Customer(items[3][0],items[3][1],items[3][2],items[3][3],items[3][4],items[3][5],items[3][6])
    custList = [Romil, Harsh, Asmit, Rishabh]
    upiList = [x.upi for x in custList]
    name = input("Enter your name: ")
    j = 0
    while j <3:   
        verify = int(input("Enter your UPI to verify: "))
        i = helpupi(verify, upiList)
        if verify in upiList:
            while (True):
                welcomeMsg = '''\nPlease choose an option:
    1. Debit Money from your account
    2. Add Money to your account
    3. Check your account balance
    4. Print your passbook ***(This is not working currently We are working on this feature)***
    5. Details of your account
    6. Details of your bank
    7. Exit the bank
            '''
                print(welcomeMsg)
                query = int(input("Enter your choice: "))
                if query == 1:
                    custList[i].out(
                        int(input("Enter the amount you want to withdraw from your account: ")))
                elif query == 2:
                    custList[i].add(
                        int(input("Enter the amount you want to add to your account: ")))
                elif query == 3:
                    custList[i].checkBalance()
                elif query == 4:
                    custList[i].passbook()
                elif query == 5:
                    custList[i].detailsCustomer()
                elif query == 6:
                    SBI.detailsBank()
                elif query == 7:
                    print("Thank you for using our banking portal")
                    con.commit()
                    con.close()
                    j = 3
                    break

        else:
            j+=1
            if j == 3:
                print("You have entered incorrect UPI ID 3 times, you account has been blocked,contact your bank for further details!")
            else:
                print("You have entered wrong UPI ID")
