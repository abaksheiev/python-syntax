class Customer:
    def __init__(self, id, name,
                 bdno, bstreet, bcity, bcountry, bpin,
                 sdno, sstreet, scity, scountry, spin
                 ):
        self.custid = id
        self.name = name
        self.baddrd = self.Address(bdno, bstreet, bcity, bcountry, bpin)
        self.saddr = self.Address(sdno, sstreet, scity, scountry, spin)

    # nested class
    class Address:
        def __init__(self, dno, street, city,country, pin) :
            self.deno =dno
            self.ctreet = street
            self.city = city
            self.country = country
            self.pin = pin
        def display(self):
            print(f'{self.deno}, {self.ctreet},{self.city},{self.country},{self.pin}')
           
            
c = Customer(10,'John',
              101,'abc','delhi','India',10001,
              202,'jks', 'mumbay','India',20001)       
    
c.baddrd.display()

a = Customer.Address(302,'3jks', '3mumbay','3India',30001)

a.display()