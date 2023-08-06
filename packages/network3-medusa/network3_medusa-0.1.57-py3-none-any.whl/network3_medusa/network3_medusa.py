import os
import json
import click
import subprocess
from dotenv import load_dotenv
from hedera import Client, AccountId, PrivateKey, Hbar, FileCreateTransaction, FileContentsQuery
from jnius import autoclass


load_dotenv()

OPERATOR_ID = AccountId.fromString(os.getenv("OPERATOR_ID"))
OPERATOR_KEY = PrivateKey.fromString(os.getenv("OPERATOR_KEY"))

class Network3Medusa():
    def __init__(self, command):
        self.command = command

    def network3_medusa(self):
        self.py2output()
        raw_json=self.output.stdout.decode('utf-8')
        parsed_json = json.loads(raw_json)
        self.add_file_to_hedera(parsed_json)
        
    def py2output(self):
        self.output = subprocess.run(["python", "call_clid.py", self.command], capture_output=True)

    def add_file_to_hedera(self, parsed_json):
        client = Client.forTestnet()
        client.setOperator(OPERATOR_ID, OPERATOR_KEY)
        tran = FileCreateTransaction()
        resp = tran.setKeys(OPERATOR_KEY.getPublicKey()).setContents(parsed_json).setMaxTransactionFee(Hbar(2)).execute(client)
        print("nodeId: ",  resp.nodeId.toString())
        receipt = resp.getReceipt(client)
        fileId = receipt.fileId
        print("file: ",  fileId.toString())
        query = FileContentsQuery()
        contents = query.setFileId(fileId).execute(client)
        json_contents = json.loads(contents.toStringUtf8())
        print(json_contents)        

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