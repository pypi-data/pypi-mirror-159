import os
import json
import click
from dotenv import load_dotenv
import subprocess

load_dotenv()

ACCOUNTID = os.getenv("ACCOUNTID")
PUBLICKEY = os.getenv("PUBLICKEY")
PRIVATEKEY = os.getenv("PRIVATEKEY")

class Network3Medusa():
    def __init__(self, command):
        self.command = command
        self.accountID = ACCOUNTID
        self.publicKey = PUBLICKEY
        self.privateKey = PRIVATEKEY

    def network3_medusa(self):
        self.py2output()

    def py2output(self):
        output = subprocess.call(["python", "call_clid.py", f'--"{ self.command }"'])
        print(output)
        return(output)

@click.command()
@click.option('--command',
    prompt='Command',
    help=('A valid Command'),
    required=True)

def cli(command):
    invoke_class = Network3Medusa(command)
    invoke_class.network3_medusa()

if __name__ == '__main__':
    Network3Medusa.main()