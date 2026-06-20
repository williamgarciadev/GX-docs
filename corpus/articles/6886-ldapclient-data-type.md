---
title: "LDAPClient Data Type"
source_id: 6886
source_url: https://wiki.genexus.com/commwiki/wiki?6886
genexus_version: "18"
---

# LDAPClient Data Type

LDAPClient data type is a [GeneXus](https://wiki.genexus.com/commwiki/wiki?1756) type that allows connecting to [LDAP](https://wiki.genexus.com/commwiki/wiki?6887) servers. It can be used to authenticate users or retrieve attributes under a specified context.

#### [Properties](#Properties)

|  |
| --- |
| [LDAP AuthenticationMethod Property](https://wiki.genexus.com/commwiki/wiki?18827) |
| [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) |
| [Password property](https://wiki.genexus.com/commwiki/wiki?6994) |
| [Port Property](https://wiki.genexus.com/commwiki/wiki?5019) |
| [User Property](https://wiki.genexus.com/commwiki/wiki?7750,,) |
| [LDAP Secure Property](https://wiki.genexus.com/commwiki/wiki?18828) |

#### [Methods](#Methods)

|  |
| --- |
| [Connect method](https://wiki.genexus.com/commwiki/wiki?7086) |
| [Disconnect method](https://wiki.genexus.com/commwiki/wiki?7101) |
| GetAttribute |

#### [Connect](#Connect)

Creates the connection to the [LDAP](https://wiki.genexus.com/commwiki/wiki?6887) server at the specified host and port, using the specified authentication method. Optionally if the user and password are specified, they will be used to create the connection.

#### [Syntax](#Syntax)

```
&ret = &LDAPCliente.Connect()
```

**Returned Values**

Numeric: 1 means it successfully connected, 0 means it could not connect to the server.

**Example**

```
&ldapClient.Host = 'myServer' 
&ldapClient.Port = 389 
&ldapClient.AuthenticationMethod = 'simple' 
&ldapClient.User = 'myUser' 
&ldapClient.Password = 'myPassword' 
&ret = &ldapClient.Connect()
```

#### [Disconnect](#Disconnect)

Terminates the connection with the server.

**Syntax**

```
&LDAPClient.DisConnect()
```

#### [GetAttribute](#GetAttribute)

Through this method, the queues to the LDAP directory are achieved. It returns the values of the *AttName* attribute, which is defined by the *context* (related to the domain or one of its branches) and fulfills the filters set by *Properties*.

**Syntax**

```
&LDAPClient.GetAttribute( AttName, context, properties )
```

**Where**:  
*AttName*  
Is the name of the attribute

*context*  
Is a string

*properties*  
Properties data type.

Returns the values of the "AttName" attribute defined by a context and a set of attributes.

**Example**

&MatchAtts -> Properties data type

```
&MatchAtts .set("uid", "John") 
for &auxString in &ldapClient.GetAttribute("mail", "ou=People, o=myserver", &MatchAtts) 
   msg(&auxString) 
endfor
```

See [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?6889,,).

### [Considerations](#Considerations)

* Java: Information about SASL Authentication: <http://java.sun.com/products/jndi/tutorial/ldap/security/sasl.html>.
* Java: For information about LDAP Authentication, see: <http://java.sun.com/products/jndi/tutorial/ldap/security/auth.html>
* Java: To use the LDAPClient data type in Java, Sun Virtual Machine must be used.
* Java: Microsoft Virtual Machine does not have native support for it. However, it is possible to use LDAPClient (\*just authenticate users) with Microsoft VM, if JNDI 1.1.2 is downloaded (JNDI 1.1.2 Class Libraries, LDAP Service Provider, 1.0.3) (http://java.sun.com/products/jndi/downloads/index.html). After that, jndi.jar, ldap.jar, providerutil.jar must be added to the classpath. When using Microsoft VM, it is possible to authenticate users but it is not possible to retrieve attributes.
* When specifying a context (when retrieving attributes, for example) it is important to take into account that contexts are different depending on the directory tree structure and depending on the [LDAP](https://wiki.genexus.com/commwiki/wiki?6887). For example, when using Netscape Server a possible context could be:  
    
  uid = John, ou = People, dc = myCompany, dc = com  
    
  When using Active Directory an example could be:  
    
  cn = John, ou = Users , dc = myCompany, dc = com  
    
  So it is very important to know that the context being used matches the server's directory tree structure in order to get correct results.

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) |
| **Interfaces** | Web |


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) |
| [Host Property](https://wiki.genexus.com/commwiki/wiki?6999) | [LDAP](https://wiki.genexus.com/commwiki/wiki?6887) | [LDAP AuthenticationMethod Property](https://wiki.genexus.com/commwiki/wiki?18827) |
| [LDAP Secure Property](https://wiki.genexus.com/commwiki/wiki?18828) | [Password property](https://wiki.genexus.com/commwiki/wiki?6994) | [Port Property](https://wiki.genexus.com/commwiki/wiki?5019) |
| [Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606) | [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
|

---
