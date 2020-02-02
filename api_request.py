import requests
from requests_oauthlib import OAuth1
import secret
import webbrowser


def api_request_Authentication():
    # first: POST oauth/request_token
    oauth_requestToken_url = "https://api.twitter.com/oauth/request_token"
    oauth_requestToken_parameters = {'oauth_callback': 'oob'}

    auth = OAuth1(secret.api_key, secret.api_key_secret, secret.access_token, secret.access_token_secret)
    oauth_tokenRequest = requests.get(oauth_requestToken_url, auth=auth, params=oauth_requestToken_parameters)

    # make sure tat the status code is 200
    if oauth_tokenRequest.status_code == 200:
        data = oauth_tokenRequest.content.decode('ASCII')
        oauth_token_response = data.split("&")
        print(oauth_token_response)
        # need to verify that oauth_callback_confirmed is true

    # second: GET oauth/authorize
    authorize_params = {'force_login': 'true'}
    authorize_url = "https://api.twitter.com/oauth/authorize" + '?' + oauth_token_response[0]

    oauth_tokenVerifier = requests.get(authorize_url, params=authorize_params)

    # This line opens the web browser for the user to authenticate and recieve the 7 digit code
    webbrowser.open_new(oauth_tokenVerifier.url)

    oauth_verifier = input("Please enter the 7 digit code recieved after authorizing your twitter profile: ")

    # error check user input (needs to be 7 digit string of numbers)

    # third: POST oauth/access_token
    accessToken_url = "https://api.twitter.com/oauth/access_token"
    accessToken_parameters = {'oauth_token': oauth_token_response[0][12:], 'oauth_verifier': oauth_verifier, 'oauth_consumer_key': secret.api_key}
    oauth_token = requests.get(accessToken_url, params=accessToken_parameters)

    print(oauth_token.status_code)  # make sure code is 200
    print(oauth_token.text)
    responsedata = oauth_token.text.split("&")
    return responsedata

# def api_request_Timeline()
