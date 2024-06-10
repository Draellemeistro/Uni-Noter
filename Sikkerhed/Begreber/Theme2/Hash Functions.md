```table-of-contents
```


> [!NOTE] **[[Hash Functions]] (1975)**: Easy to compute but hard to invert
> - The **input** can be any string of **any size** 
> - It produces a **fixed-size output** 
> - It is **efficiently computable**
> 
> **Examples**: SHA-256, SHA-512, SHA-3

# How it works
**A hash function** H maps ==arbitrary strings of data== (**message**) to ==fixed-length output== (**hash value or message digest**). 
![[Pasted image 20240610190858.png]]
![[Pasted image 20240610190923.png]]

> [!important] **REMEMBER**
> - Hash functions **DO NOT** have a secret key.
> - The hash function H is **PUBLIC**, anyone can evaluate the function.
> - The function is *deterministic* and *public*, but the **MAPPING SHOULD LOOK "RANDOM'"**.
## Example
![[Pasted image 20240610195443.png]]
# Definition of Hashing
Sometimes referred to as **one-way encryption**
Hashing, or a Hashing Algorithm takes "something" (a message, a file, a certificate, computer code, anything) and turns into a smaller, representational sample of the original something, or a "fingerprint". The **result of a hashing algorithm is known as a Digest **(among other names).

![[Pasted image 20240212191024.png]]


To check if two files are perfectly identical, you can simply run them both through a hashing algorithm and compare the digests. If the digests are the same, then you know both files are also identical. In the rare cases that multiple files result in the same digest... you have what's known as a [[Collision]]. And while rare, collisions are unavoidable.

## Properties of Hashing
- It is **deterministic**: the same message always results in the same hash. A hash algorithm always gives an** output of identical size** regardless of the size of the input.
- It is **one-way**: It is quick to compute the hash value for any given message but on the other hand it is **infeasible to generate a message from its hash value** except by trying all possible messages
- It is **collision-free**: It is **infeasible to find two different messages with the same hash value**
- It has **avalanche effect**: A small change to a message should change the hash value so extensively that the new hash value appears **uncorrelated** with the old hash value
# Real world Hashing Algorithm requirements
## The three requirements for hashing algorithms
![[Pasted image 20240215144753.png]]

### Thought experiment
![[Pasted image 20240215145704.png]]
==**the first one, COLLISION RESISTANCE is easier to break, courtesy of the**== [[Birthday paradox]]
### 1: Collision Resistant
a
![[Pasted image 20240215144810.png]]

### 2: Pre-image resistant
s
![[Pasted image 20240215144826.png]]

### 3: second pre-image resistant
s 
![[Pasted image 20240215144839.png]]

## other requirements???? #TODO 
### Infeasible to produce a given digest
In the example of Hello getting hashed to 52, it would be quite easy to deduce other ways of getting that same digest. The number given to each letter is based on their placement in the alphabet. 
JEEBOO : 10+5+5+2+15+15 =52
### Impossible to extract the original message
can't reverse-engineer a digest
### Slight changes produces drastic differences
Resulting digest should produce no hints to what the original message is. Small changes to the message should not also produce small changes to the resulting digest. It should somehow look random
### Resulting digest is fixed width (length)
Whether you hash one letter, word or book, the resulting Digest should be the same size.
