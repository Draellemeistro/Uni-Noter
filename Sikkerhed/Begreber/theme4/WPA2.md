# Wi-Fi Protected Access 2 (WPA2)

> [!NOTE] TLDR
> - Like **[[WPA]]**, but uses **[[AES]]**
> - **[[WPA]]** used ***RC4/TKIP* to remain compatible** for old hardware, but this is **not the case for *WPA2***

## Vulnerability / Attacking 

> [!warning] Attacking WPA2
> - Capture handshake
> - Perform offline **[[brute-force attack|brute-force]]**/**Dictionary attack** on the handshake
> - Recover the password!

### Play around with it ([[aircrack-ng]])
The only known way of recovering WPA2 passwords is to crack it by brute force.
```
aircrack-ng -w pass.lst -b <BSSID> <your_capture_file.cap>
```

**==Try to decrypt the traffic with Wireshark==**
https://wiki.wireshark.org/HowToDecrypt802.11 (**using the SSID and the password**)

#### Capture the Flag by cracking the wireless password
- Open the file **ctf.pcap** in wireshark. Your task if to find the flag.
	- The traffic is encrypted with **WPA2 password (wpa-pwd)**
	- The flag is known to be in the format HKNXXXXXXXX
- When you open the file, you can notice that the **traffic is encrypted**, so you cannot directly search for the flag. Thus, you are **expected to follow these steps**:
	- Identify the **SSID** which has the potential to contain the flag.
	- Try to crack the password by using the [[aircrack-ng]] tool
	-  Once you find the password, update the configuration of 802.11 protocol in **Wireshark**:
		- *Edit -> Preferences -> Protocols -> 802.11 -> Edit Decryption Keys -> OK*
		- If you notice that the traces didn’t change, reload (*View -> Reload*)
	- Do you notice now that the traces changed? Can you see the protocols?
	- Search for **tcp** protocol
	- ==**Search for string “HKN”**==
- 