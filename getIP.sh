ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -f1 -d'/' > ip.txt

git add ip.txt

git commit -m "Updated IP"

git push origin master
