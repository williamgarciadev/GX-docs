---
title: "FromTimeZone method"
source_id: 21916
source_url: https://wiki.genexus.com/commwiki/wiki?21916
genexus_version: "18"
---

# FromTimeZone method

Converts a DateTime value from one timezone, to another. The first one is passed as a parameter of the method, while the second one is the current timezone of the process executing the method.

### [Syntax](#Syntax)

&varDateTimeInCurrentTimeZone = &varDateTime**.FromTimeZone(***<TimeZone>***)**

**Where:**  
*TimeZone*  
             Is a parameter that must be of type [Timezones Domain](https://wiki.genexus.com/commwiki/wiki?21989).

**Type Returned:**  
     DateTime  
            A value resulting from the conversion of the original DateTime value, from the timezone specified in the parameter (<TimeZone>) to the current time zone of the process. If the parameter value is not a valid time zone (that is, it doesn’t belong to the Time Zone domain values) then the method has no effect.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604),[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3)

### [Description](#Description)

The current DateTime of the process depends on the application type. In case it is a web application, then it is defined by the browser that executed the application (Browser's DateTime).

When this method is used from a Mobile Application, then the current DateTime of the process will be based off of the time of the mobile device running said application. Finally, when the process is running from a command line, then the current DateTime is defined by the system's time (application server). In case the [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893) is executed, the current DateTime will be changed. Thus, after the call to the method, it may hold a different value from the browsers, mobile devices, and system times, for web and command line processes, respectively. 

### [Samples](#Samples)

```
Event 'FromTZ'
    &ConvertedTimeZone = &varDateTime.FromTimeZone(Timezones.Azores)
Endevent
```

If this application is run from a device in Uruguay, then the current time zone of the process will be America/Montevideo (UTC -03:00).

Suppose that the variable &varDateTime contains the value 24/04/2013 16:00 and the event **FromTZ** is executed. As seen in the example above, the argument of the method is Timezones.Azores. This means that the function will attempt to convert the DateTime variable  *&varDateTime* from the Azores time zone ( UTC -01:00 ) to the current timezone of the process, which is Montevideo. As a result, the variable &ConvertedTimeZone will take the value 24/04/2013 14:00.

### [See Also](#See+Also)

[Enabling TimeZone Support](https://wiki.genexus.com/commwiki/wiki?22147)  
[DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218)  
[GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915)  
[SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893)  
[CurrentOffset method](https://wiki.genexus.com/commwiki/wiki?21917)


|  |
| --- |
| **Backlinks** |
| [CurrentOffset method](https://wiki.genexus.com/commwiki/wiki?21917) | [GetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21915) | [SetTimeZone method](https://wiki.genexus.com/commwiki/wiki?21893) |
| [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) |

---
