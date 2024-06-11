When discussing network scanning, it's important to understand the differences between TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) scans, as they use different methodologies and have distinct characteristics. Here’s a breakdown:

> [!NOTE] **TLDR**
> Understanding the differences between TCP and UDP scanning helps in effectively identifying network services and potential vulnerabilities. TCP scanning is generally more reliable and easier to interpret, while UDP scanning is essential for a complete view of network services but comes with additional challenges.

> [!question] **key differences**
> **TCP scanning** is generally more reliable and easier to interpret
> Easier to detect and log due to the connection establishment process.
> 
> **UDP scanning** is essential for a complete view of network services but comes with additional challenges.
> Harder to detect but can be slower and more prone to false positives and negatives.

# Key Differences Between TCP and UDP Scanning
1. **Reliability:**
   - **TCP**: More reliable due to the connection-oriented nature and the three-way handshake.
   - **UDP**: Less reliable because it is connectionless and does not guarantee packet delivery or order.
2. **Detection and Logging**:
   - **TCP**: Easier to detect and log due to the connection establishment process.
   - **UDP**: Harder to detect but can be slower and more prone to false positives and negatives.
3. **Use Cases**:
   - **TCP Scanning**: Ideal for identifying and mapping services that require a reliable connection (e.g., HTTP, SSH).
   - **UDP Scanning**: Necessary for discovering services that use UDP (e.g., DNS, SNMP), but often more challenging due to the nature of UDP communication.
4. **Speed and Efficiency**:
   - **TCP**: Typically faster per individual connection due to clear acknowledgment of open/closed status.
   - **UDP**: Can be slower overall as it relies on the absence of responses and potential ICMP messages, making it less straightforward.

## UDP Scanning

**2. UDP (User Datagram Protocol):**
- **Connectionless**: Does not establish a connection before data transfer, leading to faster but less reliable communication.
- **No Handshake**: Simply sends packets without any acknowledgment process.

**Common UDP Scanning Techniques:**
- **UDP Scan**:
  - **Method**: Sends a UDP packet to a target port. If the port is closed, an ICMP "port unreachable" message is typically returned. If no response is received, the port may be open or filtered.
  - **Pros**: Can identify services that do not use TCP.
  - **Cons**: Slower due to the need to wait for potential ICMP responses, often less reliable because open ports may not respond at all.

## TCP Scanning

**1. TCP (Transmission Control Protocol):**
- **Connection-Oriented**: Establishes a connection before data transfer, ensuring reliable communication.
- **Three-Way Handshake**: Utilizes a three-step process (SYN, SYN-ACK, ACK) to establish a connection.

**Common TCP Scanning Techniques:**
- **TCP Connect Scan**:
  - **Method**: Completes the three-way handshake (SYN, SYN-ACK, ACK) to determine if a port is open.
  - **Pros**: Accurate and straightforward.
  - **Cons**: Easily detectable and can be logged by firewalls and IDS.

- **SYN Scan (Half-Open Scan)**:
  - **Method**: Sends a SYN packet and waits for a SYN-ACK response, then sends an RST (reset) to close the connection without completing the handshake.
  - **Pros**: Stealthier than TCP Connect Scan, less likely to be logged.
  - **Cons**: Requires privileged access to send raw packets.

- **FIN Scan**:
  - **Method**: Sends a FIN packet to a port. Open ports generally do not respond, while closed ports send an RST.
  - **Pros**: Can bypass some firewalls and packet filters.
  - **Cons**: Less reliable on modern systems due to standardized responses.

- **Xmas Scan**:
  - **Method**: Sends a packet with the FIN, PSH, and URG flags set. Open ports typically do not respond, while closed ports send an RST.
  - **Pros**: Effective against older systems.
  - **Cons**: Easily detectable and less effective against modern firewalls.

- **Null Scan**:
  - **Method**: Sends a packet with no flags set. Similar response expectations as FIN and Xmas scans.
  - **Pros**: Simple and can be effective against older systems.
  - **Cons**: Not effective against modern systems.



