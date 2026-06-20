---
title: "Application Encryption Key property"
source_id: 36909
source_url: https://wiki.genexus.com/commwiki/wiki?36909
genexus_version: "18"
---

# Application Encryption Key property

Indicates the encryption key used to encrypt sensitive data stored in configuration files.

### [Scope](#Scope)

**Level:** Deploy Target Options

### [Description](#Description)

The Application Encryption Key is used to encrypt and decrypt sensitive data of the database connection strings and URL parameters.

Its length has to be 32, 48, or 64 characters (Hexa is expected) and it's typically a GUID. By default, the length is 64 characters.

In Java, the key is stored in a file named application.key, in the folder where the client.cfg is located. Its content is as follows: 7E2E22D26FF2989E2444852A85E57866  
7E2E22D26FF2989E2444852A85E57866

The first line contains the key related to database connection information and parameter encryption used when the Encrypt URL Parameters property is set to 'Session key'.

The second line contains the key related to URL Parameter encryption used when the Encrypt URL Parameters property is set to 'Site key'.

**.NET-specific**

In .NET, the Application Deployment Tool creates a KeyResolver.dll with those keys (To encrypt the URL with a different key, follow the steps of [SAC 29874](https://www.genexus.com/developers/websac?,,,29874)).

In both .NET and Java, the Application Deployment Tool creates the files and encrypts the database connection information before packaging the application.

### [Considerations](#Considerations)

If you change the property value and deploy again, will need to clean the browser cache otherwise the Invalid key error may occur:

```
# Java
Caused by: com.genexus.util.Encryption$InvalidGXKeyException: Invalid key
    at com.genexus.util.Encryption.encrypt64(Encryption.java:69)
    at com.genexus.util.Encryption.uriencrypt64(Encryption.java:5
# .Net
Exception: Invalid key
   GeneXus.Encryption.CryptoImpl.Encrypt64(String value, String key)
   GeneXus.Http.GXHttpHandler.Encrypt64(String value, String key)
   GeneXus.Http.GXHttpHandler.GetEncryptedHash(String value, String key)
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [Encrypt URL parameters property](https://wiki.genexus.com/commwiki/wiki?8068) |

---
