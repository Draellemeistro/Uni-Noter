# Wired Equivalent Privacy (WEP)

> [!warning] WARNING!
> **NO LONGER SECURE!**
## Quick overview of its properties
### Encryption
- **WEP** encrypts data using a **shared key**. It uses **RC4 encryption protocol (==symmetric encryption==)**
- **Key sizes** were originally 40-bit but later increased to 104-bit for improved security. 
- **WEP** ==uses a single, static key to encrypt all traffic on the network==. This means the same key is used for all devices and all data transmissions.

### Authentication
- **Open System Authentication**: This method doesn't actually involve any authentication. Any device can attempt to connect to the network without providing any credentials.
- **Shared Key Authentication**: This method uses the **WEP** key for a handshake process to confirm the identity of the device trying to connect.

## WEP – an early standard for encryption at WiFi
- Authentication with ==**challenge-response** (using a shared key)==.
- Note **XOR operation**
- a single **shared key**...
- ==**Originally:** 40 bit key + 24 bit IV. (*later updated to 104 bit key*)==
![[Pasted image 20240608152746.png]]
![[Pasted image 20240608152753.png]]
### Discussion: WEP Confidentiality
- The value of **IV** will repeat (at least after $2^{24}$ frames)
- If an attacker has access to two fames with the same IV:
	- $C_{1}=P_{1}(XOR)RC_{4}(IV_{1},k)$
	- $C_{2}=P_{2}(XOR)RC_{4}(IV_{1},k$
	- $C_{1}(XOR)C_{2}=$ 
		- $=[P_{1}(XOR)RC_{4}(IV_{1},k)]$ $(XOR)$ $[P_{2}(XOR)RC_{4}(IV_{1},k)]$
		- $=P_{1}(XOR)P_{2}(XOR)RC_{4}(IV_{1},k)(XOR)RC_{4}(IV_{1},k)$
		- $=P_{1}(XOR)P_{2}$
	- **==This implies that the attacker knows the *XOR* of the two plaintexts==**
- If the attacker **knows just one pair P1,C1** (==*known plaintext attack*==), **then he can decrypt any frame with that IV.**
- ![[Pasted image 20240608153758.png]]

