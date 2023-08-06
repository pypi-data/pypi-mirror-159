import json
from cli import *

command_output = clid("show version")
output = json.loads(command_output)
print(output)