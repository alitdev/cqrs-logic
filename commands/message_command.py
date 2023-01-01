
class MessageCommand:

    def __init__(self, message):
        self.message = message

    def execute(self):
        print(self.message)

    def serialize(self):
        return "MC: " + self.message

    @staticmethod
    def deserialize(raw):
        if raw.startswith("MC: "):
            message = raw.split(" ")[1]
            return MessageCommand(message)
