---
title: "GeneXus FTPS Module"
source_id: 45274
source_url: https://wiki.genexus.com/commwiki/wiki?45274
genexus_version: "18"
---

# GeneXus FTPS Module

Warning! This module is not recommended for end-user public applications. Do not add this module to your application unless it is strictly necessary.

GeneXus FTPS Module is an independent module that implements the File Transfer Protocol over SSL  - FTPS (also known as FTPES, FTP-SSL & FTP Secure) including support for TLS.

This module is based on [FluentFTP](https://github.com/robinrodricks/FluentFTP) for .Net implementations and [Apache Commons Net](https://commons.apache.org/proper/commons-net/) for Java implementation.

## [Detail](#Detail)

The module is organized in one folder containing the Ftps Client implementation and the SDT FtpsOptions for connection configuration.

## [Dependencies](#Dependencies)

GeneXus

* SecurityAPICommons Module

.Net & .NET Core

Requires .Net Framework 4.7 since [GeneXus 17 upgrade 1](https://wiki.genexus.com/commwiki/wiki?46852,,)

Requires dotnet SDK>=3.1 and 5.0 since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,)

Requieres dotnet SDK>= 6.0 since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,)

* [FluentFTP 31.3.2](https://www.nuget.org/packages/FluentFTP/)

Java

* [commons-net-3.3.jar](https://mvnrepository.com/artifact/commons-net/commons-net/3.3)
* [commons-net-3.9.0.jar](https://mvnrepository.com/artifact/commons-net/commons-net/3.9.0) since [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396)

## [Install](#Install)

Install **SecurityAPICommons and GeneXusFtps modules**using the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog from the Knowledge Manager option (located in the GeneXus IDE toolbar).

## [Scope](#Scope)

Java, .Net Framework, and Net Core Web (server-side module)

## [FTPS in a nutshell](#FTPS+in+a+nutshell)

It is the FTP protocol but using TLS/SSL to secure the channel, and uses typical FTP authentication capabilities.

Therefore, it provides file access, file transfer, and file management over a reliable data stream provided by TLS/SSL.

There are 2 modes of negotiation: Implicit and explicit.

* On implicit mode, it typically uses the 990 port and establishes an encrypted connection only.
* The explicit mode allows the client to manage the connection encryption. In cases where the file contents are not sensitive, it could be used to encrypt the authentication and not the file transfer. Force encryption flags could be used to maintain the channel's encryption after authentication. It involves other mechanisms to challenge server encryption algorithms.

## [Security Tips](#Security+Tips)

Do not trust user inputs!!!

This module could have path manipulation vulnerabilities if not used carefully.

* This module does not sanitize paths or file names. Do not trust user inputs.
* This module allows you to upload to and download from the server any kind of file. Use a whitelist to filter file types.
* This module allows you to upload to and download from the server any directory on which the user has permissions. Fix/sanitize allowed paths and files.

Do not add this module to an application if it is not necessary.

Take security measures on deployment if external users are not allowed.

### [Availability](#Availability)

This feature is available since [GeneXus 16 upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,).


|  |
| --- |
| **Backlinks** |
| [Connection Options FTPS](https://wiki.genexus.com/commwiki/wiki?45278) | [File Extensions Whitelisting](https://wiki.genexus.com/commwiki/wiki?45554) | [FTPS Client](https://wiki.genexus.com/commwiki/wiki?45277) |
| [FTPS Domains](https://wiki.genexus.com/commwiki/wiki?45276) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
