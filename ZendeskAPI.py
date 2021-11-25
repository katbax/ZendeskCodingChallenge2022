import requests, json
from requests import auth

class Ticket:

    email = 'email'
    password = 'password'

    def showMenu(self):
        on = True
        while on:
            x = input("\nTo view all tickets, type 1 \nTo view a single ticket, type 2 \nTo view the main menu, enter 3\n")
            if x == "1": 
                self.showAllTickets() 
            elif x == "2": 
                y = input('\nEnter the number of the ticket you would like to view: \n')
                self.showSingleTicket(y)
            elif x == '3':
                break
            else:
                print('\nInvalid selection. \n')
                x = input("To view all tickets, type 1 \nTo view a single ticket, type 2 \n")

    def getTickets(self, url = 'https://zccintern2021.zendesk.com/api/v2/tickets.json?page[size]=25'):
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(url, headers=headers, auth=(self.email,self.password))
        return response.json()

    def showAllTickets(self):
        jsonTickets = self.getTickets()
        jsonLinks = jsonTickets['links']
        jsonMeta = jsonTickets['meta']
        jsonTickets = jsonTickets['tickets']
        prev = jsonLinks['prev']
        next = jsonLinks['next']
        has_more = jsonMeta['has_more']
        while has_more:
            for i in range(len(jsonTickets)):
                print(str(jsonTickets[i]['id']) + ". " + jsonTickets[i]['subject'])
                if i == (len(jsonTickets) - 1):
                    x = input('\n\nTo view next page, type 1.\nTo view previous page, type 2\nTo view the main menu, type 3\n')
                    if x == '1':
                        jsonTickets,jsonLinks,jsonMeta,prev,next,has_more = self.switchPage(next)
                    elif x == '2':
                        jsonTickets,jsonLinks,jsonMeta,prev,next,has_more = self.switchPage(prev)
                    elif x == '3':
                        self.showMenu()
                        break
                    else:
                        print('\nInvalid selection. \n')
                        x = input('\n\nTo view next page, type 1.\nTo view previous page, type 2\nTo view the main menu, tyoe 3\n\n')



            
            
    def switchPage(self, url):
        jsonTickets = self.getTickets(url)
        jsonLinks = jsonTickets['links']
        jsonMeta = jsonTickets['meta']
        jsonTickets = jsonTickets['tickets']
        prev = jsonLinks['prev']
        next = jsonLinks['next']
        has_more = jsonMeta['has_more']
        return jsonTickets,jsonLinks,jsonMeta,prev,next,has_more



    def showSingleTicket(self, ticket):
        jsonTickets = self.getTickets()
        jsonTickets = jsonTickets['tickets']
        ticket = int(ticket) - 1
        self.printTicket(jsonTickets[ticket])

    def printTicket(self, ticket):
        print("\nSubject: " + ticket['subject'] + " \n")
        print("Created At: " + ticket['created_at'] + " \n")
        print("Updated At: " + ticket['updated_at'] + " \n")
        print("Description: " + ticket['description'] + " \n")
    

obj = Ticket()
menu = ""
greeting = "\n\tWELCOME TO THE TICKET VIEWER!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
on = True
print(greeting)
while on:
    x = input('\nTo view the menu, type 1\nTo quit, type 2\n')
    if x == '1':
        obj.showMenu()
    elif x == '2':
        print('\nThank you for using the ticket viewer. Goodbye!\n')
        on = False
    else:
        print('\nInvalid selection. \n')
        x = input("To view all tickets, type 1 \nTo view a single ticket, type 2 \n")




