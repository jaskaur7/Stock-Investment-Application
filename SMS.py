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
        account_sid = ''
        auth_token = ''
        client = Client(account_sid, auth_token)
        textMessage = "You can now buy the "+stockName+" stocks"
        message = client.messages.create(
                             body=textMessage,
                  #from twilio number to your personal number
                             from_='',
                             to=''
                         )
        # Display this statement in the phone message
        print("Your message has been sent for '{0}' share.".format(stockName))
