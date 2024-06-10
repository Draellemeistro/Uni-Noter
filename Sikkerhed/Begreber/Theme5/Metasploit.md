# 

> [!NOTE] What is Metasploitable?
> **Metasploitable** is an intentionally vulnerable Linux virtual machine
> 
> This VM can be used to conduct security training, test security tools, and practice common penetration testing techniques.
> 
> It can be used as a target for testing exploits with *Metasploit framework*.
> - **In this lecture, we will use [Metasploitable 2**](https://sourceforge.net/projects/metasploitable/)
> - Alternatively, you can use [Metasploitable 3](https://docs.rapid7.com/metasploit/setting-up-a-vulnerable-target/)


## Good to know
- It is highly recommended using a system that is capable of running **multiple virtual machines** to host your labs.
- We will need to have both **an attacking machine (Kali Linux)** and **a victim machine (Metasploitable 2 or 3)** as well as a **hypervisor** (e.g., VMware Player, VMware Workstation, Virtual Box, etc.) to run both in a safe and secluded network environment.
- More details on **how to setup the victim machine**: **[here](https://docs.rapid7.com/metasploit/setting-up-a-vulnerable-target)**
- A deliberately insecure web application: **[here](https://owasp.org/www-project-webgoat/)**


> [!warning] WARNING
> **• Never expose Metasploitable to an untrusted network, use NAT or Host-only mode!**

![[Pasted image 20240608165859.png]]
## Resources
- **Metasploit Tutorial for Beginners:** **[Here](https://nooblinux.com/metasploit-tutorial/)**
- **Metasploit Unleashed:** **[Here](https://www.offsec.com/metasploit-unleashed/introduction/)**
# The Metasploit Framework
- The Metasploit Framework provides the infrastructure, content and tools to perform penetration tests and extensive security audits
- Comprises reconnaissance, exploit development, payload packaging, and delivery of exploits to vulnerable systems
- It is open source and extendable
- Exploits can be easily shared amongst the community
- Available in Windows, UNIX, Linux, and Mac OSX. If you’re using Kali Linux, Metasploit is already preinstalled. See the *[Kali documentation](https://www.kali.org/docs/tools/starting-metasploit-framework-in-kali/)* for how to get started using Metasploit in Kali Linux.
## Architecture
![[Pasted image 20240608170155.png]]
### Terms
> [!example] Module
> - **A standalone piece of code or software that extends the functionality of the Metasploit Framework**
> 
> A module can be an exploit, escalation, scanner, or information gathering unit of code that interfaces with the framework to perform some operation.
> 
> It is like a discrete job that you would assign to a co-worker: “Exploit the FTP Server on Windows 2003” or “Find me a list of all credentials stored by Firefox on this server.”

> [!example] Session
> - **A session is a connection between a target and the machine running Metasploit**
> 
> Sessions allow for commands to be sent to and executed by the target machine.

#### Modules
- **Exploits**: Exploits are the code and commands that Metasploit uses to gain access.
- **Payloads**: Payloads are what are sent with the exploit to provide the attack a mechanism to interact with the exploited system.
- **Auxiliary**: The Auxiliary modules provide many useful tools including wireless attacks, denial of service, reconnaissance scanners, and SIP VoIP attacks.
- **NOPS**: *No OP*eration. NOPs keep the payload sizes consistent
- **Post-exploitation**: can be run on compromised targets to gather evidence, pivot deeper into a target network, etc.
- **Encoders**: are used to successfully remove unwanted bytes

# Starting Metasploit
1. **Start the PostgreSQL database for Metasploit**
2. **Launch Metasploit Framework Console**
```shell
# service postgresql start
# msfconsole
```

## Metasploit Core Commands
- msf > show exploits 
- msf > show payloads 
- msf > search Variable 
- msf > show options 
- msf > set Variable 
- msf > info 
- msf > exploit
![[Pasted image 20240608171026.png]]
## Metasploit Sample Operation
1. Open Metasploit Console 
2. Select Exploit 
3. Set Target 
4. Select Payload 
5. Set Options 
6. EXPLOIT!
![[Pasted image 20240608171113.png]]
