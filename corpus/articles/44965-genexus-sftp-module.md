---
title: "GeneXus SFTP Module"
source_id: 44965
source_url: https://wiki.genexus.com/commwiki/wiki?44965
genexus_version: "18"
---

# GeneXus SFTP Module

Warning! This module is not recommended for end-user public applications. Do not add this module to your application unless it is strictly necessary.

GeneXus SFTP Module is an independent module that implements the SSH File Transfer Protocol  - SFTP (aka Secure File Transfer Protocol) defined in [this draft](https://tools.ietf.org/html/draft-ietf-secsh-filexfer-13)

This module is based on [SSH.Net](https://github.com/sshnet/SSH.NET) implementation using fixes from [Neon.SSH.NET](https://doc.neonkube.com/Neon.SSH.NET-Overview.htm) to overcome Linux problems and bugs for .Net implementations and [Jsch](http://www.jcraft.com/jsch/) for Java implementation.

## [Detail](#Detail)

The module is organized in one folder containing the Sftp Client implementation and the SDT SftpOptions for connection configuration.

**Requires Net Framework >= 4.7**

**Requires dotnet SDK>=3.1 and 5.0 since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,)**

**Requieres dotnet SDK>= 6.0 since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,)**

## [Dependencies](#Dependencies)

GeneXus

* SecurityAPICommons Module

.Net

* [Neon.SSH.Net 1.0.4](https://www.nuget.org/packages/Neon.SSH.NET/1.0.4)

Java

* [JSch-0.1.55.jar](https://mvnrepository.com/artifact/com.jcraft/jsch/0.1.55)

## [Install](#Install)

You have to install **SecurityAPICommons and GeneXusSftp modules**using the [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172) dialog from the Knowledge Manager option (located in the GeneXus IDE toolbar).

## [Availability](#Availability)

[GeneXus 16 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?44913,,)

For Net Core is available since [GeneXus 16 Upgrade 9](https://wiki.genexus.com/commwiki/wiki?45275,,)

## [Scope](#Scope)

Java, .Net Framework and Net Core Web (server-side module)

## [SFTP in a nutshell](#SFTP+in+a+nutshell)

It is the FTP protocol but using SSH as a secure channel, and it also provides mutual authentication capabilities.

Therefore, it provides file access, file transfer, and file management over a reliable data stream provided by SSH.

It provides two authentication methods:

* With username and password - This method uses a username and password to authenticate to the server, which is the same username and password used to establish an SSH session.
* With a known pre-registered private key (recommended) - This method uses a given user's private key that is registered on the server to establish the SFTP channel. The user must also be added to the connection parameters.

Also, the protocol provides a way to use mutual authentication (the client identifies to the server and vice-versa) exchanging keys in the early stages of the connection intent. In this case, the user sends his credentials (username and password or username and private key), and the server sends to the client its key fingerprint that should match a known\_hosts file registry known by the client. This way, the client knows he is connecting to a known server and avoids man-in-the-middle type of attacks.

## [Security Tips](#Security+Tips)

Do not trust user inputs!!!

This module could have path manipulation vulnerabilities if not used carefully.

* This module does not sanitize paths or file names. Do not trust user inputs.
* This module allows you to upload to and download from the server any kind of file. Use a whitelist to filter file types.
* This module allows you to upload to and download from the server any directory on which the user has permissions. Fix/sanitize allowed paths and files.

Do not add this module to an application if it is not necessary.

Take security measures on deploy if external users are not allowed.


|  |
| --- |
| **Backlinks** |
| [Connection Options SFTP](https://wiki.genexus.com/commwiki/wiki?44967) | [File Extensions Whitelisting](https://wiki.genexus.com/commwiki/wiki?45554) |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) | [SFTP Client](https://wiki.genexus.com/commwiki/wiki?44966) |

---
