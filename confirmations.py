# Confirmation messages, function names must match LUIS intent
from luis_sdk.luis_response import LUISResponse
from luis_sdk.luis_entity import LUISEntity


def none(LUISReponse):
    return "I'm sorry I did not understand your request"


def checkbalance(LUISResponse):
    accounts = LUISResponse.get_entities()
    print(accounts)
    if accounts:
        # do confidence checking
        return "Would you like to check the balance of your {0} accounts?"\
            .format(accounts.join(", "))
    else:
        return "Would you like to check the balance of your account"

