## Malicious USBs
As mentioned, USB-based attacks are seemingly on the rise, with security professionals mentioning an increased interest from nation-state actors. Much of the effectiveness that USB-based attacks enjoy, come from exploiting user trust and curiosity. 

There are quite a few options available to attackers wanting to abuse the USB stack. Of course there are the usual suspects like flash drives with malware on them or autorun exploits
Examples include malware-infected flash drives and keystroke injection devices. BadUSB, and programmable microcontrollers at large, emulate a trusted peripheral, while secretly executing malicious actions through firmware and driver vulnerabilities. There are also more forceful and directly destructive attacks like USBkill, which leverages electricity to damage the physical system through a high voltage surge.
The thing to note about programmable microcontrollers is their availability. Microcontrollers like Arduino or PiCO are very cheap and readily available. They can be easy to setup with many angles for attacks and concealment, giving them quite the potential for misuse.

Pictured are the USBkill, rubberducky, BashBunny, O.MG cable and the pico microcontroller. The last two effectively exemplify the breadth of options available, and the options for concealment.

## Malware Detection
There’s the classical Approach, most often using signatures of known malicious code patterns. VirusTotal: Compare results from multiple antivirus services. Good for malware checks, not designed for real-time protection or new / advanced 
Modern approaches leverage ML-based models to perform behavioral detection to Identify suspicious behavior and quarantine the files. May possibly recognize patterns and similarities, which otherwise wouldn’t be detected by typical rules or signature matches.

Can be implemented in different ways and areas.
Standard / static: Headers, patterns in bytes ………….
Dynamic: Anomaly detection, like odd API calls or network connections
Training a machine learning algorithm to detect malware
Many datasets with varying compositions of data. Easily highlighted by the amount of malware-families, and choice of benign inclusion. 
Also goes beyond, to how features are extracted from files and which features are available.
Example: Virus-MNIST takes inspiration from the classic MNIST dataset, and formats the binaries into images for use in computer vision
### Slide 2 & 3
Many datasets with varying compositions of data. Easily highlighted by the amount of malware-families, and choice of benign inclusion. 
Also goes beyond, to how features are extracted from files and which features are available.
Example: Virus-MNIST takes inspiration from the classic MNIST dataset, and formats the binaries into images for use in computer vision

## Cloud implementation – Containers
Offload to minikube cluser for scalability
Essentially, as is,
We wanted to try at setting up virtual machines in the cluster, which could also be leveraged for the possible implementation of dynamic testing. Also better isolation in theory.
Persistent Volumes could have been leveraged to store  potentially malicious files


## Future implementations
Datasets: Explore ways to improve detection capabilities. Choices in Feature selection depend alot on what kind of dataset is provided. through use of more diverse benign and malicious samples. Expanding the datasets to include more real world benign data and a broader range
of real-world malicious files could enhance the classification accuracy
NixOS: Since the nix device will interact with many potentially malicious devices, implementing the capability of automatic rebuilds after or before use could automate cleaning, and allow for the ability to configure how it should function. With remote building that process can be removed from the device
Checks: Light and efficient detection processes on-device would be suitable for real-time analysis, but could also help to filter out clear malignance without communication with the cloud.

