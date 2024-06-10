

## Capturing WiFi Packets Using *airodump-ng*
```shell
########################## 
## Capturing WiFi Packets Using airodump-ng 
########################## 
# installing aircrack-ng 
sudo apt install aircrack-ng 

# displaying the help 
airodump-ng --help 

## TO CAPTURE ALL WIFI TRAFFIC THE INTERFACE SHOULD BE PUT INTO MONITOR MODE 
 
# sniffing all wifi traffic in the range/air (on the medium) 
airodump-ng -i wlan0mon 
 
# sniffing all wifi traffic on a specific channel (ex: 1) 
airodump-ng -i wlan0mon -c 1 
 
# sniffing all wifi traffic on a specific channel (ex: 1) of a specific wifi network 
airodump-ng -i wlan0mon -c 1 --bssid 34:2C:C4:93:45:97 # -> bssid is MAC of the AP
 
# writing to a file 
airodump-ng -i wlan0mon -c 1 --bssid 34:2C:C4:93:45:97 -w dump
```
