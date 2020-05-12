"""
 @PythonWebScrapping.py
 
 Contains the main function getCurrentPrice(stockName) from which different functions located in other files are called to perform 
 different tasks assigned such as to pull the data and save it in .csv file and send an SMS through twilio account when the 
 share price is in the range of the user.

"""
import time
import twilio
import requests
from SMS import *
from DataPull import *
from bs4 import BeautifulSoup
from pyautogui import alert,prompt
from twilio.base.exceptions import TwilioRestException

class CurrentPrice:
    # Function get the current price of the stock by scraping data fom yahoo finance
    def getCurrentPrice(self,stockName):
        # URL of the stock
        url = "https://finance.yahoo.com/quote/"+stockName+"/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text
        price = str(price).replace(',','')
        return float(price)

class WrapperClass:     
    
    choice = "yes"
    while (choice == "yes"):
        check = 0
        currentPrice = 0.0
        # Get current price
        try:
            name_choice = 1
            # Enter the name of the share you want to buy.
            while(name_choice == 1):
                stockName = prompt(text='Enter name of share', title='Enter name',default='')
                #URL of the summary tab of stock
                target_website=r'https://sg.finance.yahoo.com/quote/'+(stockName)+'?p='+(stockName)
                #Check if stock name is provided
                if stockName:
                    print("The entered Stock name is: ",stockName,sep="")
                    name_choice=0
                else:
                    print("You have to enter any share name")
                    name_choice=1
            
            #Creating object of CurrentPrice
            #Calling getCurrentPrice to retrieve the current price
            Price = CurrentPrice()
            currentPrice = Price.getCurrentPrice(stockName)
            alert(text='Current price is : '+ str(currentPrice), title='Data', button='OK')
            print("The current price of "+stockName+" shares is: ",currentPrice,sep="")
                
            #Creating object of GetSummary class and calling get_key_summary function to retrieve summary in excel sheet
            summary = GetSummary()
            summary.get_key_summary(target_website)
            check = 1 
        
        # Display a  type of dialog box (alert) when invalid share name is written or nothing is typed
        except:
            alert(text='Invalid Stock Name', title='Invalid', button='OK')                  

        #Asking user to enter the preferred price for buying stock
        if check == 1:
            prefer_choice = 1
            
            # Entering the user's price
            while(prefer_choice == 1):
                preferredRate = prompt(text='Enter the preffered rate to buy share', title='Enter price', default='')
                
                try :
                    if (preferredRate is not 0):
                        preferredRate = float(preferredRate)
                        while(True):
                            try:
                                # User's price is more than or equal to the actual price of the stock    
                                if preferredRate >= currentPrice:
                                    sendNotification = Notification()
                                    sendNotification.sendSms(stockName)
                                    prefer_choice = 0
                                    break
                                # Actual price is more than user's choice
                                else:
                                    currentPrice = Price.getCurrentPrice(stockName)
                                    print("Waiting for {0} to reach {1} USD".format(stockName,preferredRate))
                                    time.sleep(3)
                            except TwilioRestException:
                                alert(text='Invalid/Unregistered number of the recipient', title='Mobile Number', button='OK')
                                break
                            
                except ValueError:
                    alert(text='Please enter a valid price', title='Price', button='OK')
                    prefer_choice = 1
                    
        # User input asking whether user wants to know any other share price or not
        choice = input("Do you want to know about another share price (yes/no)? ")
    print("System is exiting because you did not press yes")
            
if __name__ == "__main__":
    wrappper = WrapperClass()
