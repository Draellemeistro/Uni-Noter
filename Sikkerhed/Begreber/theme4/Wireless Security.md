
> [!example] TLDR
> - **==Why?:==** Wireless networking standards allow you to send network packets wirelessly
> - There are a variety of standards used for things like standard WiFi, cell network connections, low speed serial connections, etc.


> [!warning] BEWARE of
> - **Rogue access point** (a classic)
> 	- (*in this case*) combined with an **evil twin**
> 
> ![[Pasted image 20240608155608.png]]
> 
> *What can one use such a [[Man-ln-The-Middle (MITM)]] attack for?*
> - **Wireless Injection: [[Deauthentication Attack]]**
> 

# Wi-Fi: 802.11
- Wi-Fi makes use of the 802.11 standard
	- 802.11 is just the number assigned to the standard by the **IEEE**
- It can be seen as a **wireless form of Ethernet**
	- Packets are still addressed using the **MAC address**
- Normally, clients send and receive traffic from a wireless access point
- All data is transmitted using radio waves
- Different “flavors” of it use different frequencies and have different throughputs

## Terminology

> [!info] Terminology
> - Beacon
> - Channel
> - Basic Service Set Identifier (**BSSID**)
> - Access Point (**AP**)
> - Station (**STA**)
> - Service Set Identifier (**SSID**)

### Beacon
- It is broadcasted regularly by an AP to advertise its existence on a particular channel or channels
- includes SSID and other information needed by clients to connect to AP
### Channel
- Network path for wireless transmissions.
- Each Wi-Fi standard has numerous channels
### Basic Service Set Identifier (BSSID)
- MAC address of the access point
### Access Point (AP)
- A device that serves as a central wireless connection point for a Wi-Fi network.
- A device that all stations connect to.
### Station (STA)
- A client device that connects to the wireless network
### Service Set Identifier (SSID)
- Name of the wireless network
- *==example:==* AAU-1X, wifimodem9c29g, etc

## Typical 802.11 network
![[Pasted image 20240608150102.png]]
## WiFi Network Interaction
![[Pasted image 20240608150721.png]]
### Probe Request Frame
- This is the very first step of connection. The driver of the client searches for an **AP**.
- The client first sends a probe request on all channels to find the **AP**.
- then the **APs** in range answer with a **Probe response frame**.
- The client can also request for an *Access Point* (**AP**) using a specific **SSID**

### Authentication Frame
- Station requests to connect to *Access Point* (**AP**)
- if **WEP** encryption is used on the network, a cryptographic exchange occurs here to verify the station knows the correct key
- **AP** replies with yes or no

### Association Request Frame
- Station requests a full connection to the **AP**.
- **AP** connects station to network
- Station needs to have completed [[Authentication]]
- **WPA/WPA2** security mechanisms are verified after this

### Additional Frames
#### Control frames
- Controls a 802.11 connection
- Sent between the *Access Point* (**AP**) and *stations* (**STA**)
- not authenticated by default in any way
#### Beacon Frame
- Periodically broadcasted by *Access Point* (**AP**) to prospective *Stations* (**STA**)
- *Stations* (**STA**)  look for these frames to get list of available *Access Points* (**AP**)
#### Disassociation Frame
- Sent to terminate the connection
- similiar to a **FIN packet** in **TCP**

## Play around with it

> [!NOTE] Title
> The file **Exercise_1.cap** contains a capture of an *access point* (**AP**) without any clients.
> - Open the file and identify a ***Beacon Frame***
> - Determine the **SSID**, Channel number and **BSSID**

# Wi-Fi Security Options
- **Open**: Unencrypted and un-authenticated
- **Wired Equivalent Privacy ([[WEP]])**: Encrypted and authenticated but completely broken 
- **Wi-Fi Protected Acces ([[WPA]])**: Improved encryption (**TKIP**), authentication (pre-shared key or enterprise) 
- **Wi-Fi Protected Access2 ([[WPA2]])**: **[[AES]]** [[encryption]] 
- **[[WPA3]]**: in addition to **WPA2** security, **WPA3** provides protection against **[[brute-force attack|brute-force attacks]]** 
- 
