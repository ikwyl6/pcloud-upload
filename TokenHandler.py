#!/usr/bin/python

# Create my own TokenHandler class so oauth2_authorize
# can use it for headless mode
class TokenHandler:
    redirect_url = "localhost"

    def __init__(self, client_id):
        self._id = client_id
        self.auth_url = f"https://my.pcloud.com/oauth2/authorize?response_type=code&redirect_uri={self.redirect_url}&client_id={self._id}"

    def get_access_token(self):
        print("Copy url into browser: {0}".format(self.auth_url))
        access_token = input("\nCopy/paste the 'code' portion of the link in address bar here: ")
        return access_token, "localhost"

