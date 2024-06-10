[Security theme 2 video](https://www.youtube.com/watch?v=HHQ2QP_upGM)
```table-of-contents
```


> [!quote] **For more info, see these:**
> - **[[Hash Functions]]**
> - **[[Collision]]**
> 	- [[Birthday paradox]]
> 	- [[the birthday attack]]
> - **[[Actual Hashing Algorithms]]**
> 	- [[MD (Message Digest)]]
> 	- [[SHA (Security Hash Algorithm)]]

# Overview
> [!NOTE] **[[Hash Functions]] (1975)**: Easy to compute but hard to invert
> - The **input** can be any string of **any size** 
> - It produces a **fixed-size output** 
> - It is **efficiently computable**
> 
> **Examples**: SHA-256, SHA-512, SHA-3
> 
> **==Hash values of at least 256 bits recommended to defend against brute-force attacks==**

> [!example] **Terms regarding Hashing**
> - **Digest**: The result of a hashing algorithm is known as a Digest.
> - **deterministic:** same message always results in the same hash. also *output of identical size*
> - **one-way:** infeasible to generate a message from its hash value
> - **collision-free:** infeasible to find two different messages with the same hash value
> - **avalanche effect:** small change to a message should change the hash value. New value should appear uncorrelated with old value

> [!info] The **three requirements** of hashing algorithms
> - **Collision Resistance**
> - **Pre-image resistance**
> - **Second pre-image resistance**


> [!NOTE] [[Hashing Overview|Hashing]] vs [[Encryption]]
> - **HASHING:** (==**NOT** REVERSIBLE==) Creates a unique "*fingerprint*" of the data. Changes to the data will result in a different hash, indicating tampering.
> 	- **purpose**: Data Integrity Check 
> 	- **usage**: Verifying file integrity, password storage
> 
>  - - - - - -
> - **ENCRYPTION:** (==REVERSIBLE==) Transforms data into an unreadable format using a key. Decryption requires the correct key.
> 	- **purpose**: Confidentiality
> 	- **usage**: Secure communication, protecting sensitive data

# use cases
- [[Password hashing]]
- **Passwords in DB**: store the hash of the password in the database table.
- **Digital signatures and Authentication**: message digests (hashes) are widely used to provide some assurance that a transferred file has arrived intact. E.g. **Github**
- **Blockchains and Cryptocoins**
	- ![[Pasted image 20240610200551.png]]
## why hashing?
- **It ensures data integrity**: If you know the hash of a message sent to you, you can hash the received message and compare the two
- **Store things for comparison without revealing them**
	![[Pasted image 20240215155328.png]]


## Example actual real-world Hashing Algorithms
- [[MD (Message Digest)]]
- [[SHA (Security Hash Algorithm)]]
# Hashing vs Encryption ([Video discussing just this](<[Hashing vs Encryption](https://www.youtube.com/watch?v=GI790E1JMgw)>))
![[Pasted image 20240215145106.png]]
## Properties of Hashing

- It is **deterministic**: the same message always results in the same hash. A hash algorithm always gives an **output of identical size** regardless of the size of the input.
- It is **one-way**: It is quick to compute the hash value for any given message but on the other hand it is **infeasible to generate a message from its hash value** except by trying all possible messages
- It is **collision-free**: It is **infeasible to find two different messages with the same hash value**
- It has **avalanche effect**: A small change to a message should change the hash value so extensively that the new hash value appears **uncorrelated** with the old hash value

### Digest
> [!NOTE] **other names**
> Checksum, Fingerprint, Hash, CRC

# Cryptographic Hash Functions 
## The three requirements for hashing algorithms

> [!warning] **Collision Resistance** (aka **strong collision resistance**):
> It is **VERY HARD** (computationally infeasible) to find a pair of plaintexts $M_1$ and $M_2$ such that $H(M_{1})=H(M_{2})$

> [!NOTE] **Pre-image resistance** (aka **one-way**)
> Given a hash value $P$, it is **VERY HARD** to find a plaintext $M$ such that $H(M)=P$

> [!success] **second pre-image resistant** (aka **weak collision resistance**)
> Given a plaintext $M_1$, it is **VERY HARD** to find a plaintext $M_2$ such that $H(M_{1})=H(M_{2})$

### 1: Collision Resistant
a
![[Pasted image 20240215144810.png]]

### 2: Pre-image resistant
s
![[Pasted image 20240215144826.png]]

### 3: second pre-image resistant
s 
![[Pasted image 20240215144839.png]]
