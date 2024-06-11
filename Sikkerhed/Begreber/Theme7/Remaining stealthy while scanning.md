

Performing stealthy network scanning aims to avoid detection by firewalls, intrusion detection systems (IDS), and intrusion prevention systems (IPS). Here are several techniques and best practices for conducting stealthy scans:

# Stealthy Scanning
> [!NOTE] **Conclusion**
> **Combine advanced scanning techniques with best practices to reduce the likelihood of detection while ensuring compliance and ethical conduct.**
> 
> Stealthy scanning requires a combination of advanced techniques and best practices to minimize detection. By leveraging SYN, FIN, Xmas, and Null scans, fragmentation, decoys, idle scanning, timing adjustments, and encryption, you can effectively reduce the chances of detection. Always ensure you have the necessary permissions and are compliant with applicable laws and regulations.
## TLDR
To perform stealthy network scanning and avoid detection by firewalls and intrusion detection systems, use these techniques:

1. **SYN Scan (Half-Open)**: Sends SYN, waits for SYN-ACK, then sends RST to avoid completing the handshake.
2. **FIN, Xmas, Null Scans**: Use unusual flag combinations to elicit responses without establishing a connection.
3. **Fragmentation**: Break packets into smaller pieces to evade detection.
4. **Decoy Scanning**: Spoof multiple IP addresses to obscure the true source.
5. **Idle Scan**: Use a third-party idle system (zombie) to send packets, hiding the real scanner.
6. **Timing and Throttling**: Slow down the scan rate to avoid triggering rate-based alarms.
7. **Randomizing IPs and Ports**: Scan non-sequentially to avoid pattern detection.
8. **Encrypted Tunnels**: Use VPNs or SSH tunnels to encrypt scan traffic and bypass deep packet inspection.
### Best Practices:
- **Reconnaissance**: Gather info passively.
- **Trusted Tools**: Use Nmap (`-sS`, `-sF`, `-sX`, `-sN`, `-D`, `-T0`, `-T1`) and Hping.
- **Monitor for Detection**: Test against your own systems.
- **Cover Tracks**: Ensure logs don’t reveal your activity.
- **Legal and Ethical**: Always have permission and comply with regulations.
### Summary:
Combine advanced scanning techniques with best practices to reduce the likelihood of detection while ensuring compliance and ethical conduct.

## Techniques for Stealthy Scanning
1. **SYN Scan (Half-Open Scan)**
   - **Description**: Sends a SYN packet and waits for a SYN-ACK response, then sends an RST packet to avoid completing the handshake.
   - **Stealth Benefit**: Less likely to be logged by the target system since the connection is not fully established.
2. **FIN, Xmas, and Null Scans**
   - **FIN Scan**: Sends a FIN packet. Open ports typically do not respond, while closed ports send an RST.
   - **Xmas Scan**: Sends a packet with FIN, PSH, and URG flags set. Similar response expectations as FIN scans.
   - **Null Scan**: Sends a packet with no flags set. Again, open ports typically do not respond.
   - **Stealth Benefit**: These scans exploit differences in how operating systems handle unexpected flag combinations, making them harder to detect by basic filtering mechanisms.
3. **Fragmentation**
   - **Description**: Breaks the scan packets into smaller fragments to bypass detection.
   - **Stealth Benefit**: Fragmented packets are less likely to be reassembled and detected by some IDS/IPS devices.
4. **Decoy Scanning**
   - **Description**: Spoofs the IP addresses of multiple decoys along with the actual scanning IP.
   - **Stealth Benefit**: Makes it difficult for the target system to determine the actual source of the scan.
5. **Idle Scan (Zombie Scan)**
   - **Description**: Uses a third-party, idle system (zombie) to send packets to the target, using the zombie's IP address.
   - **Stealth Benefit**: The real scanning system remains hidden, as the scan appears to come from the zombie.
6. **Timing and Throttling**
   - **Description**: Slows down the rate of sending scan packets.
   - **Stealth Benefit**: Reduces the likelihood of triggering rate-based IDS/IPS alarms by spacing out the scan over a longer period.
7. **Randomizing IP Addresses and Ports**
   - **Description**: Scans random IP addresses and ports instead of sequentially.
   - **Stealth Benefit**: Makes it harder for IDS/IPS to detect patterns and identify scanning behavior.
8. **Using Encrypted Tunnels**
   - **Description**: Uses VPNs or SSH tunnels to encrypt scan traffic.
   - **Stealth Benefit**: Encrypted traffic can evade deep packet inspection by IDS/IPS.

### Best Practices for Stealthy Scanning

1. **Reconnaissance**
   - **Passive Reconnaissance**: Gather as much information as possible without directly interacting with the target (e.g., using WHOIS, DNS queries, and public databases).

2. **Use Trusted Tools**
   - **Nmap**: Widely used and has options for stealth scanning (`-sS`, `-sF`, `-sX`, `-sN`, `-D`, `-T0`, `-T1`).
   - **Hping**: Customizable packet crafting tool useful for stealth scans.

3. **Monitor for Detection**
   - **Verify Stealth**: Run scans against your own systems to check if they are detected by IDS/IPS.
   - **Use Multiple Tools**: Different tools and techniques to avoid relying on a single method.

4. **Cover Tracks**
   - **Log Deletion**: If accessing systems, ensure logs do not show traces of your activity.
   - **Proxy Servers and VPNs**: Use to mask your actual IP address.

5. **Legal and Ethical Considerations**
   - **Authorization**: Ensure you have explicit permission to scan the network.
   - **Regulations**: Be aware of and comply with legal and regulatory requirements.

