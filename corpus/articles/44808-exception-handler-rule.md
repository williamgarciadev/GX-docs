---
title: "Exception_Handler rule"
source_id: 44808
source_url: https://wiki.genexus.com/commwiki/wiki?44808
genexus_version: "18"
---

# Exception_Handler rule

# Exception\_Handler rule

Provides a way to perform actions when a non-managed exception occurs at runtime.

### [Syntax](#Syntax)

**Exception\_Handler(‘***subname*'**);**  
  
**Where:**  
  
*subname*  
    Is the name of a subroutine contained in the [GeneXus object](https://wiki.genexus.com/commwiki/wiki?1866) that uses this rule.

### Scope

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### Description

The exception\_handler rule is declarative.  
  
Defining this rule (and its associated subroutine) does not affect its flow, output, or [exit code](https://wiki.genexus.com/commwiki/wiki?33076).  
It will be executed after an exception is triggered. Then, it is intended to trigger an action such as sending a notification, so that those monitoring it can act on the exception.   
The action performed should be a safe one, not one that could also fail.

It is possible to get more detailed information about the exception by defining the following variables and using them in the subroutine.

|  |  |
| --- | --- |
| **Name** | **Description** |
| &GXexceptionType | Name of the platform-specific type of exception |
| &GXexceptionDetails | Message, reason, or detailed information associated with the exception |
| &GXexceptionStack | Runtime stack trace information about the exception location |

**Considerations:**

* If an object A calls object B when both have an Exception\_Handler defined and an exception occurs in B, the subroutines of both objects are executed.
* If an object A calls object B when object A has an Exception\_Handler defined and an exception occurs in B, the subroutine of A is executed.

### Samples

Consider the following Rule defined in a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293):

```
Exception_Handler('ExceptionNotifier');
```

The following Subroutine is defined in the Procedure Source, to be executed when a non-managed exception occurs at runtime:

```
Sub 'ExceptionNotifier'
    NotifyException(&GXExceptionType, &GXExceptionDetails, &GXExceptionStack)   //Sends a notification of some kind to sysadmin
EndSub
```

### [Availability](#Availability)

Exception\_Handler Rule is available since [GeneXus 16 upgrade 7](https://wiki.genexus.com/commwiki/wiki?44454,,).

### [See Also](#See+Also)

* [Error\_Handler rule](https://wiki.genexus.com/commwiki/wiki?6853)
* [ExitCode Property](https://wiki.genexus.com/commwiki/wiki?33076)
