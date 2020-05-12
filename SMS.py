"""
 @SMS.py
 
 Includes the function for sending the message to the user through twilio account whenever that stock rate is in the range of the user

"""

from twilio.rest import Client

class Notification():
    #Function to send SMS to end user by making use of 3rd Party API - twilio
    #Recepient number shoud be registered to send SMS
    def sendSms(self,stockName):
        #account_sid and auth_token are user specific and can be retrieved fom twilio website
        account_sid = 'ACf08c30993e8ecf5239d038dff5902700'
        auth_token = '9bd9a32bf17b37e3e35665967c5a32fa'
        client = Client(account_sid, auth_token)
        textMessage = "You can now buy the "+stockName+" stocks"
        message = client.messages.create(
                             body=textMessage,
                             from_='+12029522907',
                             to='+18732886120'
                         )
        # Display this statement in the phone message
        print("Your message has been sent for '{0}' share.".format(stockName))