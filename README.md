# ZendeskCodingChallenge2022

##Ticket Viewer

Zendesk is a customer service tool that allows the creation and management of support tickets. This app will:
● Connect to the Zendesk API
● Request all the tickets for your account
● Display them in a list
● Display individual ticket details
● Page through tickets when more than 25 are returned

##Installation

From the root folder of the project, use the package manager pip to install python 3, dotenv, and pytest

If you don't already have Python installed, install it using this article:https://realpython.com/installing-python/#how-to-install-python-on-macos and confirm it is Python 3.

Install dotenv and pytest using the following commands:

```bash
pip install python-dotenv
```

```bash
pip install -U pytest
```

##Usage

Update 'keys.env.example' to include your authentication info and add the file name to .gitignore or change file name to 'keys.env' as 'keys.env' is already included in .gitignore

```bash
email=email@email.com
api_token=token
subdomain=subdomain
```
To run tests, comment out function calls and new instance. Then run py.test from root directory 

```bash
# email = str(os.environ.get('email'))
# api_token = str(os.environ.get('api_token'))
# subdomain = str(os.environ.get('subdomain'))
# obj = Ticket(email,api_token, subdomain)
# obj.greeting()
# obj.startMenu()
```

```bash
(base) user@user ZendeskCodingChallenge2022 % py.test
```
    
