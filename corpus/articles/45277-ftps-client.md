---
title: "FTPS Client"
source_id: 45277
source_url: https://wiki.genexus.com/commwiki/wiki?45277
genexus_version: "18"
---

# FTPS Client

**Note**: this is part of [GeneXus FTPS Module](https://wiki.genexus.com/commwiki/wiki?45274) and implements a restricted client for the FTPS Protocol.

## [Connect](#Connect)

It establishes the SSL/TLS connection to the server using the authentication parameters defined on the SDT FtpsOptions.

```
Connect(FtpsOptions)
```

* Input FtpsOptions: SDT FtpsOptions with authentication configuration preloaded
* Returns: Boolean true if the connection was successful.

Example:

```
&success = &FtpsClient.Connect(&FtpsOptions)
```

## [Get](#Get)

Downloads a file from the remote FTPS server to the client's machine using an already open connection.

```
Get(remoteFilePath, localDirectory)
```

* Input remoteFilePath: VarChar(9999), path relative to the working directory (pwd) including filename and extension.
* Input localDirectory: VarChar(9999), an absolute local path to save the downloaded file.
* Returns: Boolean true if the operation was successful.

Example:

```
&success = &FtpsClient.Get("/ftpsfolder/samplefile.txt", "C:\Temp\")
```

## [Put](#Put)

Uploads a file from the local client's machine to the FTPS server using an already open connection.

```
Put(localFilePath, remoteDirectory)
```

* Input localFilePath - VarChar(9999), absolute local path to the file including filename and extension.
* Input remoteDirectory - VarChar(9999), a path relative to the working directory (pwd).
* Returns: Boolean true if the operation was successful.

Example.

```
&success = &FtpsClient.Put("C:\Temp\samplefile.txt", "/ftpsfolder")
```

## [GetWorkingDirectory](#GetWorkingDirectory)

Returns the default remote server working directory (command pwd).

```
GetWorkingDirectory()
```

* Returns VarChar(9999)

Example:

```
&directory = &FtpsClient.GetWorkingDirectory()
```

## [Disconnect](#Disconnect)

Closes the FTPS connection.

It is mandatory as good programming practice after finishing using the channel and as a security measure.

```
Disconnect()
```

* It does not receive any parameters and does not return any value.

Example

```
&FtpsClient.Disconnect()
```

## [Rm](#Rm)

This method is available since [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396)

Remove/delete a file from the remote FTPS server using an already open connection.

```
Rm(remoteFilePath)
```

* Input remoteFilePath: VarChar(9999), path relative to the working directory (pwd) including filename and extension.
* Returns: Boolean true if the operation was successful.

Example:

```
&success = &FtpsClient.Rm("/ftpsfolder/samplefile.txt")
```

## [How to Download a File](#How+to+Download+a+File)

```
&FtpsOptions.Host = "172.16.4.5"
&FtpsOptions.User = "dummyuser"
&FtpsOptions.Port = 21
&FtpsOptions.Password = "dummypass"
&FtpsOptions.ForceEncryption = true 
&FtpsOptions.ConnectionMode = FtpConnectionMode.PASSIVE 
&FtpsOptions.EncryptionMode = FtpEncryptionMode.EXPLICIT 
&FtpsOptions.Protocol = FtpsProtocol.TLS1_2 
&FtpsOptions.TrustStorePath = "C:\cacerts\truststore.pkcs12" 
&FtpsOptions.Encoding = FtpEncoding.BINARY

&success = &FtpsClient.Connect(&ftpsOptions)
&var_error = false

if (&success = true)
    &getsuccess = &FtpsClient.Put("C:\temp\testfile.txt", "/ftpstest")
    if (&getsuccess = false)
        &var_error=true
    endif
else
    &var_error=true
endif

&FtpsClient.Disconnect()

if (&var_error = true)
    if(&FtpsClient.HasError())
        msg("Error. Code: " + "&FtpsClient.GetErrorCode() + "Description: " + &FtpsClient.GetErrorDescription())
    endif
endif
```

## [How to Upload a file](#How+to+Upload+a+file)

```
&FtpsOptions.Host = "172.16.4.5" 
&FtpsOptions.User = "dummyuser" 
&FtpsOptions.Port = 21 
&FtpsOptions.Password = "dummypass"
&FtpsOptions.ForceEncryption = true
&FtpsOptions.ConnectionMode = FtpConnectionMode.PASSIVE
&FtpsOptions.EncryptionMode = FtpEncryptionMode.EXPLICIT
&FtpsOptions.Protocol = FtpsProtocol.TLS1_2
&FtpsOptions.TrustStorePath = "C:\cacerts\truststore.pkcs12"
&FtpsOptions.Encoding = FtpEncoding.BINARY

&success = &FtpsClient.Connect(&ftpsOptions)
&var_error = false

if (&success = true)
    &putsuccess = &FtpsClient.Put("C:\temp\testfile.txt", "/ftpstest")
    if (&putsuccess = false)
        &var_error=true
    endif
else
    &var_error=true
endif

&FtpsClient.Disconnect()

if (&var_error = true)
    if(&FtpsClient.HasError())
        msg("Error. Code: " + "&FtpsClient.GetErrorCode() + "Description: " + &FtpsClient.GetErrorDescription())
    endif
endif
```

Warning! These are just working examples; do not hardcode passwords or keys.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
