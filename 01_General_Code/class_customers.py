class Customers:
    __CustomerID = ""
    __ContactName = ""
    __Address = ""
    __City = ""
    __Country = ""

    def __init__(self, CustomerID, ContactName, Address, City, Country):
        self.CustomerID = CustomerID
        self.CustomerName = ContactName
        self.Address = Address
        self.City = City
        self.Country = Country

    def set_CustomerID(self, CustomerID):  # class setters or accessor
        self.__CustomerID = CustomerID

    def get_CustomerID(self):  # class getter or mutators
        return self.CustomerID
    
    def set_CustomerName(self, CustomerName):
        self.__ContactName = CustomerName
            
    def get_CustomerName(self, CustomerName):
        return self.ContactName

    def set_Address(self, Address):
        self.__Address = Address

    def get_Address(self, Address):
        return self.Address

    def set_City(self, City):
        self.__ContactName = CustomerName

    def get_City(self, City):
        return self.City
    
    def set_Country(self, Country):
        self.__Country = Country

    def get_Country(self, Country):
        return self.Country
    
    def toString(self):
        return ("{} with ID {} with a contact name {} stay in the city of {} and in the country {}".format(self.CustomerID, self.CustomerName, self.Address, self.City, self.Country))

customer_one = Customers('1', 'jide', '12,ibrahim onashokun street', 'lagos', 'Nigeria')
customer_one.toString()
print(customer_one.toString())
customer_one = Customers('1', 'mary', '15,ibrahim onashokun street', 'lagos', 'Nigeria')
customer_one.toString()
print(customer_one.toString())
print(Customers)






    


    