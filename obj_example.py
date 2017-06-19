import os
from slackclient import SlackClient

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

BOT_ID = "U5CB5DP1S"

# constants
AT_BOT = "<@" + "U5CB5DP1S" + ">"

class Command(object):
    def execute(self):
        raise NotImplementedError()

    def respond(self):
        slack_client.api_call("chat.postMessage",
                              channel=channel,
                              text=self.response,
                              as_user=True)


class ExampleCommand(Command):
    def execute(self):
        self.response = "Sure...write some more code then I can do that!"


class Age(Command):
    age_limit = 40

    def execute(self):
        x = int(raw_input("How old are you"))
        if x > self.age_limit:
            self.response = "full of wisdom"
        else:
            self.response = "You're still fresh"

class Calculation(Command):
    def execute(self):
        self.response = "give me some numbers"



commands_list = {
    "do": ExampleCommand,
    "how": Age,
    "calc": Calculation
    
}


def handle_command(request, channel):
    for name, obj in commands_list:
        if request.startswith(name):
            my_command = obj()
            my_command.execute()
            my_command.respond()
