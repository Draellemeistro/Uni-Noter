# Theme 1: intro
## Assignment 1
**Choose one attack among the following:**
1. Mirai botnet
2. NotPetya attack
3. Stuxnet
**Then answer the questions:**
What was the target of the attack? Was it possible to prevent the attack, or was there something that could have been done to detect the attack more quickly and thus mitigate some of the consequences?
## Assignment 2
**Choose an Attack different from the ones mentioned in Assignment 1**
Describe the cyber attack that has occurred and create a 2-page essay covering:
- What happened?
- Who did it (or who you think did it)?
- What type of attack was involved?
- Which vulnerability was exploited and how it was possible to carry out the attack?
- How the attack could have been prevented?
- Your own reflections and thoughts about the attack.
- Other observations or comments you think are relevant.
# Theme 2: Hashing
## Assignment 1
In your favorite programming language, create a simple hash generator similar to the one shown in this figure
![[Pasted image 20240610230339.png]]
## Assignment 2
On Kali add a new user called **admin** and set an easy-to-guess password, e.g., **secret**  
- Using John the Ripper try to crack the user’s password using this wordlist: /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt

- Hint: Find the linux command to create a new user, and set its password.
# Theme 3: Encryption
## Assignment 1
 **Answer the following questions:** 
 **Question 1**: Assume the following scenario: A and B both have the knowledge of a secret key K (e.g. pre-shared). They communicate over an unsecure channel. Define a protocol (by writing down a message sequence chart) in which A and B use the pre-shared key K to mutually authenticate each other and to agree on a common session key (different from the long-term pre-shared key K). Try to keep the number of exchanged messages as low as possible.  
  
**Question 2**. Imagine that encryption is done by XORing a plain text with the same key (the length of the plaintext and the length of the key are the same). An attacker captures two cipher texts. What information it can derive from the captured packets?
## Assignment 2
**There is an encrypted message:**
0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104

This message has been XORed with a secret key.  
It is known that the format of the message is crypto{XXXXXXX} where the XXXXXXX is the unknown part of the message. Can you find the message?
  
**Hint**: If Plaintext XOR Key = Cipher then Cipher XOR Plaintext = Key  
Describe the steps of the solution. Write a small python script.
# Theme 4: Authentication & Wireless Security
## Assignment 1
**Capture the Flag by cracking the wireless password**
- Open the file ctf.pcap in wireshark. Your task if to find the flag. 
	- The traffic is encrypted with WPA2 password (wpa-pwd) 
	- The flag is known to be in the format HKNXXXXXXXX • 
- When you open the file, you can notice that the traffic is encrypted, so you cannot directly search for the flag. Thus, you are expected to follow this steps:
	- Identify the SSID which has the potential to contain the flag. 
	- Try to crack the password by using the aircrack-ng tool explained in the previous slide 
	- Once you find the password, update the configuration of 802.11 protocol in Wireshark Edit -> Preferences -> Protocols -> 802.11 -> Edit Decryption Keys -> OK 
	- If you notice that the traces didn’t change, reload View -> Reload 
	- Do you notice now that the traces changed? Can you see the protocols? 
	- Search for tcp protocol 
	- Search for string “HKN”
## Assignment 2
**Deauthentication Attack**
- Setup a hotspot connection
- Connect your laptop and your Virtual Machine to the hotspot 
- Perform Deauthentication attack in Virtual Machine to disconnect Wi-Fi in your laptop 

**(More details in moodle files: Sniffing WiFi Traffic and Deauthentication Attack)**
# Theme 5: Attack & Defense
## Assignment 1
**Exploiting Backdoor in vsftpd 2.3.4**
![[Pasted image 20240610230919.png]]
## Assignment 2
**Group work (10 min): SSH Brute Force Attack**
![[Pasted image 20240610230933.png]]

**Group work (10 min): How does an attacker use Back Channel?**
![[Pasted image 20240610231005.png]]

![[Pasted image 20240610231031.png]]
# Theme 6: Covert channels & Steganography
## Assignment 1
**Challenge #1**
Using **steghide** hide the file **secret.txt** into **earth_cover.jpg**. After that, remove the text file that was hidden.

**Challenge #2**
Using the files from Challenge #1 extract the secret file from the stego file.

**Challenge #3**
The image **earth_stego.jpg** has a secret file embedded inside it. Using **steghide** recover the file if the password is **barcelona**

**Challenge #4**
Check the solution of the previous challenge by calculating the SHA-256 hash of the file you’ve extracted.

