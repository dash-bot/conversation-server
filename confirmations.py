# Confirmation messages, function names must match LUIS intent
from luis_sdk.luis_response import LUISResponse
from luis_sdk.luis_entity import LUISEntity


def transferOut(LuisResponse):
    entities = dict([(entity.get_type(), entity.get_name()) for entity in LuisResponse.get_entities()])
    amount = entities["Number"]
    user = entities["ContactName"]
    account = entities["AccountType"]
    if not amount:
        return "Please specify the amount to transfer"
    if not user:
        return "Please specify the contact to transfer to"
    if not account:
        return "Please specify the account type"
    return "Would you like to transfer {0} from {1} to {2}".format(amount, user, account)
