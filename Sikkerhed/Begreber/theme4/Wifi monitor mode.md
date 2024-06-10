see also [[Sniffing WiFI Traffic]]
# Steps to enable monitor mode in your virtual machine.
1. Insert the USB wifi adapter in your host machine.
2. To use USB devices in VM, you need to install Virtual Box Extension Pack on your host OS (not on the guest OS). https://www.virtualbox.org/wiki/Downloads
3. After installing the extension pack you selected the VM, go to Settings -> USB -> add USB filter, and in the list, select the USB WiFi adapter and OK.
![[Pasted image 20240608162452.png]]
#### Common Issues
1. If the host OS runs Linux (you have installed Virtual Box on Linux) then you have to add the user that starts Virtual Box to the **vboxusers** ==group==.
2. **If network manager is not running:**
	1. systemctl stop NetworkManager
	2. systemctl start NetworkManager
#### Commands - WiFi Monitor Mode
```shell
########################## 
## WiFi Monitor Mode 
########################## 
# listing the wifi interface 
ifconfig -a 
iwconfig

# installing aircrack-ng 
apt update && apt install aircrack-ng 

# listing the processes that could interface with monitor mode 
airmon-ng check 
# killing the processes that could interface with monitor mode 
airmon-ng check kill 
# putting the interface into monitor mode 
airmon-ng start wlan0 
# -> new interface called wlan0mon is created 

# testing the mode of operation 
iwconfig

# disabling monitor mode (return to managed mode)
sudo airmon-ng stop wlan0mon 

#testing the mode of operation 
iwconfig
```

```shell
## 2nd method of putting the interface into monitor mode
ifconfig wlan0 down 
iwconfig wlan0 mode monitor 
ifconfig wlan0 up 

# testing the mode of operation 
iwconfig
```
# Let’s try Wifi monitor mode
#SecTodo ==More details in moodle file: **Wifi monitor mode**==
1. Start kali and log in
2. Plug in Wi-Fi adapter to your hosting machine
3. Enable monitor mode with "***airmon-ng***"
![[Pasted image 20240608160753.png]]