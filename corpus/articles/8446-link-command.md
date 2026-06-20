---
title: "Link command"
source_id: 8446
source_url: https://wiki.genexus.com/commwiki/wiki?8446
genexus_version: "18"
---

# Link command

Redirects to web objects of the [KB](https://wiki.genexus.com/commwiki/wiki?1836) or any external URL.

### [Syntax](#Syntax)

**Link(** *usr-pgm* | *’url’*[{, *parm*}…] **)**

**Where:**  
  
*usr-pgm*  
    Is the name of the Web Panel to where it is going to redirect.

*url*  
    Is the name of URL to where it is going to redirect.

*parm*  
    Are the parameters that the Web Panel or URL receives.

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550),
[Apple](https://wiki.genexus.com/commwiki/wiki?14917),
[Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Description](#Description)

The Link command is equivalent to the Call command, but it is specific to the web. When this command is used, there is an automatic redirecting to the URL specified in it.  
  
When it is used in a Web Panel, it can be used in any event, except for the Load event.

### [Samples](#Samples)

```
Event Enter //External URL
    Link(‘http://www.example.com’) 
EndEvent
```

```
Event 'MyEvent' //Object known at design-time
    Link(Client,1,!'INS')
    Client(1,!'INS') // recommended coding style
EndEvent
```

```
Event 'MyEvent' //Object known at run-time
   &MyObject = !'Client' 
   Link(&MyObject,1,!'INS') 
EndEvent
```

### [See Also](#See+Also)

[Link Function](https://wiki.genexus.com/commwiki/wiki?8444)  
[Parameters Style property for Environments](https://wiki.genexus.com/commwiki/wiki?46404)  
[Call command](https://wiki.genexus.com/commwiki/wiki?8260)


|  |
| --- |
| **Backlinks** |
| [Call command](https://wiki.genexus.com/commwiki/wiki?8260) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [HowTo: Open a Web Page in a New Browser Window from a Smart Devices Application](https://wiki.genexus.com/commwiki/wiki?18555) |
| [Link Function](https://wiki.genexus.com/commwiki/wiki?8444) | [Macroservices and Miniservices systems](https://wiki.genexus.com/commwiki/wiki?55518) | [Microservices systems](https://wiki.genexus.com/commwiki/wiki?55526) | [Modules - Dynamic calls](https://wiki.genexus.com/commwiki/wiki?22585) |
| [Parameters Style property for Environments](https://wiki.genexus.com/commwiki/wiki?46404) | [Single Page Applications](https://wiki.genexus.com/commwiki/wiki?22455) | [Transitions for Web](https://wiki.genexus.com/commwiki/wiki?22460) |

---
