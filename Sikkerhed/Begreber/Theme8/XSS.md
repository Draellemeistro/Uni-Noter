# Cross-site Scripting (XSS)

> [!example] In a nutshell
> **A link to an otherwise trustworthy page is used to execute malicious code**
> 
> - the original web page is modified and HTML/JavaScript code is injected into the page 
> - the client’s browser executes any code and renders any HTML present on the (vulnerable) page


> [!BUG] Dangers of it? with example (Se **[video](https://www.youtube.com/watch?v=ns1LX6mEvyM)**)
> - Browser doesn't scrutinize HTML received from server
> 	- It'll execute whatever it receives
> - Query is inside url (**if you send url to somebody, as soon as they go to it, it'll inject into their page**)
> - goal example (**document.cookie**, **session_ID**)
> 	- with session ID, you can log into the website as them
> - **solution**: sanitize don't directly inject text or such as HTML, but as text or similar


> [!warning] TLDR
> - **Target**: the users’ applications (not the server) 
> - **Goal**: unauthorized access to information stored on the client (browser) or unauthorized actions 
> - **Cause**: Lack of input sanitization

- A link to an otherwise trustworthy page is used to execute malicious code. It can, for example, be a link that looks like this: 
	- `http://legitamite-bank.com/index.php?user=<script>here is some bad code!</script>`
- Requires that you can get the user to click on the link! And that the page is vulnerable to XSS! 
- The malicious code can be used to install malware from another site or send data to another site (usernames, passwords, cookies).
![[Pasted image 20240608195101.png]]

## Persistent Cross-site Scripting (XSS)
Here, the malicious code is uploaded to a website, e.g., in a comment field.
![[Pasted image 20240608195128.png]]

> [!tip] A few insights
> - All the users that will visit the vulnerable resource will be victim of the attack
> - The injected code is not visible as a URL

