class LuisCommands(object):

    none = "None"
    confirm = "Confirm"
    cancel = "Cancel"

    @staticmethod
    def is_action(intent):
        return not LuisCommands.isConfimation(intent)

    @staticmethod
    def is_confirmed(intent):
        return intent == LuisCommands.confirm

    @staticmethod
    def is_confirmation(intent):
        return intent == LuisCommands.confirm or intent == LuisCommands.cancel
