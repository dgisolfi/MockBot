# MockBot [![MockBot version](https://img.shields.io/pypi/v/MockBot.svg)](https://pypi.org/project/MockBot)

A Bot that responds with the "spongemock" version of a message when sent by a particular user.

### Author

**Daniel Gisolfi** - *All current work* - [dgisolfi](https://github.com/dgisolfi)

## Groupme Bot

 A GroupMe bot can be created [here](https://dev.groupme.com/bots) and using the Groupme API can send messages to its assigned group. This particular bot uses a callback URL to be notified of new messages. Once notified the message will be parsed and a response will be created if the `USER_ID` of the sender matches that of the `USER_ID` environment variable.

## Usage

Once a bot is registered with Groupme the following requirements must be specified in the form of environment variables:

* **USER_ID** - The ID of the user that should be mocked in the group chat.

  Example: `USER_ID=29384`    
  
* **BOT_ID** - The assigned bot ID by GroupMe.

  Example: `BOT_ID=a6a7a7a7a7a7a7a7a77a7a7`    

* **GROUP_ID** - The ID of the Groupme Chat where the bot resides

  Example: `GROUP_ID=0987890987`    
* **API_TOKEN** - The api token for the authorized Groupme account

  Example: `API_TOKEN=983u4ritgo0v98ujkorf`

After the environment variables have been set run the Flask server, `python -m MockBot`

## Customization/Additions

Feature Additions/Suggestions are welcome, for any particular functionality that may need to be added for a particular use case, simple parse the incoming messages looking for specified input in the `server.py` file and add methods in the bot class to perform the desired function.

