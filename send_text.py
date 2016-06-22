from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd843dfe3d8ccad23c386bc1574e3c66f"
auth_token  = "a79aa85fe043fa528425cef2a7da9607"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Happy Valentine Day par, Mu Paing Shin Ma Gyi MaMa Khine! <fart you>",
    to="+15108238237",    # Replace with your phone number
    from_="+16503628845") # Replace with your Twilio number
print message.sid
