from commands.message_command import MessageCommand


class HelloWorldCommand(MessageCommand):

    def __init__(self):
        super().__init__("hello world")

    def serialize(self):
        return "HWC"

    @staticmethod
    def deserialize(raw):
        if raw == "HWC":
            return HelloWorldCommand()
