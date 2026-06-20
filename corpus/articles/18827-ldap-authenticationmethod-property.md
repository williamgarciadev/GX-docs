---
title: "LDAP AuthenticationMethod Property"
source_id: 18827
source_url: https://wiki.genexus.com/commwiki/wiki?18827
genexus_version: "18"
---

# LDAP AuthenticationMethod Property

Details the authentication method to be used when using [LDAP data type](https://wiki.genexus.com/commwiki/wiki?6886).

### [Values](#Values)

|  |  |
| --- | --- |
| **Simple** | Use weak authentication (clear-text password). |
| **Anonymous** | [SASL Authentication](http://java.sun.com/products/jndi/tutorial/ldap/security/sasl.html); a space-separated list of SASL mechanism names. |
| **SASL** | NTLM authentication: the user and password are sent using the NTLM protocol. |

### [Examples](#Examples)

Set the 'simple' authentication method:

```
&LDAPVariable.AuthenticationMethod = "simple"
```

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Extended Data Types** | [LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886) |
| **Languages** | .NET, Java |

### [See Also](#See+Also)

[LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886)  
[LDAP](https://wiki.genexus.com/commwiki/wiki?6887)


|  |
| --- |
| **Backlinks** |
| [LDAPClient Data Type](https://wiki.genexus.com/commwiki/wiki?6886) |

---
