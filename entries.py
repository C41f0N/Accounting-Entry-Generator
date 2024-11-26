from datetime import datetime

class Service:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tCash\t{self.amount}\t0\n\tService Revenue\t0\t{self.amount}\n\t(Performed Services for {self.amount})\n\n"

class Supplies:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tSupplies\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Bought Supplies for {self.amount})\n\n"


class ServiceCredit1:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tAccounts Reveivable\t{self.amount}\t0\n\tService Revenue\t0\t{self.amount}\n\t(Performed Services on Credit)\n\n"


class ServiceCredit2:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tCash\t{self.amount}\t0\n\tAccounts Reveivable\t0\t{self.amount}\n\t(Recieved Money for Services performed)\n\n"


class ElectricityBill:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tUtilities Expense\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Paid the electricity bill)\n\n"

class InternetBill:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tUtilities Expense\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Paid the internet bill)\n\n"

class Rent:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tRent Expense\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Paid the shop rent)\n\n"

class Equipment:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tEquipment\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Paid the shop rent.)\n\n"

class ServiceAdvance1:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date


    def toString(self):
        return f"{self.date.month}-{self.date.day}\tCash\t{self.amount}\t0\n\tUnearned Revenue\t0\t{self.amount}\n\t(Performed Services on Credit)\n\n"


class ServiceAdvance2:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date

    def toString(self):
        return f"{self.date.month}-{self.date.day}\tUnearned Revenue\t{self.amount}\t0\n\tService Revenue\t0\t{self.amount}\n\t(Performed Services on Credit)\n\n"


class MiscExpense:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date

    def toString(self):
        return f"{self.date.month}-{self.date.day}\tMiscellaneous Expense\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Paid {self.amount} for misc. expenses)\n\n"


class Salaries:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date

    def toString(self):
        return f"{self.date.month}-{self.date.day}\tSalaries Expense\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Paid salaries to employees)\n\n"

class SuppliesOnAccount1:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date

    def toString(self):
        return f"{self.date.month}-{self.date.day}\tSupplies\t{self.amount}\t0\n\tAccounts Payable\t0\t{self.amount}\n\t(Bought {self.amount} worth of supplies on account.)\n\n"

class SuppliesOnAccount2:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date

    def toString(self):
        return f"{self.date.month}-{self.date.day}\tAccounts Payable\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Payed for {self.amount} worth of supplies purchased earlier.)\n\n"

class Equipment:
    def __init__(self, amount:int, date:datetime):
        self.amount = amount
        self.date = date

    def toString(self):
        return f"{self.date.month}-{self.date.day}\tEquipment\t{self.amount}\t0\n\tCash\t0\t{self.amount}\n\t(Bought Equipment worth {self.amount}.)\n\n"
