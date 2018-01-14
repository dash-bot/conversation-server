class LuisCommands(object):

    none = "none"
    confirm = "confirm"
    cancel = "cancel"

    confirm_commands = []

    @staticmethod
    def requires_confirm(intent):
        return intent in LuisCommands.confirm_commands

    @staticmethod
    def is_action(intent):
        return not LuisCommands.is_confirm(intent)

    @staticmethod
    def is_confirm(intent):
        return intent == LuisCommands.confirm

    @staticmethod
    def is_confirmation(intent):
        return intent == LuisCommands.confirm or intent == LuisCommands.cancel
