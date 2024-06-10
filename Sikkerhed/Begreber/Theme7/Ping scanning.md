# Internet Control Message Protocol (ICMP) – Ping scan
- **ICMP scanning is a method used to identify active hosts on a network.**
	- When a device receives an ICMP Echo Request (also known as a "ping"), it will respond with an ICMP Echo Reply
	- An ICMP scan sends out a series of ICMP Echo Requests to a range of IP addresses, and the scanner then listens for ICMP Echo Replies from any devices that respond.
	- By analyzing the responses, the scanner can determine which hosts are alive and available on the network.
- ICMP scanning is often used as a preliminary step in **network mapping** and **vulnerability assessment** because it provides information about the **==network's topology and the devices that are connected to it.==**
- ==However==, some devices may be configured to **ignore** ICMP requests, so ICMP scanning may not detect all hosts on the network.