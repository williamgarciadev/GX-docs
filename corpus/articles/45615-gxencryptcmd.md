---
title: "GxEncryptCMD"
source_id: 45615
source_url: https://wiki.genexus.com/commwiki/wiki?45615
genexus_version: "18"
---

# GxEncryptCMD

GxEncryptCMD is a command-line tool that allows you to encrypt and decrypt strings using the same algorithms as GeneXus.

It's called GxEncryptCMD.exe and is located at the root folder of the GeneXus installation.

You can use it to change some of the encrypted data saved by GeneXus in your app configuration files, like web.config, client.cfg, appsettings.json, CloudServices.config, or GXCF\_Chatbots.config.

The syntax is as follows:

```
Usage: GxEncryptCMD /e|/d [/r] [/k:key] input

/e : Encrypt the input
/d : Decrypt the input
/k : Use this key for encryption/decryption
/r : Reverse the key (used for Java passwords)
input : Text to encrypt/decrypt
```

Just tell the tool whether you want to encrypt (/e) or decrypt (/d) a string, and add the string at the end.

By default, the tool will use GeneXus' default encryption keys. If you need to change that key, add a second parameter with the /k flag.

Keep in mind that if you change the encryption key, the same key must be used to decrypt the data.

### [Samples](#Samples)

Encrypt using GeneXus default key

```
C:\GeneXus>GxEncryptCMD.exe /e root
GxEncryptCMD 11.0.0.0
Copyright © 1988-2020 GeneXus. All Rights Reserved

lDhkEMO1isz7KuCQ4M358Q==
```

Decrypt using GeneXus default key

```
C:\GeneXus>GxEncryptCMD.exe /d lDhkEMO1isz7KuCQ4M358Q==
GxEncryptCMD 11.0.0.0
Copyright © 1988-2020 GeneXus. All Rights Reserved

root
```

Encrypt using an Application Encryption key

```
C:\GeneXus>GxEncryptCMD.exe /e /k:1A73A66F4A9C45358F4830E34C6807F5 root
GxEncryptCMD 11.0.0.0
Copyright © 1988-2020 GeneXus. All Rights Reserved

vkmzYmdujBpc+At9dUE+hg==
```

Decrypt using an Application Encryption key

```
C:\GeneXus>GxEncryptCMD.exe /d /k:1A73A66F4A9C45358F4830E34C6807F5 vkmzYmdujBpc+At9dUE+hg==
GxEncryptCMD 11.0.0.0
Copyright © 1988-2020 GeneXus. All Rights Reserved

root
```

**Notes**

* If you want to execute GxEncryptCMD.exe in another folder, you need to also bring the files: GxEncrypt.dll and if needed, the KeyResolver.dll or application.key which will be used to get the value of the Encryption key.


|  |
| --- |
| **Backlinks** |
| [.NET Platform restrictions](https://wiki.genexus.com/commwiki/wiki?39853) | [How to configure Session State In ASP.NET Core (GeneXus 18 Upgrade 3)](https://wiki.genexus.com/commwiki/wiki?54892) |
| [HowTo: Deploy a Workflow-based Application](https://wiki.genexus.com/commwiki/wiki?19848) |

---
