---
title: "LDAP Secure Property"
source_id: 18828
source_url: https://wiki.genexus.com/commwiki/wiki?18828
genexus_version: "18"
---

# LDAP Secure Property

Sets or gets if [LDAP](https://wiki.genexus.com/commwiki/wiki?6887) authentication uses a secure (HTTPS) or unsecure (HTTP) protocol.

### [Values](#Values)

|  |  |
| --- | --- |
| **0** | Unsecure (HTTP) protocol is used. This is the default value. |
| **1** | Secure (HTTPS) protocol is used. |

### [Example](#Example)

Set protocol to be secure.

```
&LDAPVariable.Secure = 1
```

### [Scope](#Scope)

**Extended Data Types:**[LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886)  
**Generators:** .NET, Java

### [Java Notes](#Java+Notes)

Make sure to import and add the server certificate in a [Keystore](https://wiki.genexus.com/commwiki/wiki?4443,,) file. The application server must reference the associated keystore and password; set the following properties in the application server:

```
-Djavax.net.ssl.trustStore=/tmp/keystoresample
-Djavax.net.ssl.trustStorePassword=MyPassword
```

### [See Also](#See+Also)

[LDAP Data Type](https://wiki.genexus.com/commwiki/wiki?6886)  
[Authentication using LDAP](http://tldp.org/HOWTO/LDAP-HOWTO/authentication.html)


|  |
| --- |
| **Backlinks** |
| [LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886) |

---
