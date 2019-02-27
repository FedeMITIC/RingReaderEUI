# RingReaderEUI

### RaspberryPi info
```
Username: pi  
Password: EUI2019@aalto.fi
```

### How to connect
#### SSH
If you already have SSH in your system just type   
```
ssh 82.130.8.34 -l pi for Windows OSs
ssh pi@82.130.8.34    for MacOSs
```
The first time you will be asked to verify the authenticity of the host. The SHA256 fingerprint is as follows:  
```
SHA256:XzojhKDmyEifYtXhd5jG50Ym+ZX1CzZFMMUylQHhAL8
```
Verify that the fingerprint you get in the terminal and this one above are the same, then type `yes` to accept the connection.  
Finally insert the password to connect. (The password is in the section `Raspberry Pi info`

#### FTP
While SSH allows the user to execute remote commands, FTP is better to transfer files.
To connect with ftp use the **same address** of the SSH and port **22**.
The username and the password are the same.

### At the end of the project
Return to Shreyasi @ design factory.  

Items to be returned:
Raspberry PI 3 model B+  
Raspberry PI Charger  
Raspberry PI Camera  

### Notes
https://www.pyimagesearch.com/2017/07/10/using-tesseract-ocr-python/
