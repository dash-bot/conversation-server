from flask import Flask, request
from luis_sdk import LUISClient
import commands
import confirmations
from luis_command_names import LuisCommands
app = Flask(__name__)
application = app

# TODO get these, then hide them
APPID = "a754fc42-56f2-434a-a56b-8818c3df71f5"
APPKEY = "3423d600dd744266867e8ec0752b881b"
prev_action = None
prev_reply = None
none_command = commands.none(None)

CLIENT = LUISClient(APPID, APPKEY, True)

@app.route("/")
def get_command():
    command = request.args.get("command")
    reply = CLIENT.predict(command)

    # error checking here

    intent = reply.get_top_intent().get_name()
    print(intent)
    if LuisCommands.is_confirmation(intent):
        return confirm_cancel_request(intent, prev_action, prev_reply)
    else:
        action = getattr(commands, intent.lower())
        confirm_reply = getattr(confirmations, intent.lower())
        prev_action = action
        prev_reply = reply
        return confirm_reply(reply)


def confirm_cancel_request(intent, action, reply):
    if LuisCommands.is_confirmed(intent):
        if action and reply:
            reply = action(reply)
        else:
            reply = none_command()
        return reply
    else:
        return "Canceled request"


