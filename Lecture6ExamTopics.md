# What is [[XSS]] and [[CSRF]]?
## [[XSS]]

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

#### What to achieve with it? (XSS)

#### What happens? (XSS)


## [[CSRF]]

> [!Example] TLDR
> - Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they are currently authenticated.
> - Avoided by correct authentication, so it is not enough to just send a request in a URL without further information from the server

> [!NOTE] Principles
> - Browser requests automatically include any credentials associated with the site 
> 	- user's session cookie, IP address, credentials... 
> - The attacker makes an authenticated user to submit a malicious, unintentional request 
> 	- This can happen from a different source (hostile website) 
> - If the user is currently authenticated, the site will have no way to distinguish between a legitimate and a forged request sent by the victim 
> 	- The attacker does not see anything...

#### What to achieve with it? (CSRF)

#### What happens? (CSRF)


## Similar but different


# What are [[cookies]]

### How attackers use cookies?

### Properties of cookies that can be misused?

# [[Buffer overflow Attack|Buffer overflow]]

> [!example] quick and dirty overview
> - **Buffer** is a contiguous memory associated with a variable. 
> - **Overflow of a buffer**: process tries to put/get more data in/from the buffer than it can hold. 
> 	- What can possibly go wrong? 
> - The C standard states that such process is undefined 
> - Compiler and OS protections can be applied to detect and prevent out-of-bound accesses 
> 	- but many compilers ignore these checks and assume the program is safe/just raise a warning
> 

### If you know what it is.?
### Know why it happens?

# [[Regular expressions (Regex)]]
### Mention reqular expressions?
### why used
### examples