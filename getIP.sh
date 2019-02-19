ip addr show wlp2s0 | grep 'inet ' | awk '{print $2}' | cut -f1 -d'/' > ip.txt
add ip.txt

git commit -m "Updated IP"

git push origin master