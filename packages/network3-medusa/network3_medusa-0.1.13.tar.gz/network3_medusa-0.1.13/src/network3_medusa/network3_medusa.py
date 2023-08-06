import os
import json
from dotenv import load_dotenv
import subprocess

load_dotenv()

ACCOUNTID = os.getenv("ACCOUNTID")
PUBLICKEY = os.getenv("PUBLICKEY")
PRIVATEKEY = os.getenv("PRIVATEKEY")

class Network3Medusa():
    def __init__(self):
        self.accountID = ACCOUNTID
        self.publicKey = PUBLICKEY
        self.privateKey = PRIVATEKEY

    def network3_medusa(self):
        py2output = subprocess.check_output(["python", "show_version.py"])
        print(py2output)

def cli():
    invoke_class = Network3Medusa()
    invoke_class.network3_medusa()

if __name__ == '__main__':
    Network3Medusa.main()