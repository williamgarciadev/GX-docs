---
title: "Runtime external object"
source_id: 33076
source_url: https://wiki.genexus.com/commwiki/wiki?33076
genexus_version: "18"
---

# Runtime external object

The GeneXus.Common.Runtime external object allows you to get or set specific runtime properties, with different purposes.

`[imagen omitida: wiki id 52091]`

## [Properties](#Properties)

### [Environment property](#Environment+property)

It allows you to differentiate, at runtime, when the application executes some action on the client-side or on the server-side. Its purpose is to allow you to make decisions programmatically to be consistent with the business logic of the system (e.g. determine the insert timestamp of a new record, which can differ between the client or the server during the synchronization).

It is based on the RuntimeEnvironment domain (described below) that provides the environment information in which the called action was executed.

|  |  |  |  |
| --- | --- | --- | --- |
|  | **[Online Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?14981)** | **[Offline Native Mobile applications architecture](https://wiki.genexus.com/commwiki/wiki?22221)** | **Web** |
| **[Start event](https://wiki.genexus.com/commwiki/wiki?8043)** | Server | Device | Server |
| **[Refresh event](https://wiki.genexus.com/commwiki/wiki?8195,,)** | Server | Device | Server |
| **[Load event](https://wiki.genexus.com/commwiki/wiki?8188)** | Server | Device | Server |
| **[Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)** | Server | Device | Server |
| **[Business Component rules](https://wiki.genexus.com/commwiki/wiki?23813)** | Server | Device | Server |
| **[ClientStart event](https://wiki.genexus.com/commwiki/wiki?24044) & [Navigation Start events](https://wiki.genexus.com/commwiki/wiki?25668)** | Device | Device | N/A |
| **[User defined event](https://wiki.genexus.com/commwiki/wiki?8044)** | Device | Device | Browser |

#### [RuntimeEnvironment domain](#RuntimeEnvironment+domain)

It is an enumerated domain describing possible runtime environments.

|  |  |
| --- | --- |
| **Server** | Server-side |
| **Device** | Client-side on the Native Mobile or Angular environment. |
| **Browser** | Client-side on Web environment. |

### [ExitCode Property](#ExitCode+Property)

This property allows setting the exit code (also known as errorlevel) of a process when it terminates, specifically, the one of a procedure with [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) set to 'Command Line'. It is typically used to control the flow of batch programs.

The default value is 0.  
The exit code of a process that terminates abnormally (with an exception) is 1.

**Note:** The exit code set by the terminated program can be read using the '%ERRORLEVEL%' variable in a Windows batch file and the '$?' in Linux shell.

## [Methods](#Methods)

The runtime external object allows you to read the generic environment variables you have defined. To achieve this, you can use the following methods:

#### [**GetEnvironmentVariable**](#GetEnvironmentVariable)

Returns the value of the environment variable. If it does not exist, returns EMPTY.

**Return value**[VarChar](https://wiki.genexus.com/commwiki/wiki?6778)  
**Parameters**VarName:VarChar

#### [**HasEnvironmentVariable**](#HasEnvironmentVariable)

Returns True if, and only if, the environment variable exists (<> NULL).

**Return value**[Boolean](https://wiki.genexus.com/commwiki/wiki?4374)  
**Parameters** VarName:VarChar

#### [**GetEnviromentVariables**](#GetEnviromentVariables)

Returns all environment variables defined.

**Return value**[Properties Data Type](https://wiki.genexus.com/commwiki/wiki?31606)  
**Parameters** None

## [Samples](#Samples)

This section provides some simple use cases where the Runtime external object might be useful.

1. **Environment Property - Gap during synchronization**  
   In an offline Native Mobile application, when a new record is inserted in the database, this record will adopt the device timestamp (the real one), but after the synchronization, the server will persist another. This problem can be avoided if you take control when the record is physically inserted.  
     
   Suppose you have the following transaction:

   ```
   Task
   {
      TaskId*      : Numeric(4.0)
      TaskAbstract : Character(200) 
      TaskCreated  : DateTime
   }
   Rules
      noaccept(TaskCreated);
      TaskCreated = now() if insert;
   ```

   If the application is offline, which will be the TaskCreated timestamp value? The moment when the record is inserted on the offline database or when is inserted in the server database? For avoiding this problem, you can include TaskSynced attribute (DateTime base too), and differentiate both cases as follows:

   ```
   Task
   {
      TaskId*      : Numeric(4.0)
      TaskAbstract : Character(200) 
      TaskCreated  : DateTime
      TaskSynced   : DateTime
   }
   Rules
      noaccept(TaskCreated);
      noaccept(TaskSynced);
      TaskCreated = now() if insert and Runtime.Environment = RuntimeEnvironment.Device;
      TaskSynced  = now() if insert and Runtime.Environment <> RuntimeEnvironment.Device;
   ```
2. **Environment property - Offline notifications**  
   When a Native Mobile application works in an offline architecture, the process for sending notifications must be controlled in order to be sent by the server (not the device). This problem can be avoided analogously to the use-case (1) by restricting the execution to only when it's from the server (RuntimeEnvironment.Server).
3. **ExitCode property - Setting Errorlevel**   
   The following procedure returns exit codes (and writes to the console) as follows  
   If data could be saved successfully: The procedure sets exit code 0 and writes to the console "Data has been saved successfully"  
   If data could not be saved: The procedure sets exit code 2 and writes to the console "Data could not be saved"  
   If a not handled exception occurs (eg. the 'Client BC' has a division by zero): The procedure sets exit code 1 and writes to the console the details of the exception

   ```
   &Client.Id = 1
   &Client.Name = "John"
   &Client.Save()
   If &Client.Fail()
       rollback
       msg("Data could not be saved",status)
       GeneXus.Common.Runtime.Exitcode = 2
   else
       commit
       msg("Data has been saved successfully",status)
   endif
   ```
4. To get an environment variable, you can use HasEnvironmentVariable and GetEnvironmentVariable as follows:

   ```
   if(Runtime.HasEnvironmentVariable('VAR_NAME'))
        &VarName = Runtime.GetEnvironmentVariable("VAR_NAME")
   endif
   ```
5. If you want to get all the environment variables, you should do something like the following:

   ```
   &AllEnvironmentVars = Runtime.GetEnviromentVariables()//&AllEnvironmentVars is of Properties data type
   for (&EnvionmentVariable in &AllEnvironmentVars)
       msg(Format(!"%1:%2", &EvironmentVariable.Key, &EvironmentVariable.Value))
   endfor
   ```

## [Scope](#Scope)

**Generators:**[Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

## [See Also](#See+Also)

[Error\_Handler command](https://wiki.genexus.com/commwiki/wiki?8238)  
[Exception Handling in Genexus](https://wiki.genexus.com/commwiki/wiki?21740,,)


|  |
| --- |
| **Backlinks** |
| [Toc:Application Deployment tool](https://wiki.genexus.com/commwiki/wiki?32092) | [Toc:Application Deployment tool (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?54334) | [CORS settings with environment variables](https://wiki.genexus.com/commwiki/wiki?52127) |
| [Exception\_Handler rule](https://wiki.genexus.com/commwiki/wiki?44808) |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) |
| [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