The hash you should get is **bc2eec571b9b43e94b19e7a53286d2c7dcf6c5e00cdab86a3b741d20b79019dc**
## Assignment 2
**The task consists of 5 parts,**
**#1**
Give an overview of the most important concepts within covert channels and steganography. It is a large area, so you may limit yourself to what you have read about in the articles or if there is an area that you think is particularly interesting. (max one page).

**#2**
Identify and describe a scenario where either (1) confidential data must be protected to ensure it remains within an organization's network or (2) data related to malicious/illegal activity can be hidden in real data. It can either be an imagined scenario, a scenario you have heard about, or a scenario you, e.g., know from a work situation.

Please take this scenario as a starting point to answer the following questions in this assignment.

In the description, try to use some of the concepts that are introduced in the two articles you have read in connection with the theme here.

As I said, the first task here is to describe the scenario (you are welcome to draw and illustrate).

**#3**
Suppose you are a person with malicious intentions (insider or outsider). You would now like to get hold of the confidential information described in the previous question and get it out of the organization's network. Based on what you have read about covert channels and steganography, please describe at least three different methods that could be used to transfer this information.

**#4**
Identify which parameters are relevant to compare these methods.
Rate the different methods on a scale from 1 (poor) to 5 (excellent), and briefly justify your assessment.

**#5**
Assume that your task is to protect the confidential information in your organization. What precautions will you take to protect this data?
# Theme 7: Network monitoring and scanning
## Assignment 1
**==Note: The lab is only active until and including April 1st.==**
In this task, you must visit the virtual lab in Haaukins, which you will find at https://cct4.haaukins.com Register as a user. After this, it is necessary to solve the following:

1. Use **ifconfig** to find out which network you are on and which other machines could potentially be on the same network.
2. Use **nmap** to find other machines on the network. Try different types of scans and evaluate what information you get out of it vs. how long it takes to complete the scans.
3. Use **nmap** to find out which operating systems are running on the various machines in the lab.
4. Solve **Network Scanning**: Find a web server (the only web server that runs on port 8080, supports http, and has a flag on the front)?
5. Solve the **Heartbleed**
6. **Samba** - what is the version number?
7. Optional: WaterTank, SSHtay HYDRAted, etc.

Remember to document what you find, preferably with screenshots.
## Assignment 2
Read the article that belongs to the theme. Give a brief overview of the most important forms of TCP scanning, and advantages/disadvantages of the different types of scanning. It should preferably be short, 1-2 pages incl. drawings/tables.  

## Assignment 3
Solve at least 3 exercises from the slides of Part 2.

# Theme 8: Application security
## Assignment 1
Solve 5 of the Haaukins challenges in the topic "Web exploitations". You can write a report with the steps and screenshots.
![[Pasted image 20240610231638.png]]
## Assignment 2
Solve the Quiz of the Regular expressions in Slides 38-41.
# Theme 9: Risk Assessment
## Assignment 1
Write 1-2 page report about the case study in the slides.
## Assignment 2
Take as a starting point a company as described below, and make a short analysis (2-5 pages) of which cyber threats and challenges are the most significant in this new reality, and which measures you would recommend the company to take. Divide the measures into the short term (within a week), the medium term (within a month) and the long term (up to a year).

-0-0-0-0-0-0-0-0-0-0- **DEN HER** -0-0-0-0-0-0-0-0-0-0-0-0-
After Corona, the culture has changed in many companies, and many employees expect it to be possible to work from home - and "from home" in this context can mean anywhere in the world. At the same time, the situation in Ukraine means that the threat picture can change from day to day.

Take as a starting point a company as described below, and make a short analysis (2-5 pages) of which cyber threats and challenges are the most significant in this new reality, and which measures you would recommend the company to take. Divide the measures into the short term (within a week), the medium term (within a month) and the long term (up to a year).

About the company, do you know that:
- The company has approx. 100 employees.
- This is a manufacturing company.
- The company does not have a tradition of working from home, but after Corona has introduced that all administrative employees can now work from anywhere in the world. It is also possible to connect to the company from private devices.
- Part of the production can also be controlled via the Internet, as intelligent production lines have been installed
- The company has not had a tradition of thinking about security, as until now the entire system has been perceived as closed from the outside
- The systems are a mix of new and old, including some non-standardized legacy systems
- The company has branches in Denmark (management, design and production), the USA (marketing) and Ukraine (IT).
- Feel free to use some of the knowledge you have gained through the course here.

# Theme 10: Incident Response
## Assignment 1

## Assignment 2

