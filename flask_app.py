from flask import Flask, request, session
from luis_sdk import LUISClient
import commands
import confirmations
from luis_command_names import LuisCommands
from luis_sdk.luis_response import LUISResponse

app = Flask(__name__)
app.secret_key = '\xe2\xd2\xfeSIM\x93\xad\x1b\x8bGgn{V\xd0\x00\x8f\x13\x95dr\xeeT'
application = app

# TODO get these, then hide them
APPID = "a754fc42-56f2-434a-a56b-8818c3df71f5"
APPKEY = "3423d600dd744266867e8ec0752b881b"

CLIENT = LUISClient(APPID, APPKEY, True)


@app.route("/")
def get_command():
    command = request.args.get("command")
    if not command:
        print("No command parameter")
        return
    print(command)
    reply = CLIENT.predict(command)
    # error checking here

    intent = camelCase(reply.get_top_intent().get_name())
    print("Intent: ", intent)
    if LuisCommands.is_confirmation(intent):
        if session['prev_reply']:
            prev_reply = LUISResponse(session['prev_reply'])
            print("Previous Intent: ", prev_reply.get_top_intent().get_name())
        else:
            prev_reply = None
        session['prev_reply'] = None
        return confirm_cancel_request(intent, prev_reply)
    elif LuisCommands.requires_confirm(intent):
        confirm_reply = getattr(confirmations, intent)
        session['prev_reply'] = reply.json
        return confirm_reply(reply)
    else:
        session['prev_reply'] = None
        action = getattr(commands, intent)
        return action(reply)


def camelCase(str):
    return str[0].lower() + str[1:]


def confirm_cancel_request(intent, prev_reply):
    if prev_reply is None:
        return commands.none(None)
    if LuisCommands.is_confirm(intent):
        prev_intent = camelCase(prev_reply.get_top_intent().get_name())
        action = getattr(commands, prev_intent)
        return action(prev_reply)
    else:
        return "Canceled request"


