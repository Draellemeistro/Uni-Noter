```c
int tls1_process_heartbeat (SSL *s) { 
	unsigned char *p = &s->s3 ->rrec. data [0] , *pl;
	unsigned int payload ; hbtype = *p++; 
	n2s(p, payload ); pl = p;
	
	if ( hbtype == TLS1_HB_REQUEST ) { 
		buffer = OPENSSL_malloc (1 + 2 + payload + padding ); 
		bp = buffer ; s2n( payload , bp ); 
		memcpy (bp , pl , payload ); 
		bp += payload; 
		r = ssl3_write_bytes (s, TLS1_RT_HEARTBEAT , buffer , 3 + payload + padding );
	}
}
```

> [!warning] Missing bound check for payload: Payload can be manipulated
> `unsigned char *p = &s->s3 ` ==->rrec. data [0]== ` , *pl;`
> `unsigned int payload;` 
> `hbtype = *p++;` 
> ==n2s(p, payload );==
> `if ( hbtype == TLS1_HB_REQUEST ) {` 
> 	`buffer = OPENSSL_malloc (1 + 2 + payload + padding );`
> 	`bp = buffer; `
> 	`s2n( payload , bp ); `
> 	==memcpy (bp , pl , payload );== 
> 	`bp += payload ;` 
> 	`r = ssl3_write_bytes (s, TLS1_RT_HEARTBEAT , buffer , 3 + payload + padding );`
> `} }`

## More details
This serious flaw (CVE-2014-0160) is a missing bounds check before a `memcpy()` call that uses non-sanitized user input as the length parameter. An attacker can trick OpenSSL into allocating a 64KB buffer, copy more bytes than is necessary into the buffer, send that buffer back, and thus leak the contents of the victim’s memory, 64KB at a time.
### The Fix
The patch in OpenSSL 1.0.1g is essentially a bounds check, using the correct record length in the SSL3 structure (`s3->rrec`) that described the incoming HeartbeatMessage.
Below is the revised code from [Github](https://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=731f431497f463f3a2a97236fe0187b11c44aead)

```
hbtype = *p++;
n2s(p, payload);
if (1 + 2 + payload + 16 > s->s3->rrec.length)
  return 0; /* silently discard per RFC 6520 sec. 4 */
pl = p;
```

### Impact of the Vulnerability
This vulnerability allows an attacker to extract memory contents from the webserver through the vulnerability in the heartbeat. As a result an attacker may be able to access sensitive information such as the private keys used for SSL/TLS.