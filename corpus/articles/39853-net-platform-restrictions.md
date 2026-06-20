---
title: ".NET Platform restrictions"
source_id: 39853
source_url: https://wiki.genexus.com/commwiki/wiki?39853
genexus_version: "18"
---

# .NET Platform restrictions

This is a list of restrictions to take into account when producing .NET applications.

* .NET does not support Basic Authentication <https://stackoverflow.com/questions/35296648/basic-authentication-in-asp-net-core>.
* Support of [Cryptography data types](https://wiki.genexus.com/commwiki/wiki?22980) (CryptoHash, CryptoSign, CryptoSignXML, CryptoSymmetricEncrypt, CryptoAsymmetricEncrypt, CryptoCertifcate data types) is poor. Consider using the corresponding of the [GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) instead
  + eg.: [CryptoSign data type](https://wiki.genexus.com/commwiki/wiki?33458) with PKCS7 standard is not supported. Use [Asymmetric Signing](https://wiki.genexus.com/commwiki/wiki?42687) with PKCS8 instead.
* [WMI](https://wiki.genexus.com/commwiki/wiki?9244) (the equivalent of JMX in Java) is not available, because that is something specific to Windows and it is also being deprecated in the industry.
* GUI Reorganizations are not supported (nor the Show Prompt property for reorganizations), since both cases are Windows forms dialogs.
* Generation of Event Log entries for errors is not supported since Windows Event Viewer is specific to Windows.
* [SOAP native implementation](https://wiki.genexus.com/commwiki/wiki?13446) is not supported because of the low support of WFC and CoreWFC on the platform.
* GxConfig.exe tool that allows modifying database connection settings at web.config (when using .NET) is not supported since it is a Windows form dialog. As an alternative, you can use [GxEncryptCMD](https://wiki.genexus.com/commwiki/wiki?45615) to encrypt the desired values to be pasted into appsetting.json file.
* Logging to Trace.axd is not supported
* The GeneXus .Net generator does not support at the moment
  + the invocation of SAP BAPIs as RFC
  + deployment to AWS Elastic Beanstalk


|  |
| --- |
| **Backlinks** |
| [Table of contents:.NET Applications Development](https://wiki.genexus.com/commwiki/wiki?53971) | [.NET Generator Feature Support](https://wiki.genexus.com/commwiki/wiki?38607) | [Comparing the .NET generator with the .NET Framework generator](https://wiki.genexus.com/commwiki/wiki?45778) |
| [Comparing the .NET generator with the .NET Framework generator (GeneXus 18 Upgrade 9 or prior)](https://wiki.genexus.com/commwiki/wiki?58039) | [GeneXus .NET Generator - FAQ](https://wiki.genexus.com/commwiki/wiki?45833) |

---
