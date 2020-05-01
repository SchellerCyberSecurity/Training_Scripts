#! /bin/bash

echo "Which VPN would you like to active?"
echo "[1] HTB Original"
echo "[2] HTB Fortress"
read -p "> " vpn

if [ $vpn = 1 ]
then
	# Set your OVPN file for HTB standarad here
	openvpn /htb/ovpn/file
elif [ $vpn = 2 ]
then
	# Set your OVPN file for HTB fortress here
	openvpn /htb/fortress/file
else
	echo Please choose 1 or 2
fi
