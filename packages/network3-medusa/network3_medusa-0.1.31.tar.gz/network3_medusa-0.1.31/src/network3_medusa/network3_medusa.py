import os
import json
import click
from dotenv import load_dotenv
from hedera import Client, AccountId, PrivateKey, Hbar, FileCreateTransaction, FileId, FileContentsQuery
import subprocess

load_dotenv()

OPERATOR_ID= AccountId.fromString(os.getenv("OPERATOR_ID"))
OPERATOR_KEY= PrivateKey.fromString(os.getenv("OPERATOR_KEY"))

class Network3Medusa():
    def __init__(self, command):
        self.command = command

    def network3_medusa(self):
        self.py2output()
        print("here")
        print(self.output)
        # self.add_file_to_hedera(parsed_json)
        
    def py2output(self):
        self.output = subprocess.run(["python", "call_clid.py", self.command])

    # def add_file_to_hedera(self, parsed_json):
    #     client = Client.forTestnet()
    #     client.setOperator(OPERATOR_ID, OPERATOR_KEY)
    #     fileContents = parsed_json
    #     tran = FileCreateTransaction()
    #     resp = tran.setKeys(OPERATOR_KEY.getPublicKey()).setContents(fileContents).setMaxTransactionFee(Hbar(2)).execute(client)
    #     print("nodeId: ",  resp.nodeId.toString())
    #     receipt = resp.getReceipt(client)
    #     fileId = receipt.fileId
    #     print("file: ",  fileId.toString())
    #     query = FileContentsQuery()
    #     contents = query.setFileId(fileId).execute(client)
    #     json_contents = json.loads(contents.toStringUtf8())
    #     print(json_contents)        

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