
> [!NOTE] **TLDR**
> Network scanning is a multifaceted process involving various techniques to uncover different aspects of network security. **Each type of scan provides unique insights, and often, multiple types of scanning are used together to create a comprehensive security assessment.** Understanding these different types and categories helps in effectively securing and managing networked environments.

Network scanning is a crucial aspect of network security and involves various techniques and tools to identify vulnerabilities, open ports, and active devices on a network. Here are the different types and categories of network scanning:

```table-of-contents
```
## Categories of Network Scanning
### Port Scanning
   - **Purpose**: Identifies open ports and services available on a networked device.
#### Types of Port Scans
   - **TCP Connect Scan**: Establishes a full TCP connection to check if ports are open.
   - **SYN Scan (Half-Open Scan)**: Sends SYN packets and waits for SYN-ACK responses without completing the handshake, stealthier than TCP Connect.
   - **UDP Scan**: Sends UDP packets to target ports to determine if they are open based on responses or lack thereof.
   - **ACK Scan**: Used to map out firewall rulesets by sending ACK packets.

### Vulnerability Scanning
   - **Purpose**: Identifies known vulnerabilities in network devices and software.
   - **Tools**: Typically performed using automated tools like Nessus, OpenVAS, or QualysGuard.

### Network Discovery Scanning
   - **Purpose**: Maps out devices and their connectivity on a network.
   - **Techniques**:
     - **Ping Sweep**: Sends ICMP Echo Requests to a range of IP addresses to determine which hosts are active.
     - **ARP Scan**: Identifies active devices on a local network by sending ARP requests.

### Operating System Detection
   - **Purpose**: Determines the operating system running on a networked device.
   - **Techniques**:
     - **TCP/IP Stack Fingerprinting**: Analyzes responses to specific TCP/IP packets to infer the OS.
     - **Banner Grabbing**: Connects to services and examines the responses or "banners" for OS details.

### Service Scanning
   - **Purpose**: Identifies running services on open ports and gathers information about them.
   - **Tools**: Tools like Nmap can probe services to gather detailed information.

### Wireless Network Scanning
   - **Purpose**: Identifies wireless networks, their security settings, and potential vulnerabilities.
   - **Techniques**:
     - **Passive Scanning**: Listens for wireless traffic to identify SSIDs, channels, and security settings.
     - **Active Scanning**: Sends probe requests to discover available wireless networks.

## Types of Scanning

### Active Scanning
   - **Description**: Involves sending packets to target devices and analyzing responses.
   - **Pros**: More accurate and detailed information.
   - **Cons**: Can be detected by security systems and may be intrusive.

### Passive Scanning
   - **Description**: Involves listening to network traffic without sending any probes.
   - **Pros**: Less likely to be detected, non-intrusive.
   - **Cons**: May provide less detailed information compared to active scanning.

### Stealth Scanning
   - **Description**: Techniques designed to avoid detection by firewalls and intrusion detection systems (IDS).
   - **Examples**:
     - **SYN Scan**: Sends SYN packets without completing the TCP handshake.
     - **FIN, Xmas, Null Scans**: Send unconventional packet flags to elicit responses from open ports without establishing a connection.

### Comprehensive Scanning
   - **Description**: Combines multiple scanning techniques to get a complete view of the network.
   - **Purpose**: Often used in security assessments and penetration testing to gather extensive information.

### External vs. Internal Scanning
   - **External Scanning**: Performed from outside the network perimeter to identify vulnerabilities exposed to the internet.
   - **Internal Scanning**: Conducted within the network to identify vulnerabilities accessible to internal users.

## Conclusion
Network scanning is a multifaceted process involving various techniques to uncover different aspects of network security. Each type of scan provides unique insights, and often, multiple types of scanning are used together to create a comprehensive security assessment. Understanding these different types and categories helps in effectively securing and managing networked environments.