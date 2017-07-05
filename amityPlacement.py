
from twilio.rest import Client #SMS API Package
import urllib2
import re
import time
 
account_sid = "AC23530dd7e29cdf310d1cf0e0cfe80eac" #Your Twilio account ID
auth_token = "d57f693e21cbbd27d8b5497c64805865"    #Your secret API Token
 
client = Client(account_sid, auth_token)
 
while 1:
 
    html_content = urllib2.urlopen('http://amity.edu/placement/Popup.asp?Eid=2161').read()
 
    matches = re.findall('Batch', html_content);
 
 
    if len(matches) == 0: 
       print ("No new placement notification") #there is no new update, no msg will be sent
       time.sleep(5) #sleep for a period of 5 seconds
 
    else:
       message = client.api.account.messages.create(to="+91 8920321803", from_="+1 8058745672", body="There is a new placement update. Visit http://amity.edu/placement ") #this is the method to send a new message
       print ("New placement notification, SMS sent") 
       quit()
