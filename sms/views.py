from django.shortcuts import render
from twilio.rest import Client
import http.client
# from twilio_api import settings
# from twilio.rest import TwilioRestClient

def home(request):
    return render(request, 'sms/index.html', {})

def sms(request):
    account_sid = "ACe3f82446d48c6a3cc77a6ad6adb259f7"
    auth_token  = "0a9c5b3d35ac1795c4c87f6b0c461d09"
    client = Client(account_sid, auth_token)


    message = client.messages\
    .create(
    to='+919482893063',
    from_='+19282966720',
    body='This message is sent through twilio api using django framework by me.')

    print(message.sid)
    # conn = http.client.HTTPSConnection("control.msg91.com")
    #
    # payload = '''{
    #   "sender": "SOCKET",
    #   "route": "4",
    #   "country": "91",
    #   "sms": [
    #     {
    #       "message": "hello test",
    #       "to": [
    #         "9482893063",
    #
    #       ]
    #     }
    #
    #   ]
    # }'''
    #
    #
    # headers = { 'authkey':"293805AoaU2SvUfX1m5d7a8b0c",'content-type': "application/json" }
    #
    # conn.request("POST", "/api/postsms.php", payload, headers)
    #
    # res = conn.getresponse()
    # data = res.read()
    #
    # print(data.decode("utf-8"))


    return render(request, 'sms/thankyou.html')
