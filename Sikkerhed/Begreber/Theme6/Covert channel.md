See also **[[Channels]]**  and **[[Side channels]]**
> [!NOTE] What?
> **Covert channels are mechanisms used to transmit information using methods not originally intended for data transmission.**
> - Communicate publically
> - Not necessarily encrypted or protected
> - The goal is to avoid notice

# Covert Channels
## Human Nature and Flaws
- **Human vision is limited by physiology**
	- Limited spectrum of colors
	- No ultraviolet vision (*unaided*)
	- Limited visual distance
- **Hearing limitations**
	- Limited frequency capability (*20 Hz - 10 KHz*)
	- All other frequencies are considered infrasonic or ultrasonic (*outside our range*)
- **Selective attention**
	- When we focus on a particular thing, we tend to miss other things that are occurring at the same time
## Covert Storage Channel
- Involves a party that writes data to a storage location, and another party that reads it. 
- Exploits shared storage resources (hard drives, file systems, memory). 
- **How it works?** 
	- Sender manipulates storage in a pre-determined way (e.g., file sizes, timestamps). 
	- These manipulations encode data (like bits: 0 or 1). 
	- Receiver, knowing the method, interprets the changes as data.

## Covert Timing Channel
- An attacker might manipulate the timing of network traffic to transmit information. 
- For instance, subtly delaying packets by a certain amount could encode bits (longer delay = 1, shorter delay = 0). 
- This can be incredibly difficult to identify because network traffic naturally fluctuates.

## Looking at network/transport layer
- **A number of ways to induce covert channels exist:**
	- Unused header bits 
	- Optional header fields 
	- Use of existing header fields 
	- Modulating header fields 
	- Packet sequence timing 
	- Corrupt/lost/retransmitted messages 
	- And many more...
![[Pasted image 20240608182605.png]]
![[Pasted image 20240608182616.png]]

## What is a good covert channel?
- **It depends on what you want to use it for!**
- The performance will often be a trade-off between:
	- **Capacity (bandwidth)**
	- **Undetectability**
	- **Robustness**

## How can covert channels be detected?
- Communication with suspicious hosts/countries
- Use of optional header fields where not expected
- Looking for patterns….
	- Distribution of data in header fields
	- Lost, corrupt, retransmitted packets
- **Some techniques can also limit the use of covert channels, or making it even impossible:**
	- Normalising packet headers
	- Introducing random noise

## Example: [[Bitwhisper Attack]] - Covert Communication Through Thermal Channels
- **What is Bitwhisper?**
	- A covert communication method for air-gapped computers.
	- Exploits thermal fluctuations to transmit data
	- requires no additional hardware
- **How it Works:**
	- One computer (*sender*) modulates CPU load to generate heat patterns
	- the other computer (*receiver*) monitors thermal sensors to detect patterns
	- Heat patterns encode data(*e.g., 0=cooler, 1=hotter*)