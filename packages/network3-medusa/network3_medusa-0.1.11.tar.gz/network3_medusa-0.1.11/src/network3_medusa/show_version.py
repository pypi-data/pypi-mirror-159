import os
import json
from cli import *

class Network3Medusa():
    def __init__(self):
        self.accountID = ACCOUNTID
        self.publicKey = PUBLICKEY
        self.privateKey = PRIVATEKEY
    def network3_medusa(self):
        self.show_version = self.get_show_version()
        print(self.show_version)

    def get_show_version(self):
        command_output = clid("show version")
        output = json.loads(command_output)
        return(output)

def cli():
    invoke_class = Network3Medusa()
    invoke_class.network3_medusa()

if __name__ == '__main__':
    Network3Medusa.main()