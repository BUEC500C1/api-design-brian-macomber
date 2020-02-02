'''
Brian Macomber - U25993688
References:
    https://requests.readthedocs.io/en/master/user/authentication/
'''

from api_request import api_request_Authentication


responsedata = api_request_Authentication()

token = responsedata[0][12:]
token_secret = responsedata[1][19:]
user_id = responsedata[2][8:]
screen_name = responsedata[3][12:]
print("token is: " + token)
print("secret token is: " + token_secret)
print("user id is: " + user_id)
print("Twitter handle is: " + screen_name)


'''
Questions to answer:
    How much of the twitter feed do I want to display?
        How should i format it to look good? (comes later)
    This file will call all the different modules
        import a ton of shit
'''
