# ZendeskCodingChallenge2022

## Ticket Viewer

Zendesk is a customer service tool that allows the creation and management of support tickets. This app will:
● Connect to the Zendesk API
● Request all the tickets for your account
● Display them in a list
● Display individual ticket details
● Page through tickets when more than 25 are returned

I used Python 3 and Python's 'Requests' and 'OS' libraries to accomplish this task. I chose to make multiple requests from the API instead of using caching to conserve memory at the expense of reduced speed optimization.

I also used a Command Line Interface(CLI) for the user interface. See example output below:


<img width="993" alt="image" src="https://user-images.githubusercontent.com/54691273/143801616-e49bc869-6e50-4787-92cb-23788a55e362.png">
<img width="1031" alt="image" src="https://user-images.githubusercontent.com/54691273/143801666-fd89ec51-7fb7-4871-b562-c4743bb46583.png">

## Installation

From the root folder of the project, use the package manager pip to install python 3, dotenv, and pytest

If you don't already have Python installed, install it using this article:https://realpython.com/installing-python/#how-to-install-python-on-macos and confirm it is Python 3.

Install dotenv and pytest using the following commands:

```bash
pip install python-dotenv
```

```bash
pip install -U pytest
```

## Usage

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
    
## License

MIT License

Copyright (c) [2021] Katrina Baxter

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
