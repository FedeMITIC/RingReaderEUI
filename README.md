# RingReaderEUI

## Purpose

The purpose of this small project, developed for the CS-E4200 Emergent User Interfaces course at Aalto University, is to create a tool that allows blind people to read books and documents; this device, realized by my teammates (Xinyan Luo, Ling Sun) and me, comprises:
- a base where the user positions a document
- a camera, that grabs its picture
- headphones
- guides, to position the document and help users find the buttons
- buttons, to reproduce the help audio and read a new page
- a raspberry PI 4
The usage is straightforward:
- the user positions a document on the base, following the ad-hoc guides
- wears the headphones
- presses the start button
- waits a couple of seconds for the processing of the picture
- starts listening

The picture is processed through the Google OCR (Optical Character Recognition) APIs to extract the text; the text is spoken back to the users using a text synthetizer, provided by the Google TTS (Text To Speech).

### Additional resources

Demo video: https://drive.google.com/file/d/1DO_9yqXCI3ZUt28N1DBO-Wa7uD8-RLUO/view (Actress: Xinyan Luo, one of my teammates, Production: me)  
Report: https://github.com/FedeMITIC/RingReaderEUI/raw/master/docs/Emergent_User_Interface_Paper_Cinema%20For%20the%20Blind.pdf (Cinema For The Blind was the name of the group, not related to the actual concept :))

## Usage
Make sure all the dependencies are installed and up-to-date:
- picamera
- GPIO
- requests
- Google Cloud API (vision and texttospeech) for Python

API Keys must be created using the Google Tutorial: https://cloud.google.com/vision/docs/quickstart-client-libraries  
The main entry point is main.py script, in the src folder.  
A blueprint of the device is shown in Figure 2 of the report (Additional Resources - Report)  
A blueprint of the circuit is shown in Figure 3 of the report (Additional Resources - Report)

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
