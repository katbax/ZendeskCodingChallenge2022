import requests, json
from requests import auth

class Ticket:

    def showMenu(self):
        while 1:
            x = input("To view all tickets, type 1 \nTo view a single ticket, type 2 \n")
            if x == "1": 
                print(1) 
                break
            if x == "2": 
                print(2)
                break

    def getTickets(self,email,password):
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get('https://zccintern2021.zendesk.com/api/v2/tickets.json', headers=headers, auth=(email,password))
        return response.json()

    def showAllTickets(self,email,password):
        jsonTickets = self.getTickets(email,password)
        jsonTickets = jsonTickets['tickets']
        for i in range(25):
            print(str(i+1) + "." + jsonTickets[i]['subject'])




    def showSingleTicket(self,email,password):
        jsonTickets = self.getTickets(email,password)
        jsonTickets = jsonTickets["tickets"]
        print(jsonTickets[0]['subject'])

obj = Ticket()
print("\tWELCOME TO THE TICKET VIEWER!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
menu = ""
email = 'example@email.com'
password = 'password'
obj.showAllTickets(email,password)
obj.showSingleTicket(email,password)


