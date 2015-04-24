"""Hello World API implemented using Google Cloud Endpoints.

Defined here are the ProtoRPC messages needed to define Schemas for methods
as well as those methods defined in an API.
"""

import endpoints
from protorpc import messages
from protorpc import message_types
from protorpc import remote

# All of the imports shown are required for an Endpoints API backend.

package = "hello"

class Greeting(messages.Message):
    """Greeting that stores a message."""
message = messages.StringField(1)

class GreetingCollection(messages.Message):
    """Collection of Greetings."""
items = messages.MessageField(Greeting, 1, repeated=True)

STORED_GREETING = GreetingCollection(items[Greeting(message='hello world!'), Greeting(message='goodbye world!')])
