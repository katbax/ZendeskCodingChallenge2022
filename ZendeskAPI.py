from dotenv import load_dotenv   
load_dotenv('keys.env')
import requests, os
from requests import auth

class Ticket:

    def __init__(self, email, api_token, subdomain):
       self.email = email
       self.api_token = api_token
       self.subdomain = subdomain
       self.ticketurl = 'https://' + self.subdomain + '.zendesk.com/api/v2/tickets.json'
       self.pageurl = 'https://' + self.subdomain + '.zendesk.com/api/v2/tickets.json?page[size]=25'
       


    def greeting(self):
        greeting = "\n\tWELCOME TO THE TICKET VIEWER!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
        print(greeting)


    def startMenu(self):
        on = True
        while on:
            startMenuChoice = input('\nTo view the menu, type 1\nTo quit, type 2\n')
            if startMenuChoice == '1':
                obj.showMenu()
            elif startMenuChoice == '2':
                print('\nThank you for using the ticket viewer. Goodbye!\n')
                on = False
            else:
                print('\nInvalid selection. \n')
                startMenuChoice = input("To view all tickets, type 1 \nTo view a single ticket, type 2 \n")
            break


    def showMenu(self):
        on = True
        while on:
            mainMenuChoice = input("\nTo view all tickets, type 1 \nTo view a single ticket, type 2 \nTo exit, type 3\n")
            if mainMenuChoice == "1": 
                self.showAllTickets() 
            elif mainMenuChoice == "2": 
                y = input('\nEnter the number of the ticket you would like to view: \n')
                self.showSingleTicket(y)
            elif mainMenuChoice == '3':
                print('\nThank you for using the ticket viewer. Goodbye!\n')
                break
            else:
                print('\nInvalid selection. \n')
                mainMenuChoice = input("To view all tickets, type 1 \nTo view a single ticket, type 2 \n")
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
        jsonTickets,prev,next,has_more = self.switchPage()
        lastID = ""
        while has_more:
            for i in range(len(jsonTickets)):
                print(str(jsonTickets[i]['id']) + ". " + jsonTickets[i]['subject'])
                lastID = jsonTickets[i]['id']
                if i == (len(jsonTickets) - 1):
                    if lastID >= 26 and lastID < self.getTicketsCount() - 1:
                        pageDirection = input('\n\nTo view next page, type 1.\nTo view previous page, type 2\nTo view the main menu, type 3\n')
                    elif lastID < 26:
                        pageDirection = input('\n\nTo view next page, type 1.\nTo view the main menu, type 3\n')
                    elif lastID == self.getTicketsCount():
                        pageDirection = input('\n\nTo view prev page, type 2.\nTo view the main menu, type 3\n')
                    if pageDirection == '1':
                        jsonTickets,prev,next,has_more = self.switchPage(next)
                    elif pageDirection == '2':
                        jsonTickets,prev,next,has_more = self.switchPage(prev)
                    elif pageDirection == '3':
                        self.showMenu()
                        has_more = False
                        break
                    else:
                        print('\nInvalid selection. \n')
                        pageDirection = input('\n\nTo view next page, type 1.\nTo view previous page, type 2\nTo view the main menu, type 3\n\n')        


    def switchPage(self, url = None):
        if url == None:
            url = self.pageurl
        jsonTickets = self.getTickets(url)
        prev = jsonTickets['links']['prev']
        next = jsonTickets['links']['next']
        has_more = jsonTickets['meta']['has_more']
        jsonTickets = jsonTickets['tickets']
        return jsonTickets,prev,next,has_more


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
    

email = str(os.environ.get('email'))
api_token = str(os.environ.get('api_token'))
subdomain = str(os.environ.get('subdomain'))
obj = Ticket(email,api_token, subdomain)
obj.greeting()
obj.startMenu()






