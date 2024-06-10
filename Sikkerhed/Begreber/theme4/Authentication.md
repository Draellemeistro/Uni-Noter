# A solution for identity verification
- A process by which one entity **verifies the identity** of other entity
- Based on the possession of some **secret information**, like password or a secret key, known only to the entities participating in the authentication
- when an entity wants to authenticate another entity, the former will verify if the latter possesses the knowledge of the secret
- **1-way authentication** only one entity verifies the identity of the other party
- **mutual authentication** both communicating principals verify eacch others identities
# Symmetric authentication
- Uses a **single private key** to both encrypt and decrypt data
- in a symmetric cryptosystem, authentication protocols can be designed using the following principle:

> [!quote] **principle**
> ”***”if an entity can correctly encrypt a message using a key that the verifieer believes is known only to a principal with the claimed identity (outside of the verifier), this act constitutes sufficient proof of identity.”***


> [!example] TLDR
> - It is the **typical password authentication**.
> - However, to send this password, we need to make sure that the **communication channel is secured**.
> 	- To send the secret password, we need a **channel to be encrypted**.
> 	- It requires another secret, the encryption key to encrypt that session.
> 
> ![[Pasted image 20240608140710.png]]



## Basic protocol
- Based on shared secret: **key *K***
- **A** encryots a message **M** using the symmetric key **K** ands to **B**
- **B** encrypts the plaintext message using the symmetric key **K** to get the encrypted message
- if it is equal to the encrypted message sent by **A**, then **B** has authenticated **A**; else, the authentication fails
![[Pasted image 20240608135916.png]]
### ==Weakness==: Vulnerability to Replay attacks
- A valid signed message is copied and later re-sent
- An adversary could masquerade as **A** by recording the message **M** and **c** and later ==replaying== it to **B**
![[Pasted image 20240608140109.png]]
## Message Authentication Code [[MAC]]
- Allows for **Alice** and **Bob** to have data integrity, if they share a **secret key K**
- Given a message **M**, **Alice** computes $MAC=H(K || M)$, where **M'** is the received messaged
- **Alice** sends both **M** and **MAC** to **Bob**
- **Bob** $MAC'=H(K||M')$, where **M'** is the received message
- **Bob** checks **MAC** and **MAC'**: if same, then data integrity, else attack detected.
![[Pasted image 20240608140511.png]]
![[Pasted image 20240608140526.png]]


# Asymmetric Authentication (A.K.A. public-key based authentication)

> [!example] TLDR
> ![[Pasted image 20240608140835.png]]
> - Uses a **secret key (*private key*) and a *public key*** of an entity $A:PK_{A},SK_{A}$
> - Only **A** can generate $E_{SKA}(M)$ for any message **M** by signing it using $SK_A$
> - the signed message **c** ($c=E_{SKA}(M)$) can be verified by **any entity with the knowledge of $PK_A$** by $E_{PKA}(M)$


> [!NOTE] Design principle
> Authentication protocols can be constructed using the following design principle:
> **”*If an entity can correctly sign a message using the private key of the claimed identity, this act constitutes a sufficient proof of the identity*”**

## Basic Protocol (with *nonce*)
- To prevent replay attacks, we modify the protocol by adding a challenge-and response step using **nonce** (number used **once**)
	- ==A nonce ensures that old communications cannot be reused in replay attacks==
![[Pasted image 20240608141439.png]]

# How does Digital Signature guarantee Authenticity?
![[Pasted image 20240608141529.png]]
sssssss
ssssssss
ssssssss
## The fundamental problem: Man-in-the-middle attack
- Recall from previous lecture, the [[Man-ln-The-Middle (MITM)]] attack in [[Diffie Hellman]] (it does not use public key)
- In public key authentication, the [[Man-ln-The-Middle (MITM)]] attack is similar
- Because the ==public key is just data==, there is **no correlation** **between that piece of data and the identity of Alice.**
![[Pasted image 20240608141753.png]]
## Digital Signature and Real Identity

> [!NOTE] Problem
> ***There is still a problem linked to the “==real identity==” of the signer…***
> Why should I trust what the Sender claims to be?

# Public Key Infrastructure (PKI)

> [!NOTE] Analogy
> - **John** proves identity to the **DMV** by providing his passport, ...
> - DMV creates a driver's license that **John** can use to prove his identity
> - Although many people may not trust **John** to identify himself truthfully, they do trust the third party, the **DMV**
>   
> ![[Pasted image 20240608142001.png]]

- A **[[public key infrastructure (PKI)]]** provides all the components necessary for different types of users and entities to be able to communicate securely and in a predictable manner
- Designing and implementing a **PKI** boils down to **establishing a level of trust**
- in **PKI** enviroments, entities called **==Registration Authorities (RAs)==** and **==Certificate Authorities (CAs)==** provide services similar to those of the Department of Motor Vehicles (**DMV**)
-  **==consists of:==**
	- hardware,
	- applications,
	- policies,
	- services,
	- programming interfaces,
	- cryptographic algorithms,
	- protocols,
	- users,
	- utilities


> [!NOTE] When to use PKI?
> - **Use PKI if you do not automatically trust individuals** you do not know
> - Use a **trusted third party** to vouch for the other individual so confidence can be instilled and sensitive communication can take place
> - When a user trusts a **CA**, the user downloads that **CA's** *digital certificate* and public key and stores them on the local computer

## Registration and Certificate Authorities (RA and CA)

> [!NOTE] Third-party trust model:
> - **RA** requires proof of identity from the individual requesting a **digital certificate** and will validate this information
> 	- a **digital certificate** is a binding between an entity's **public key** and one or more attributes relating its identity
> - **RA** advises the **CA** to generate a *certificate*
> - **CA** digitally signs the *certificate* using its **private key**
> 	- this ensures that the *certificate* came from the **CA**

### Digital Certificates

> [!NOTE] TLDR
> - **A digital certificate binds an entity’s identity to a public key**
> 	- It contains information a receiver needs to be assured of the identity of the **public key owner**
> 	- it is created and formatted based on the **[[X509 standard]]**
> 		- Outlines necessary fields of a *certificate* and the possible values that can be inserted into the fields
> 		- A standard of *the International Telecommunication Union (**ITU**)*
> 	- The entity can be a person, a hardware component, a service, etc...

#### Certificates 

> [!NOTE] in Operating Systems (*Linux*)
>  ```
>  cd /etc/ssl/certs 
>  openssl x509 -in DigiCert_High_Assurance_EV_Root_CA.pem -noout -text
>  ```
>  ![[Pasted image 20240608144545.png]]


> [!NOTE] Certificates in Browsers (Try in Firefox)
> Most browsers have a list of CAs configured to be trusted by default, so when a user installs a new web browser, several of the most well- known and most trusted CA will be trusted without any change of settings
> - Go to URL: \about:prefences#privacy
> - Click View Certificates
> - Click Authorities


> [!example] Applications of Public Key Cryptography
> - **SSH keys:** (see: *GitHub*, *SSH in general*, etc.)
> - **Credit card verifications (chip cards)**


# Play around with it
**Setup SSH connection in Raspberry Pi 4**
- Set up **SSH** connection between your laptop and Raspberry Pi4 (**==Symmetric authentication using password==**)
- Set up **SSH key pairs** for automatic authentication (**==Asymmetric authentication==**)





