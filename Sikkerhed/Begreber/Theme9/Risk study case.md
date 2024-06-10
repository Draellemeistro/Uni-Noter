
> [!NOTE] Case details
> You are a risk manager in the Cyber Security Unit of a large financial institution. Executive management has asked the following:
> - **Is ransomware a top risk for our enterprise?**
> - **Should it be prioritized over other cyber security risks?**
> - **What investments should be done to mitigate the ransomware?**


## Considerations
- Our enterprise has several legacy systems. 
- The back-ups are not immutable, and they are stored in the same environment as the primary logs and data
- Business continuity and disaster recovery plans are made for recovery from IT Operational and physical incidents
- There is no secondary communication channels
- There is no “break the glass” procedure on several IAM and incident response toolsets.
## Hints

| Protect                      | Detect and Response                             | Recover                       |
| ---------------------------- | ----------------------------------------------- | ----------------------------- |
| Access Management (controls) | Incident Response Plan                          | Decrypting methods            |
| Security Configurations      | Playbooks                                       | Back-up restoration           |
| Patching                     | Threat Intelligence gathering                   | Hardware sanitization         |
| Endpoint protection          | Forensics                                       | Hardware replacement strategy |
| Email and web security       | Fall back solutions (break the glass solutions) |                               |
## Sources

| thing                                          | link                                                                                                                            |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Lockheed Martin, 2021: The Cyber Kill Chain    | [Cyber Kill Chain](https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html)                               |
| MITRE ATT&CK                                   | [Threat landscape for ransomware attacks](https://attack.mitre.org/)                                                            |
| ENISA Publications                             | [Landscape for Ramsomware Attacks](https://www.enisa.europa.eu/publications/enisa-threat-landscape-for-ransomware-attacks)      |
| Cybersecurity & Infrastructure Security Agency | [CISA](https://www.cisa.gov/)                                                                                                   |
| Delinea report                                 | [State of Ransomware](https://delinea.com/hubfs/Delinea/whitepapers/delinea-whitepaper-state-of-ransomware-2024-report.pdf)     |
| World Economic Forum                           | [3 tremds to drive cyberattacks and ransomware in 2024](https://www.weforum.org/agenda/2024/02/3-trends-ransomware-2024/)       |
| Sophos report                                  | [Sttate of ransomware 2023](https://assets.sophos.com/X24WTUEQ/at/c949g7693gsnjh9rb9gr8/sophos-state-of-ransomware-2023-wp.pdf) |
| Splunk article                                 | [Ransomware & Extortionware in 2024](https://www.splunk.com/en_us/blog/learn/ransomware-trends.html)                            |
