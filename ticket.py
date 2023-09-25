import re

class TickerGenerator:
    def __init__(self,name,phone):
        self.name = name
        self.phone = str(phone)
        self.destination = input('Enter your destination:')

    def checkValidName(self):
        while re.search('\W',self.name,re.IGNORECASE):
            self.name = input('!!!------- Ivalid name --------!!!\nEnter new one:')

    def validDestination(self):
        valid_destination = ['chennai','mumbai','delhi','hydrabad','pune','jaipur','banglore','kerala']
        while self.destination.lower() not in valid_destination:
            self.destination = input('!!!------- Ivalid Destination --------!!!\nEnter valid destination:')

    def validPhoneNumber(self):
        pass

    def ticketPrice(self):
        price = '0'
        valid_destination = ['chennai','mumbai','delhi','hydrabad','pune','jaipur','banglore','kerala']
        for count,val in enumerate(valid_destination):
            if self.destination == val:
                if count <= 3:
                    price = 'Rupeess 10'
                if count>3 and count <= 5:
                    price = 'Rupeess 20'
                else:
                    price = 'Rupeess 30'
        return price

    def genTicket(self):
        ticket_id = self.destination[:3]+"-"+self.name[:3]+self.phone[-4:]
        return ticket_id

def getDetials():
    name = input('Enter your name:')
    phone = int(input('Enter your phone number:'))  
    ticket = TickerGenerator(name,phone)
    ticket.checkValidName()
    ticket.validDestination()
    ticket_id = ticket.genTicket()
    price = ticket.ticketPrice()
    print(price,'----')
    print(ticket_id.title())
getDetials()
     



