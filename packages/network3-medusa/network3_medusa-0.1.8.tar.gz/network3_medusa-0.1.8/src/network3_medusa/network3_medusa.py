import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
ACCOUNTID = os.getenv("ACCOUNTID")
PUBLICKEY = os.getenv("PUBLICKEY")
PRIVATEKEY = os.getenv("PRIVATEKEY")
IPADDRESS = os.getenv("IPADDRESS")

class Network3Medusa():
    def __init__(self):
        self.username = USERNAME
        self.password = PASSWORD
        self.accountID = ACCOUNTID
        self.publicKey = PUBLICKEY
        self.privateKey = PRIVATEKEY
        self.url = f'http://{ IPADDRESS }/ins'
        self.myheaders = {'content-type':'application/json'}
    def network3_medusa(self):
        self.show_version = self.get_show_version()
        print(self.show_version)

    def get_show_version(self):
        payload={
          "ins_api":{
          "version": "1.0",
          "type": "cli_show",
          "chunk": "0",
          "sid": "1",
          "input": "show version",
          "output_format": "json"
        }}
        response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword)).json()
        output = json.dumps(response, indent=4, sort_keys=True)
        return(output)

def cli():

    invoke_class = Network3Medusa()
    invoke_class.network3_medusa()

if __name__ == '__main__':
    Network3Medusa.main()