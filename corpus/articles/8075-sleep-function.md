---
title: "Sleep function"
source_id: 8075
source_url: https://wiki.genexus.com/commwiki/wiki?8075
genexus_version: "18"
---

# Sleep function

Makes a pause for a given number of seconds during execution of a program.

### [Syntax](#Syntax)

**sleep(***Seconds***)**   
  
**Where:**  
  
*Seconds*  
    Is the number of seconds that the application will be waiting. It can be a numeric variable or a constant.

**Type Returned:**  
Numeric(1)

### [Scope](#Scope)

**Objects:**  [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?1908,,), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

This function is useful, for instance, to implement a "daemon" to be executed with specific timeouts. The idea is to have an infinite loop and to have a waiting time of a specific number of seconds between each iteration. Thus, its use is recommended in 'batch' processes rather than in interactive applications, where the application 'dies' before the timeout specified is over.

Sleep function is better than a loop because it does not consume CPU resources. It is implemented using the Thread.Sleep method of the .Net Framework / Java Virtual Machine.

### [Samples](#Samples)

```
&var = sleep(15)  // It waits 15 seconds and in &var it returns 0
&var = sleep(0)   // It waits  0 seconds and in &var it returns 0
&var = sleep(-10) // It waits  0 seconds and in &var it returns 0
```

### [See Also](#See+Also)

[Lapse property](https://wiki.genexus.com/commwiki/wiki?17303)  
[Triggers property](https://wiki.genexus.com/commwiki/wiki?7420)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [HowTo: Use a Progress Indicator in a Panel](https://wiki.genexus.com/commwiki/wiki?19338) |
| [Lapse property](https://wiki.genexus.com/commwiki/wiki?17303) | [Sleep function (GeneXus 18 Upgrade 11 or prior)](https://wiki.genexus.com/commwiki/wiki?59671) | [Triggers property](https://wiki.genexus.com/commwiki/wiki?7420) |

---
