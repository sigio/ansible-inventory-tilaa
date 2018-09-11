#!/usr/bin/env python

# coding: utf-8

# Copyright (c) 2018 Cybersprint
# Copyright (c) 2018 Sig-I/O Automatisering
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with the software. If not, see <http://www.gnu.org/licenses/>.

'''a dynamic Ansible inventory source based on the Tilaa API'''

import argparse
import requests
import json
import os
import sys

user = os.environ['TILAA_USERNAME']
password = os.environ['TILAA_PASSWORD']

url = 'https://api.tilaa.com/v1/virtual_machines'

req = requests.get(url, auth=(user, password))

content = req.content
content = json.loads(content)
output = {}
names = []
networks = {}

for entry in content['virtual_machines']:
    names.append(entry['name'])

    networks[entry['name']] = {
            'ansible_host': entry['network'][0]['address'],
            'tilaa_vars': entry
        }

output['tilaa'] = names
output['_meta'] = {'hostvars': {}}

for n in names:
    output['_meta']['hostvars'] = networks


print(json.dumps(output))

