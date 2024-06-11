More details about nmap **[here](https://nmap.org/book/man-briefoptions.html)** se også den [her](https://www.comparitech.com/net-admin/the-definitive-guide-to-nmap/)
![[Pasted image 20240611165823.png]]

> [!NOTE]
> **Use [[zenmap]] if you prefer the GUI**

![[Pasted image 20240611170028.png]]
## Nmap and UDP Scanning
Nmap will need sudo privileges to run a UDP scan to send custom packets.
```
sudo nmap -sU <target>
```
![[Pasted image 20240608191604.png]]

```
sudo nmap -sU –T4 –F <target>
```
![[Pasted image 20240608191632.png]]

## Nmap quiz

> [!QUESTION] What nmap option is used to scan all ports of a host?
> - -p-
> - -p0 
> - --all-ports

> [!QUESTION] What nmap option will perform a faster scan?
>  - -T2 
>  - -T3 
>  - -T4


> [!QUESTION] What nmap option does OS and version detection?
> - -sV
> - -A
> - -O


> [!QUESTION] What nmap option exports the scan results to a file?
> - -oN
> - -iL
> - --export


> [!question] What nmap option performs a ping scan?
> - -Pn
> - -sP
> - --scan-icmp


