from dotenv import load_dotenv
from requests.api import patch
load_dotenv('keys.env.example')
import os,pytest,sys, unittest
from Ticket.main import Ticket
from mock import Mock


class TestTicket():

    @pytest.fixture
    def test_sampleAuth(self):
        email = str(os.environ.get('email'))
        api_token = str(os.environ.get('api_token'))
        subdomain = str(os.environ.get('subdomain'))
        obj = Ticket(email,api_token, subdomain)
        return email, api_token, subdomain, obj

    @pytest.fixture
    def test_sampleAuthBad(self):
        bademail = str(os.environ.get('email1'))
        badapi_token = str(os.environ.get('api_token1'))
        badsubdomain = str(os.environ.get('subdomain1'))
        badobj = Ticket(bademail,badapi_token, badsubdomain)

    @pytest.fixture
    def test_sampleAPI(self):
        return {
        "tickets": [
            {
            "url": "https://zccintern2022.zendesk.com/api/v2/tickets/1.json",
            "id": 1,
            "external_id": None,
            "via": {
                "channel": "sample_ticket",
                "source": {
                "from": {},
                "to": {},
                "rel": None
                }
            },
            "created_at": "2021-11-23T17:55:33Z",
            "updated_at": "2021-11-23T17:55:33Z",
            "type": "incident",
            "subject": "Sample ticket: Meet the ticket",
            "raw_subject": "Sample ticket: Meet the ticket",
            "description": "Hi there,\n\nI\u2019m sending an email because I\u2019m having a problem setting up your new product. Can you help me troubleshoot?\n\nThanks,\n The Customer\n\n",
            "priority": "normal",
            "status": "open",
            "recipient": None,
            "requester_id": 1902304574244,
            "submitter_id": 1267099175570,
            "assignee_id": 1267099175570,
            "organization_id": None,
            "group_id": 1900005049064,
            "collaborator_ids": [],
            "follower_ids": [],
            "email_cc_ids": [],
            "forum_topic_id": None,
            "problem_id": None,
            "has_incidents": False,
            "is_public": True,
            "due_at": None,
            "tags": [
                "sample",
                "support",
                "zendesk"
            ],
            "custom_fields": [],
            "satisfaction_rating": None,
            "sharing_agreement_ids": [],
            "followup_ids": [],
            "ticket_form_id": 1900004110664,
            "brand_id": 1900001306244,
            "allow_channelback": False,
            "allow_attachments": True
            },
            {
            "url": "https://zccintern2022.zendesk.com/api/v2/tickets/2.json",
            "id": 2,
            "external_id": None,
            "via": {
                "channel": "api",
                "source": {
                "from": {},
                "to": {},
                "rel": None
                }
            },
            "created_at": "2021-11-24T05:27:46Z",
            "updated_at": "2021-11-24T05:27:46Z",
            "type": None,
            "subject": "velit eiusmod reprehenderit officia cupidatat",
            "raw_subject": "velit eiusmod reprehenderit officia cupidatat",
            "description": "Aute ex sunt culpa ex ea esse sint cupidatat aliqua ex consequat sit reprehenderit. Velit labore proident quis culpa ad duis adipisicing laboris voluptate velit incididunt minim consequat Nonea. Laboris adipisicing reprehenderit minim tempor officia ullamco occaecat ut laborum.\n\nAliquip velit adipisicing exercitation irure aliqua qui. Commodo eu laborum cillum nostrud eu. Mollit duis qui non ea deserunt est est et officia ut excepteur Lorem pariatur deserunt.",
            "priority": None,
            "status": "open",
            "recipient": None,
            "requester_id": 1267099175570,
            "submitter_id": 1267099175570,
            "assignee_id": 1267099175570,
            "organization_id": 1900081408664,
            "group_id": 1900005049064,
            "collaborator_ids": [],
            "follower_ids": [],
            "email_cc_ids": [],
            "forum_topic_id": None,
            "problem_id": None,
            "has_incidents": False,
            "is_public": True,
            "due_at": None,
            "tags": [
                "est",
                "incididunt",
                "nisi"
            ],
            "custom_fields": [],
            "satisfaction_rating": None,
            "sharing_agreement_ids": [],
            "followup_ids": [],
            "ticket_form_id": 1900004110664,
            "brand_id": 1900001306244,
            "allow_channelback": False,
            "allow_attachments": True
            }
        ],
        "meta": {
            "has_more": True,
            "after_cursor": "eyJvIjoibmljZV9pZCIsInYiOiJhUUlBQUFBQUFBQUEifQ==",
            "before_cursor": "eyJvIjoibmljZV9pZCIsInYiOiJhUUVBQUFBQUFBQUEifQ=="
        },
        "links": {
            "prev": "https://zccintern2022.zendesk.com/api/v2/tickets.json?page%5Bbefore%5D=eyJvIjoibmljZV9pZCIsInYiOiJhUUVBQUFBQUFBQUEifQ%3D%3D&page%5Bsize%5D=2",
            "next": "https://zccintern2022.zendesk.com/api/v2/tickets.json?page%5Bafter%5D=eyJvIjoibmljZV9pZCIsInYiOiJhUUlBQUFBQUFBQUEifQ%3D%3D&page%5Bsize%5D=2"
        }
        }


    def test_init(self, test_sampleAuth):
        email, api_token, subdomain, obj = test_sampleAuth
        assert obj.email == email
        assert obj.api_token == api_token
        assert obj.subdomain == subdomain
        assert obj.ticketurl == 'https://' + obj.subdomain + '.zendesk.com/api/v2/tickets.json'
        assert obj.pageurl == 'https://' + obj.subdomain + '.zendesk.com/api/v2/tickets.json?page[size]=25'

    def test_greeting(self,test_sampleAuth, capfd):
        obj = test_sampleAuth[3]
        obj.greeting()
        captured1,err = capfd.readouterr()
        assert captured1 == "\n\tWELCOME TO THE TICKET VIEWER!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"

    def test_startMenu(self, test_sampleAuth, monkeypatch):
        return 0


    def test_showMenu(self):
        return 0


    def test_getTickets(self, test_sampleAPI, test_sampleAuth):
        return 0


    def test_showAllTickets(self):
        return 0


    def test_switchPage(self):
        return 0


    def test_showSingleTicket(self):
        return 0


    def test_printTicket(self):
        return 0


    def test_getTicketsCount(self, test_sampleAPI):
        return 0
    

