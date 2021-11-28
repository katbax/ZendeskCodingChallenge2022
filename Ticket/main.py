from dotenv import load_dotenv
load_dotenv('keys.env')
import requests, os

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
        return greeting


    def startMenu(self):
        on = True
        while on:
            startMenuChoice = input('\nTo view the menu, type 1\nTo quit, type 2\n')
            if startMenuChoice not in ['1', '2']:
                print('\nInvalid choice.')
            if startMenuChoice == '1':
                self.showMenu()
            elif startMenuChoice == '2':
                print('\nThank you for using the ticket viewer. Goodbye!\n')
                on = False
            else:
                continue
                
            
            


    def showMenu(self):
        on = True
        while on:
            mainMenuChoice = input("\nTo view all tickets, type 1 \nTo view a single ticket, type 2 \nTo quit, type 3\n")
            if mainMenuChoice not in ['1', '2', '3']:
                print('\nInvalid choice.')
            if mainMenuChoice == "1": 
                self.showAllTickets() 
            elif mainMenuChoice == "2": 
                y = input('\nEnter the number of the ticket you would like to view: \n')
                if not 1 <= int(y) < (self.getTicketsCount() + 1):
                    print("\n\nInvalid number. Try again\n\n")
                    continue
                self.showSingleTicket(y)
            elif mainMenuChoice == '3':
                print('\nThank you for using the ticket viewer. Goodbye!\n')
                exit()
            else:
                continue
            


    def getTickets(self, url = None):
        if url == None:
            url = self.pageurl
        headers = {
            'Content-Type': 'application/json',
        }
        response = requests.get(url, auth=(self.email + '/token', self.api_token))
        if response.status_code >= 400 and response.status_code <= 500:
            print("Oh, no! Error: " + str(response.reason) + ". Please try again. Goodbye!")
            exit()
        else:
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
                        pageDirection = input('\n\nTo view next page, type 1.\nTo view previous page, type 2\nTo view the main menu, type 3\nTo view a ticket, type 4\n')
                        if pageDirection not in ['1', '2', '3', '4']:
                            print('\nInvalid choice. Try again')
                            continue
                    elif lastID < 26:
                        pageDirection = input('\n\nTo view next page, type 1.\nTo view the main menu, type 3\nTo view a ticket, type 4\n')
                        if pageDirection not in ['1', '3', '4']:
                            print('\nInvalid choice. Try again')
                            continue
                    elif lastID == self.getTicketsCount():
                        pageDirection = input('\n\nTo view prev page, type 2.\nTo view the main menu, type 3\nTo view a ticket, type 4\n')
                        if pageDirection not in ['2', '3', '4']:
                            print('\nInvalid choice. Try again')
                            continue
                    if pageDirection == '1':
                        jsonTickets,prev,next,has_more = self.switchPage(next)
                    elif pageDirection == '2':
                        jsonTickets,prev,next,has_more = self.switchPage(prev)
                    elif pageDirection == '3':
                        self.showMenu()
                        has_more = False
                        break
                    elif pageDirection == '4':
                        ticketNumber = input('\nEnter ticket number: ')
                        if not 1 <= int(ticketNumber) < (self.getTicketsCount() + 1):
                            print("\n\nInvalid number. Try again\n\n")
                            continue
                        self.showSingleTicket(ticketNumber)
                        has_more = False
                    else:
                        continue

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






