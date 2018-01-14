'''
Actions to be taken, functions must match the intent name in LUIS
'''

def none(LuisReponse):
    # no action
    return "I'm sorry I did not understand your request"


def checkBalance(LuisResponse):
    accounts = LuisResponse.get_entities()
    reply = "Your balance of your {0} account is {1}.\n"
    if accounts:
        response = ""
        for account in accounts:
            response += reply.format(account.get_name(), "$10")
        return response
    return reply.format("chequings", "$1000") + reply.format("savings", "$100")


def transferOut(LuisResponse):
    entities = dict([(entity.get_type(), entity.get_name()) for entity in LuisResponse.get_entities()])
    return "Transferred {0} dollars from {1} to {2}".format(entities["Number"], entities["ContactName"], entities["AccountType"])

