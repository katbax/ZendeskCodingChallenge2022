import requests, os
from requests import auth

class Ticket:

    def __init__(self, email, api_token, subdomain):
       self.email = email
       self.subdomain = subdomain
       self.ticketurl = 'https://' + self.subdomain + '.zendesk.com/api/v2/tickets.json'
       self.pageurl = 'https://' + self.subdomain + '.zendesk.com/api/v2/tickets.json?page[size]=25'
       self.api_token = api_token

    def greeting(self):
        greeting = "\n\tWELCOME TO THE TICKET VIEWER!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        print(greeting)

    def startMenu(self):
        on = True
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
            break
    def showMenu(self):
        on = True
        while on:
            x = input("\nTo view all tickets, type 1 \nTo view a single ticket, type 2 \nTo exit, type 3\n")
            if x == "1": 
                self.showAllTickets() 
            elif x == "2": 
                y = input('\nEnter the number of the ticket you would like to view: \n')
                self.showSingleTicket(y)
            elif x == '3':
                print('\nThank you for using the ticket viewer. Goodbye!\n')
                break
            else:
                print('\nInvalid selection. \n')
                x = input("To view all tickets, type 1 \nTo view a single ticket, type 2 \n")
            break

    def getTickets(self, url = None):
        if url == None:
            url = self.pageurl
        headers = {
            'Content-Type': 'application/json',
        }
        try:
            response = requests.get(url, auth=(self.email + '/token', self.api_token))
        except requests.exceptions.RequestException as e:  
            raise SystemExit(e)
        return response.json()

    def showAllTickets(self):
        jsonTickets,jsonLinks,jsonMeta,prev,next,has_more = self.switchPage()
        lastID = ""
        while has_more:
            for i in range(len(jsonTickets)):
                print(str(jsonTickets[i]['id']) + ". " + jsonTickets[i]['subject'])
                lastID = jsonTickets[i]['id']
                if i == (len(jsonTickets) - 1):
                    if lastID >= 26 and lastID < self.getTicketsCount() - 1:
                        x = input('\n\nTo view next page, type 1.\nTo view previous page, type 2\nTo view the main menu, type 3\n')
                    elif lastID < 26:
                        x = input('\n\nTo view next page, type 1.\nTo view the main menu, type 3\n')
                    elif lastID == self.getTicketsCount():
                        x = input('\n\nTo view prev page, type 2.\nTo view the main menu, type 3\n')
                    if x == '1':
                        jsonTickets,jsonLinks,jsonMeta,prev,next,has_more = self.switchPage(next)
                    elif x == '2':
                        jsonTickets,jsonLinks,jsonMeta,prev,next,has_more = self.switchPage(prev)
                    elif x == '3':
                        self.showMenu()
                        has_more = False
                        break
                    else:
                        print('\nInvalid selection. \n')
                        x = input('\n\nTo view next page, type 1.\nTo view previous page, type 2\nTo view the main menu, type 3\n\n')        
            
    def switchPage(self, url = None):
        if url == None:
            url = self.pageurl
        jsonTickets = self.getTickets(url)
        jsonLinks = jsonTickets['links']
        jsonMeta = jsonTickets['meta']
        jsonTickets = jsonTickets['tickets']
        prev = jsonLinks['prev']
        next = jsonLinks['next']
        has_more = jsonMeta['has_more']
        return jsonTickets,jsonLinks,jsonMeta,prev,next,has_more



    def showSingleTicket(self, ticket):
        jsonTickets = self.getTickets(self.ticketurl)
        jsonTickets = jsonTickets['tickets']
        ticket = int(ticket) - 1
        self.printTicket(jsonTickets[ticket])

    def printTicket(self, ticket):
        print("\nSubject: " + ticket['subject'] + " \n")
        print("Created At: " + ticket['created_at'] + " \n")
        print("Updated At: " + ticket['updated_at'] + " \n")
        print("Description: " + ticket['description'] + " \n")

    def getTicketsCount(self):
        jsonTickets = self.getTickets(self.ticketurl)
        return len(jsonTickets['tickets'])
    

obj = Ticket('email@email.com','token', 'subdomain')
obj.greeting()
obj.startMenu()






