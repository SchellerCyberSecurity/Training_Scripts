import toml
import os
import sys
import subprocess
import pathlib
import base64

# Variables

settings = pathlib.Path("settings.toml")

if settings.exists():
    # load settings.toml
    ovpn_config = toml.load('settings.toml')

    # set ovpn config files
    HTB = ovpn_config['OVPN']['HTB']
    HTB_Fortress = ovpn_config['OVPN']['HTB_Fortress']
    VHL = ovpn_config['OVPN']['VHL']
    PWK = ovpn_config['OVPN']['PWK']

    print('Please select which VPN configuration you would like to load.')
    print('[1] HTB')
    print('[2] HTB-Fortress')
    print('[3] VHL')
    print('[4] PWK')
    print('[x] Exit')
    selection = input('> ')
    if selection == '1':
        print('[+] Starting HTB VPN\n')
        subprocess.run(['openvpn', HTB])
    elif selection == '2':
        print('[+] Starting HTB Fortress VPN\n')
        subprocess.run(['openvpn', HTB_Fortress])
    elif selection == '3':
        print('[+] Starting VHL VPN\n')
        subprocess.run(["openvpn", VHL])
    elif selection == '4':
        print('[+] Starting PWK VPN\n')
        subprocess.run(["openvpn", PWK])
    elif selection == 'x' or 'X':
        sys.exit(0)
    else:
        print('Please select a valid option')
        sys.exit(1)
else:
    print('You must run setup.py first!')



