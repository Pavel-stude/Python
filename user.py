class User:

    def __init__(self, firstname):
        self.first_name = firstname
        print (firstname)

    def sayLastname (self, lastname):
        self.last_name = lastname
        print (lastname)
    
    def sayName (self):
        print (self.first_name, self.last_name)
