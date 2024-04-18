class bank_acc:
    branch_name = "ICICI"
    branch = "blr"
    IFSC = "ICICI001124"

    def __init__(self,acc_name,acc_num,acc_bal):

        self.acc_name = acc_name
        self.acc_num = acc_num
        self.acc_bal = acc_bal

    def acc_info(self):
        print(f"""Name :{self.acc_name} 
Account Number : {self.acc_num}
Balance : {self.acc_bal}
Branch name : {self.branch_name}
Address : {self.branch}
IFSC : {self.IFSC}""")
        
obj = bank_acc("sid","123456798","2500")
obj.acc_info()
print()
obj1 =bank_acc("abc","987654321","40000")
obj1.acc_info()