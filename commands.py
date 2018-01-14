from luis_sdk.luis_response import LUISResponse
'''
Actions to be taken, functions must match the intent name in LUIS
'''

def none(LuisReponse):
    # no action
    return "I'm sorry I did not understand your request"

def checkbalance(LuisReponse):
    # Bank API Stuff
    # Get accounts from response
    return "Your balance is $100"
