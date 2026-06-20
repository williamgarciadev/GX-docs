---
title: "Shell function"
source_id: 8502
source_url: https://wiki.genexus.com/commwiki/wiki?8502
genexus_version: "18"
---

# Shell function

Runs an executable on the Operating System.

### [Syntax](#Syntax)

**&***ret* **= Shell(‘***program.exe**’*****,** [*Modal*]**,**[RedirectOutput]**)**

**Where:**  
  
*Modal*  
    Is a Numeric optional parameter. It indicates whether to wait for the launched program to finish or to continue executing it.

    If you pass:

* 0: The call will be non-modal. This means that the caller program will continue the execution immediately after performing the call, without waiting for the called program to finish.
* 1: The call will be modal. This means that the caller program will wait until the caller program finishes to return to the execution.

    If you don’t specify any value, 0 is assumed by default.

*RedirectOutput*  
  Is a Numeric optional parameter. It indicates whether to redirect the output of the launched program to the console window. It only applies when Modal=1.

  If you pass:

* 0: The process output won't be printed in the console window.
* 1: The process output will be printed in the console window.

   If you don’t specify any value, 0 is assumed by default.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Objects**: [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators**: [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),[Java](https://wiki.genexus.com/commwiki/wiki?12258)

### Description

If the Shell function executes the program successfully, it returns 0 (zero). Otherwise, it returns a number other than 0, depending on the error.

When using the Java generator, you make an EXECUTE that should work on any environment provided that the file is executable.

If a number other than 0 is returned, the function returns the ExitCode of the process that is sent to run. For example, &ret = shell ("process.exe",1) returns the exit code that returns process.exe. Except for Modal=0 when it doesn't get the ExitCode (it will be zero) because once the associated process is successfully launched, the shell function returns control without waiting for the process to exit.

**Notes:**

* In a Web environment, the process is executed without user interfaces and with the same security permissions as the web application.
* In Java web applications, the process is executed in Tomcat's root directory.
* Since GeneXus 16 Upgrade 2, you must include the GXClasses.Win.dll file manually in your deployment when using this function. See [SAC#44468](https://www.genexus.com/developers/websac?en,,,44468).

To use this function, the [Standard Functions property](https://wiki.genexus.com/commwiki/wiki?7403) must be set with the “Allows non-standard functions” value.

It is possible to pass parameters when executing a program with the Shell function. For example:

```
&ret = shell('program.exe "C:\My Documents\filename.txt"')
```

If the directory of the executable or the parameters has white spaces, it has to be delimited by " ". For example:

```
&ret = shell('"C:\Program Files\MyProgram.exe" Par1 Par2')
```

### [Security Tips](#Security+Tips+)

If this function is used, sanitizing external user inputs is a must.

#### 

####


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [Automated download of a file on Internet Explorer 11](https://wiki.genexus.com/commwiki/wiki?47272) |
| [Security Scanner built-in tool](https://wiki.genexus.com/commwiki/wiki?46412) | [Security Scanner built-in tool (GeneXus 18 or prior)](https://wiki.genexus.com/commwiki/wiki?52570) |
|

---
