from entries import *


if __name__ == "__main__":
    file = open("entries.txt", "w")

    # Jan
    file.write(Service(25000, date=datetime(2023, 1, 1)).toString())
    file.write(MiscExpense(1500, date=datetime(2023, 1, 3)).toString())
    file.write(Supplies(2000, date=datetime(2023, 1, 7)).toString())
    file.write(Service(30000, date=datetime(2023, 1, 12)).toString())
    file.write(Service(25000, date=datetime(2023, 1, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 1, 20)).toString())
    file.write(Service(10000, date=datetime(2023, 1, 17)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 1, 21)).toString())
    file.write(Rent(12000, date=datetime(2023, 1, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 1, 31)).toString())

    # Feb
    file.write(Service(21000, date=datetime(2023, 2, 1)).toString())
    file.write(SuppliesOnAccount1(190, date=datetime(2023, 2, 7)).toString())
    file.write(Service(15500, date=datetime(2023, 2, 12)).toString())
    file.write(Service(25000, date=datetime(2023, 2, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 2, 20)).toString())
    file.write(Service(12000, date=datetime(2023, 2, 22)).toString())
    file.write(SuppliesOnAccount2(190, date=datetime(2023, 2, 7)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 2, 21)).toString())
    file.write(Rent(10000, date=datetime(2023, 2, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 2, 28)).toString())

    # Mar
    file.write(Service(13000, date=datetime(2023, 3, 1)).toString())
    file.write(Supplies(2000, date=datetime(2023, 3, 7)).toString())
    file.write(Service(33000, date=datetime(2023, 3, 12)).toString())
    file.write(MiscExpense(3000, date=datetime(2023, 3, 3)).toString())
    file.write(Service(25000, date=datetime(2023, 3, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 3, 20)).toString())
    file.write(Equipment(5000, date=datetime(2023, 3, 17)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 3, 21)).toString())
    file.write(Rent(12000, date=datetime(2023, 3, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 3, 31)).toString())

    
    # Apr
    file.write(Service(21000, date=datetime(2023, 4, 1)).toString())
    file.write(Service(15500, date=datetime(2023, 4, 3)).toString())
    file.write(SuppliesOnAccount1(190, date=datetime(2023, 4, 5)).toString())
    file.write(Service(25000, date=datetime(2023, 4, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 4, 18)).toString())
    file.write(Service(12000, date=datetime(2023, 4, 20)).toString())
    file.write(SuppliesOnAccount2(190, date=datetime(2023, 4, 19)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 4, 21)).toString())
    file.write(Rent(10000, date=datetime(2023, 4, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 4, 28)).toString())

    # May
    file.write(SuppliesOnAccount1(2400, date=datetime(2023, 5, 7)).toString())
    file.write(Service(12000, date=datetime(2023, 5, 1)).toString())
    file.write(Service(15500, date=datetime(2023, 5, 12)).toString())
    file.write(Service(25000, date=datetime(2023, 5, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 5, 20)).toString())
    file.write(Service(12000, date=datetime(2023, 5, 22)).toString())
    file.write(SuppliesOnAccount2(2400, date=datetime(2023, 5, 7)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 5, 21)).toString())
    file.write(Rent(10000, date=datetime(2023, 5, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 5, 31)).toString())

    # June
    file.write(Service(19000, date=datetime(2023, 6, 1)).toString())
    file.write(Service(12200, date=datetime(2023, 6, 3)).toString())
    file.write(Supplies(350, date=datetime(2023, 6, 5)).toString())
    file.write(Service(25000, date=datetime(2023, 6, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 6, 18)).toString())
    file.write(Service(12000, date=datetime(2023, 6, 20)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 6, 21)).toString())
    file.write(Rent(10000, date=datetime(2023, 6, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 6, 30)).toString())

    # Jul
    file.write(Service(25000, date=datetime(2023, 7, 1)).toString())
    file.write(MiscExpense(1500, date=datetime(2023, 7, 3)).toString())
    file.write(Supplies(2000, date=datetime(2023, 7, 7)).toString())
    file.write(Service(30000, date=datetime(2023, 7, 12)).toString())
    file.write(Service(25000, date=datetime(2023, 7, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 7, 20)).toString())
    file.write(Service(10000, date=datetime(2023, 7, 17)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 7, 21)).toString())
    file.write(Rent(12000, date=datetime(2023, 7, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 7, 31)).toString())

    # Aug
    file.write(Service(21000, date=datetime(2023, 8, 1)).toString())
    file.write(SuppliesOnAccount1(190, date=datetime(2023, 8, 7)).toString())
    file.write(Service(15500, date=datetime(2023, 8, 12)).toString())
    file.write(Service(25000, date=datetime(2023, 8, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 8, 20)).toString())
    file.write(Service(12000, date=datetime(2023, 8, 22)).toString())
    file.write(SuppliesOnAccount2(190, date=datetime(2023, 8, 7)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 8, 21)).toString())
    file.write(Rent(10000, date=datetime(2023, 8, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 8, 31)).toString())

    # Sep
    file.write(Service(13000, date=datetime(2023, 9, 1)).toString())
    file.write(Supplies(2000, date=datetime(2023, 9, 7)).toString())
    file.write(Service(33000, date=datetime(2023, 9, 12)).toString())
    file.write(MiscExpense(3000, date=datetime(2023, 9, 3)).toString())
    file.write(Service(25000, date=datetime(2023, 9, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 9, 20)).toString())
    file.write(Equipment(5000, date=datetime(2023, 9, 17)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 9, 21)).toString())
    file.write(Rent(12000, date=datetime(2023, 9, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 9, 30)).toString())

    
    # Oct
    file.write(Service(21000, date=datetime(2023, 10, 1)).toString())
    file.write(Service(15500, date=datetime(2023, 10, 3)).toString())
    file.write(SuppliesOnAccount1(190, date=datetime(2023, 10, 5)).toString())
    file.write(Service(25000, date=datetime(2023, 10, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 10, 18)).toString())
    file.write(Service(12000, date=datetime(2023, 10, 20)).toString())
    file.write(SuppliesOnAccount2(190, date=datetime(2023, 10, 19)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 10, 21)).toString())
    file.write(Rent(10000, date=datetime(2023, 10, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 10, 31)).toString())

    # Nov
    file.write(SuppliesOnAccount1(2400, date=datetime(2023, 11, 7)).toString())
    file.write(Service(12000, date=datetime(2023, 11, 1)).toString())
    file.write(Service(15500, date=datetime(2023, 11, 12)).toString())
    file.write(Service(25000, date=datetime(2023, 11, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 11, 20)).toString())
    file.write(Service(12000, date=datetime(2023, 11, 22)).toString())
    file.write(SuppliesOnAccount2(2400, date=datetime(2023, 11, 7)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 11, 21)).toString())
    file.write(Rent(10000, date=datetime(2023, 11, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 11, 30)).toString())

    # Dec
    file.write(Service(19000, date=datetime(2023, 12, 1)).toString())
    file.write(Service(12200, date=datetime(2023, 12, 3)).toString())
    file.write(Supplies(350, date=datetime(2023, 12, 5)).toString())
    file.write(Service(25000, date=datetime(2023, 12, 14)).toString())
    file.write(ElectricityBill(5000, date=datetime(2023, 12, 18)).toString())
    file.write(Service(12000, date=datetime(2023, 12, 20)).toString())
    file.write(InternetBill(2000, date=datetime(2023, 12, 21)).toString())
    file.write(Rent(10000, date=datetime(2023, 12, 22)).toString())
    file.write(Salaries(7000, date=datetime(2023, 12, 31)).toString())