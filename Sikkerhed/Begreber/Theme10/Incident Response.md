
> [!example] Incident
> **An incident** can be thought of as a **violation** or **imminent threat** of violation of computer security policies, acceptable use policies, or standard security practices.


> [!NOTE] Security Incident Response
> Security incident response is the **ability to detect and resolve problems** that threaten people, process, technology and facilities
> 
> Resolution of an incident through **an appropriate reaction to** and containment of the problem, constitutes **security incident response**.

# determining the type of Incident
- Malicious code attacks 
- Probes and network mapping 
- Unauthorized access 
- Denial of service (DOS) 
- Misuse 
- Intrusions 
- Data Loss or Leakage 
- System Misconfigurations 
- Social Engineering Attempts 
- Third-Party Vendor Incidents

# High-level incident response process
SE DEN HER: **[INCIDENT MANAGEMENT](https://www.ncsc.gov.uk/collection/incident-management/cyber-incident-response-processes)**
![[Pasted image 20240609003909.png]]
## Prepatory
- **Triage** Determine how **urgent** your response by understanding the **type** and **severity** of an incident
	- Assess impact
	- Categorise Incident
	- Assign incident manager
	- Check for false positive
	- Is legal input needed?
- **Escalate**
	- If required
	- Within IR Team or to CIO/CISO who may escalate further
- **Kick off response**
	- Who else needs to be involved?
	- IT, legal, HR, PR?
	- Consider internal AND external parties
- **Reporting**
	- Consider reporting and evidence capture requirements.
	- For example in the case of a data breach

## Core response
- **Incident Management** - as required throughout
- **Analyse**
	- Capture and analyse data/information
- **contain**/**mitigate**
	- Stop or lower the impact, prevent spread of the problems
	- Consider the potential impact of **all** actions
- **Remediate**/**Eradicate**
	- Fully remove/stop the incident
	- Confirm successful remediation
- **Recover**
	- Recover data and systems if needed.
	- resume '*business as usual*'
- **==resolved?==**
	- **review and Close down:** Document and assign improvements

# Incident Response Plan

> [!NOTE] A basic incident response plan should include:
> - Key contacts
> - Escalation criteria 
> - Basic flowchart or process 
> - At least one conference number: Alternative tools and communication means 
> - Basic guidance on legal or regulatory requirements 
> - External communication guidelines

# Incident management
**Encompasses a number of aspects, including**:
- Tracking, documenting, assigning and correlating all findings, tasks and communications.
- Arranging of regular update meetings or calls, and involvement of relevant teams
- Escalating serious incidents to senior management
- Ensuring the incident is communicated appropriately (to team, wider business, other stakeholders)
- Ensuring that the full incident lifecycle is covered from initial discovery through to close down.

## Triage 
Determine how **urgent** your response by understanding the **type** and **severity** of an incident

> [!NOTE] To determine Severity
> - **Confidentiality**: Has sensitive data been accessed, leaked or stolen? 
> - **Integrity**: Could data or systems have been altered? 
> - **Availability**: can authorized users access the system
### Escalation
The severity level will inform how quickly the incident needs to be handled and who it might need to be escalated to.
**Example:**
- A low priority incident --> handled by IT security team
- A high or critical severity incident --> goes up to CIO or board level

### Post incident review and close down: 
##### Lessons from the incident
- Are there security improvements which could have prevented the incident or enabled earlier detection?
- Consider both the tactical fixes that would have prevented or detected this incident as well as strategic solutions that may only be identifiable across multiple incidents.
- In particular, was there any information which would have significantly helped your response but which was difficult or impossible to obtain? Make a plan to gather this data ahead of any future attacks.
##### Lessons from the response
- Was the response successful and effective?
- Were there elements which could have been handled better?
- Was there data which could have been useful but wasn't available (For example, the right logs, or something that was overwritten early in the response
