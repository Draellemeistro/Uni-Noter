
> [!NOTE] Definition
> **Steganography** is the practice of concealing a file, message, image, or video within another file, message, image, or video. 
> 
> The word steganography combines the Greek words steganos (*στεγανός*), meaning **"covered, concealed, or protected"**, and *graphein* (*γράφειν*) meaning **"writing”**
> 
> **==Very old technique: 5tth century BC==**

> [!question] What for?
> **Steganography tools can embed secret files into images, movies, audio files or other file formats.**
> - Sending encrypted messages without raising suspicion, such as in countries where free speech is suppressed.
> - Digital watermark of the copyright holder
> - Hiding or transporting secret information (secret documents, Bitcoin private key etc)
> - Transporting sensitive data from point A to point B such that the transfer of the data is unknown.

> [!important] What kind of media can be used?
> Basically all kind of files, where information can be hidden (e.g., in metadata or unused fields of data):
> - Digital media (audio, video, pictures)
> - Text
> - Device resources (e.g., CPU load)
> - Computer network protocols
> 
> It is important to be aware **that some of these files can be changed/processed**, for example:
> - Pictures uploaded to social media can be compressed
> - IP headers might get normalized
# Steganography vs Encryption
- **[[encryption]]**
	- Even when the encryption is secure, **it does NOT hide the existence of the message**
	- **Anyone can see that an encrypted message** has been sent and even though no one can read it merely communicating a secret can trigger alarms and make others suspicious.
- **Steganography**
	- *==The purpose of steganography is to hide even the mere existence of the message that is being stored.==*

# How Steganography really works
1. The secret file is encrypted.
	1. This is not mandatory but this highly recommended and main steganography tools do that automatically for you.
	2. The file that is hidden is called ***“embedded file”***
2. The secret file (encrypted or in clear text) is embedded into a **cover file** according to a steganographic algorithm.
	1. The steganography algorithm decides how to hide data and how to randomize the placement of the data.
	2. The cover file that contains the script the message or the embedded file is called ***“stego file”***.
3. The stego file is sent normally (in clear-text or encrypted) to the destination or is made public to be easily reached.
![[Pasted image 20240608180342.png]]

## Example: bitmap pictures
- In a bitmap picture, each bit is represented as: (r,g,b,a), each having a value 0-255. r=Red, g=Green, b=Blue, a=Alpha channel
- However, small variations are hard/impossible to see by the human eye. For example if b=120 or 121.
- If we want to encode a byte of text we can do it by using the last bit of each color.

> [!NOTE] Example
> Let's write to the RGB code of color orange!
> Color **orange** = RGB(255,153, 0) or in binary:
> ```
> (11111111, 10011001, 00000000) -> embedding 1, 0, 1 -> (11111111, 10011000, 00000001
> ```

## Using Steganography: [[steghide tool]]
#### Challenge 1
Using **steghide** hide the file **secret.txt** into **earth_cover.jpg**. After that, remove the text file that was hidden
```shell
steghide embed –ef secret.txt –cf earth_cover.jpg
```

#### Challenge 2
Using the files from Challenge #1 extract the secret file from the stego file.

#### Challenge 3
The image **earth_stego.jpg** has a secret file embedded inside it. Using **steghide** recover the file if the password is **barcelona**
#### Challenge 4
Check the solution of the previous challenge by calculating the SHA-256 hash of the file you’ve extracted.

==The hash you should get is== **bc2eec571b9b43e94b19e7a53286d2c7dcf6c5e00cdab86a3b741d20b79019dc**

