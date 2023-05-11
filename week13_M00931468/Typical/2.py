import datetime

class Account:
    def __init__(self, id, balance,date_created, annual_interest_rate = 0):
        self.__id = id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate
        self.__date_created = date_created

    # Getters

    def get_id(self):
        return self.__id
    
    def get_balance(self):
        return self.__balance
    
    def get_annual_interest_rate(self):
        return self.__annual_interest_rate
    
    def get_date_created(self):
        return self.__date_created
    
    def get_monthly_interest_rate(self):
        monthly_interest_rate = self.__annual_interest_rate / 12
        return monthly_interest_rate
    
    def get_monthly_interest(self):
        monthly_interest = (self.get_monthly_interest_rate()/100) * self.__balance
        return round(monthly_interest,2)
    
    # Setters

    def set_id(self, new_id):
        self.__id = new_id
    
    def set_balance(self, new_balance):
        self.__balance = new_balance

    def set_balance(self, date_created):
        self.__date_created = date_created
    
    def set_annual_interest_rate(self, new_annual_interest_rate):
        self.__annual_interest_rate = new_annual_interest_rate
        

    # Methods

    def withdraw(self, withdraw_amount : int):
        self.__balance -= withdraw_amount
        return f"You currently have ${self.__balance} in your account, after your withodrawal of ${withdraw_amount}"   
    
    def deposit(self, deposit):
        self.__balance += deposit
        return f"You currently have ${self.__balance} to your account, after your deposit of ${deposit}"    

    def __str__(self) -> str:
        return f"Balance: ${self.__balance} \nMonthly Interest: ${self.get_monthly_interest()} \nDate created:{self.__date_created}"

if __name__ == "__main__":
    
    account1 = Account(1122,20000,datetime.date.today(),4.5)
    print(account1.withdraw(2500))
    print(account1.deposit(3000))
    print(account1)
 