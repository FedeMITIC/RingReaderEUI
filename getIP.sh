#!/bin/sh

REPO=/home/pi/Desktop/RingReaderEUI

case "$IFACE" in
    lo)
        # The loopback interface does not count.
        # only run when some other interface comes up
        exit 0
        ;;
    *)
        ;;
esac

cd $REPO

ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -f1 -d'/' > ip.txt
echo '\r\n' > ip.txt
ip addr show eth0 | grep 'inet ' | awk '{print $2}' | cut -f1 -d'/' > ip.txt

cat ip.txt

git add ip.txt

git commit -m "Updated IP"

git push origin master
