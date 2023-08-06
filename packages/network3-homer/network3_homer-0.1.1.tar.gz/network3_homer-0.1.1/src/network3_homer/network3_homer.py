import sys
import os
import json
import click
import yaml
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from hedera import Client, AccountId, PrivateKey, Hbar, FileCreateTransaction, FileId, FileContentsQuery

OPERATOR_ID = AccountId.fromString(os.getenv("OPERATOR_ID"))
OPERATOR_PRIVATE_KEY = PrivateKey.fromString(os.getenv("OPERATOR_PRIVATE_KEY"))

class Network3Homer():
    def __init__(self,fileid):
        self.fileid = fileid
        self.supported_templates = [
                            'dir',
                            # 'show access-lists',
                            # 'show bgp process vrf all',
                            # 'show bgp sessions',
                            # 'show cdp neighbors',
                            # 'show cdp neighbors detail',
                            # 'show environment',
                            'show interface',
                            # 'show interface status',
                            # 'show interface transceiver',
                            'show inventory',
                            # 'show ip arp vrf all',
                            'show ip interface brief',
                            # 'show ip ospf',
                            # 'show ip ospf interface',
                            # 'show ip ospf interface vrf all',
                            # 'show ip ospf neighbors detail',
                            # 'show ip ospf neighbors detail vrf all',
                            # 'show ip route',
                            # 'show ip route vrf all',
                            # 'show mac address-table',
                            # 'show port-channel summary',
                            'show system resources',
                            'show version',
                            #'show vlan'
                            ]

    def network3_homer(self):
        self.parsed_json = self.get_hedera_json()
        self.determine_command()
        if self.command in self.supported_templates:
            self.all_files(self.parsed_json)
        else:
            self.json_file(self.parsed_json)
            self.yaml_file(self.parsed_json)

    def determine_command(self):
        if 'nxos_ver_str' in self.parsed_json:
            self.command = "show version"
        elif 'bytestotal' in self.parsed_json:
            self.command = "dir"
        elif 'cpu_state_idle' in self.parsed_json:
            self.command = "show system resources"

    def get_hedera_json(self):
        client = Client.forTestnet()
        client.setOperator(OPERATOR_ID, OPERATOR_PRIVATE_KEY)
        query = FileContentsQuery()
        hedera_fileId = FileId.fromString(self.fileid)
        contents = query.setFileId(hedera_fileId).execute(client)
        self.hedera_json = json.loads(contents.toStringUtf8())
        return self.hedera_json

    def json_file(self, parsed_json):
        with open(f'{ self.command }.json', 'w') as f:
            f.write(json.dumps(parsed_json,indent=4, sort_keys=True))

    def yaml_file(self, parsed_json):
        dirty_yaml = yaml.dump(json.loads(json.dumps(parsed_json,indent=4, sort_keys=True)), default_flow_style=False)
        clean_yaml = dirty_yaml.replace("!!python/unicode","")
        with open(f'{ self.command }.yaml', 'w') as f:
            f.write(clean_yaml)

    def html_file(self, parsed_json):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        html_template = env.get_template('html.j2')
        html_output = html_template.render(command = self.command,
            data_to_template=parsed_json)
        with open(f'{ self.command }.html', 'w') as f:
            f.write(html_output)

    def markdown_file(self, parsed_json):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        markdown_template = env.get_template('md.j2')
        markdown_output = markdown_template.render(command = self.command,
            data_to_template=parsed_json)
        with open(f'{ self.command }.md', 'w') as f:
            f.write(markdown_output)

    def csv_file(self, parsed_json):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        csv_template = env.get_template('csv.j2')
        csv_output = csv_template.render(command = self.command,
            data_to_template=parsed_json)
        with open(f'{ self.command }.csv', 'w') as f:
            f.write(csv_output)

    def mindmap_file(self, parsed_json):
        template_dir = Path(__file__).resolve().parent
        env = Environment(loader=FileSystemLoader(str(template_dir)))
        mindmap_template = env.get_template('mindmap.j2')
        mindmap_output = mindmap_template.render(command = self.command,
            data_to_template=parsed_json)
        with open(f'{ self.command } mindmap.md', 'w') as f:
            f.write(mindmap_output)

    def all_files(self, parsed_json):
        self.json_file(parsed_json)
        self.yaml_file(parsed_json)
        self.html_file(parsed_json)
        self.markdown_file(parsed_json)
        self.csv_file(parsed_json)
        self.mindmap_file(parsed_json)

@click.command()
@click.option('--fileid',
    prompt='Hedera File ID',
    help=('A valid Hedera File ID'),
    required=True)
def cli(fileid):
    invoke_class = Network3Homer(fileid)
    invoke_class.network3_homer()

if __name__ == "__main__":
    cli()