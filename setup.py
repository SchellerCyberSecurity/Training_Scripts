#! /usr/bin/env python3
import itertools
import os
import base64
from getpass import getpass

import toml
expected_result = {}

# Variables

HTB_Primary = input('Please enter the full path to your primary HTB OVPN file\n> ')
HTB_Fortress = input('Please enter the full path to your HTB Fortress OVPN file\n> ')

VHL = input('Please enter the full path to your VHL OVPN file\n> ')
VHL_User = input('What is your VHL Username\n> ')
VHL_Pass = getpass('What is your VHL Pass\n> ')
VHL_Pass64 = base64.b64encode(bytes(VHL_Pass, 'latin-1'))

PWK = input('Please enter the full path to your PWK OVPN file\n> ')
PWK_User = input('What is your PWK Username\n> ')
PWK_Pass = getpass('What is your PWK Pass\n> ')
PWK_Pass64 = base64.b64encode(bytes(PWK_Pass, 'latin-1'))

def settings_file():
    """Temporarily write a settings file and return the filepath and the expected settings outcome."""
    with open("settings.toml", "w") as p:

        expected_result = {
            'OVPN': {
                'HTB': HTB_Primary,
                'HTB_Fortress': HTB_Fortress,
                'VHL': VHL,
                'VHL_User': VHL_User,
                'VHL_Pass': VHL_Pass64,
                'PWK': PWK,
                'PWK_User': PWK_User,
                'PWK_Pass': PWK_Pass64
            }
        }

        p.write(toml.dumps(expected_result))


    return str(p), expected_result



settings_file()
