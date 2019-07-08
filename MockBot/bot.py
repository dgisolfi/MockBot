#!/usr/bin/python3
# 2019-7-7

import re
import requests
from spongemock.spongemock import mock

class Bot:
    def __init__(self, user_id, bot_id, group_id, api_token):
        self.bot_id = bot_id
        # This is the user ID of the person who should be "mocked"
        self.user_id = user_id
        self.group_id = group_id
        self.api_token = api_token
        self.api_base_url = 'https://api.groupme.com/v3'
        self.api_session = requests.session()

       
    def sendMessage(self, msg):
        '''Send a message from the bot to its assigned group.
            Args:
                msg (str): message to be sent to group
            Returns:
                request response
        '''
        # set parameters for post request
        params = {
            'bot_id': self.bot_id,
            'text': msg
        }
        # send the request to the api and get the results in the response var
        response = self.api_session.post(
            f'{self.api_base_url}/bots/post', 
            params=params
        )
        return response
        
    def checkUser(self, callback):
        """ Check if the message sent was by a ceartin user
        Parameters
        ----------
        callback : object
            - An instance of
        Returns
        -------
        boolean
            True if ....
        """
        return True if callback['user_id'] == self.user_id else False
         
        
    def getResponse(self, msg):
        '''Given a message the appropriate response is returned.
            Args:
                msg (str): a message to respond to
            Returns:
                response (str): the bot's response to the message
        '''
        # makes a call to the sponegemock package to make the resposne
        return mock(msg)