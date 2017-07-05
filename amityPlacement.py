
from twilio.rest import Client #SMS API Package
import urllib2
import re
import time
 
account_sid = "Account ID Here" #Your Twilio account ID
auth_token = "Secret API Token Here"    #Your secret API Token
 
client = Client(account_sid, auth_token)
 
while 1:
 
    html_content = urllib2.urlopen('http://amity.edu/placement/Popup.asp?Eid=2161').read()
 
    matches = re.findall('Batch', html_content);
 
 
    if len(matches) == 0: 
       print ("No new placement notification") #there is no new update, no msg will be sent
       time.sleep(5) #sleep for a period of 5 seconds
 
    else:
       message = client.api.account.messages.create(to="Your Number", from_="Your Twilio Number", body="There is a new placement update. Visit http://amity.edu/placement ") #this is the method to send a new message
       print ("New placement notification, SMS sent") 
       quit()
