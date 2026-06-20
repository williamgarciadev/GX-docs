---
title: "SFTP Client"
source_id: 44966
source_url: https://wiki.genexus.com/commwiki/wiki?44966
genexus_version: "18"
---

# SFTP Client

**Note**: This is part of [GeneXus SFTP Module](https://wiki.genexus.com/commwiki/wiki?44965)  and implements a restricted client for the SFTP Protocol.

## [Connect](#Connect)

It establishes the SSH connection to the server using the authentication method defined on the SDT SftpOptions.

```
Connect(SftpOptions)
```

* Input SftpOptions: SDT SftpOtptions with authentication configuration preloaded
* Returns: Boolean true if the connection was successful.

Example:

```
&success = &SftpClient.Connect(&SftpOptions)
```

## [Get](#Get)

Downloads a file from the remote SFTP server to the client's machine using an already open connection.

```
Get(remoteFilePath, localDirectory)
```

* Input remoteFilePath: VarChar(9999), path relative to the working directory (pwd) including filename and extension.
* Input localDirectory: VarChar(9999), an absolute local path to save the downloaded file.
* Returns: Boolean true if the operation was successful.

Example:

```
&success = &SftpClient.Get("/sftpfolder/samplefile.txt", "C:\Temp\")
```

## [Put](#Put)

Uploads a file from the local client's machine to the SFTP server using an already open connection.

```
Put(localFilePath, remoteDirectory)
```

* Input localFilePath - VarChar(256), absolute local path to the file including filename and extension.
* Input remoteDirectory - VarChar(256), path relative to the working directory (pwd).
* Returns: Boolean true if the operation was successful.

Example.

```
&success = &SftpClient.Put("C:\Temp\samplefile.txt", "/sftpfolder")
```

## [GetWorkingDirectory](#GetWorkingDirectory)

Returns the default remote server working directory (command pwd).

```
GetWorkingDirectory()
```

* Returns VarChar(9999)

Example:

```
&directory = &SftpClient.GetWorkingDirectory()
```

## [Disconnect](#Disconnect)

Closes the SFTP connection.

It is mandatory as good programming practice after finishing using the channel and as a security measure.

```
Disconnect()
```

* It does not receive any parameters and does not return any value.

Example

```
&SftpClient.Disconnect()
```

## [Rm](#Rm)

This method is available since [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396)

Remove/delete a file from the remote SFTP server using an already open connection.

```
Rm(remoteFilePath)
```

* Input remoteFilePath: VarChar(9999), path relative to the working directory (pwd) including filename and extension.
* Returns: Boolean true if the operation was successful.

Example:

```
&success = &SftpClient.Rm("/sftpfolder/samplefile.txt")
```

## [How to Download a File](#How+to+Download+a+File)

```
&SftpOptions.Host = "172.16.4.5"
&SftpOptions.User = "dummyuser"
&SftpOptions.Port = 22
&SftpOptions.Password = "dummypass"
&SftpOptions.AllowHostKeyChecking = true
&SftpOptions.KeyPath = "C:\Temp\keys\private_key.pem"
&SftpOptions.KeyPassword= "dummykeypass"
&SftpOptions.KnownHostsPath = "C:\Temp\known_hosts"

&success = &SftpClient.Connect(&sftpOptions)
&var_error = false

if (&success = true)
    &getsuccess = &SftpClient.Put("C:\temp\testfile.txt", "/sftptest")
    if (&getsuccess = false)
        &var_error=true
    endif
else
    &var_error=true
endif

&SftpClient.Disconnect()

if (&var_error = true)
    if(&SftpClient.HasError())
        msg("Error. Code: " + &SftpClient.GetErrorCode() + "Description: " + &SftpClient.GetErrorDescription())
    endif
endif
```

## [How to Upload a file](#How+to+Upload+a+file)

```
&SftpOptions.Host = "172.16.4.5"
&SftpOptions.User = "dummyuser"
&SftpOptions.Port = 22 
&SftpOptions.Password = "dumypass"
&SftpOptions.AllowHostKeyChecking = true
&SftpOptions.KeyPath = "C:\Temp\keys\private_key.pem"
&SftpOptions.KeyPassword= "dummykeypass"
&SftpOptions.KnownHostsPath = "C:\Temp\known_hosts"

&success = &SftpClient.Connect(&sftpOptions)
&var_error = false

if (&success = true)
    &putsuccess = &SftpClient.Put("C:\temp\testfile.txt", "/sftptest")
    if (&putsuccess = false)
        &var_error=true
    endif
else
    &var_error=true
endif

&SftpClient.Disconnect()

if (&var_error = true)
    if(&SftpClient.HasError())
        msg("Error. Code: " + &SftpClient.GetErrorCode() + "Description: " + &SftpClient.GetErrorDescription())
    endif
endif
```

Warning! These are just working examples, do not hardcode passwords or keys.


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 2](https://wiki.genexus.com/commwiki/wiki?53396) | [Toc:GeneXus Security API](https://wiki.genexus.com/commwiki/wiki?43916) |

---
