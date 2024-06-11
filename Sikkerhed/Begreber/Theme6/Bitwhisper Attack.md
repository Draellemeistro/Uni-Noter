

> [!question] What is Bitwhisper?
> **Covert Communication Through Thermal Channels**
> - A covert communication method for air-gapped computers.
> - Exploits thermal fluctuations to transmit data
> - requires no additional hardware
> 
> **Both the connected and air-gapped machines need to be infected with specially designed [[malware]]**

> [!example] How it Works:
> - One computer (*sender*) modulates CPU load to generate heat patterns
> - the other computer (*receiver*) monitors thermal sensors to detect patterns
> - Heat patterns encode data(*e.g., 0=cooler, 1=hotter*)

Even if the intended target isn't connected to the network directly, Information can be transmitted to or from it, through the use of bitwhisper. 

The internet-connected computer sitting nearby can monitor temperature fluctuations using its internal sensors and interpret them as a data stream. Commands can also be sent from the Internet side to the air-gapped system via heat.