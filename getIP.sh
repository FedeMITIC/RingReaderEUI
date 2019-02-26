#!/bin/sh
ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -f1 -d'/' > ip.txt
echo '\r\n' > ip.txt
ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -f1 -d'/' > ip.txt

git commit ip.txt -m "Updated IP"

git push
