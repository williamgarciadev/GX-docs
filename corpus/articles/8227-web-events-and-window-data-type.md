---
title: "Web Events and Window Data Type"
source_id: 8227
source_url: https://wiki.genexus.com/commwiki/wiki?8227
genexus_version: "18"
---

# Web Events and Window Data Type

The objective of this document is to explain how to work with Web object events with [Window Data Type](https://wiki.genexus.com/commwiki/wiki?7112).

The Window Data Type allows you to open [GeneXus objects](https://wiki.genexus.com/commwiki/wiki?1866) with UI or Web pages in a popup window, with the ability to do so in modal mode (blocking the caller page).

### [Behavior of Web Events](#Behavior+of+Web+Events)

The events of GeneXus objects for the Web [Environment](https://wiki.genexus.com/commwiki/wiki?7115) behave in a certain way that is different from how Objects in other environments behave. For this reason, you have to take into account several considerations when programming them.

Below you can see the highlighting of some properties of the event execution in Web objects.

A couple of elements have to be considered:

* In a Web object event, only one rerouting to an object with an interface (Web page) can be run. That is to say, only one call is executed even if more than one is programmed in the code (if there are more than one, the last one that appears is executed).
* In addition, this call (reroute) will be executed at the end of the event, regardless of where it is located within the event code.

For example, if you have the following event:

```
Event ‘event’
    <Code1>
    WebPanel.Call()
    <Code2>
EndEvent
```

**Note:** <CodeX> represents any type of code that doesn't imply a rerouting of the Web page; that is, [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) calls, variable assignments, and so on. This notation will be used throughout this document.

The order of execution will be as follows:

```
<Code1>
<Code2>
WebPanel.Call()
```

And in the following event:

```
Event ‘event’
    <Code1>
    WebPanelA.Call()
    <Code2>
    WebPanelB.Call()
    <Code3>
EndEvent
```

The order of execution will be as follows:

```
<Code1>
<Code2>
<Code3>
WebPanelB.Call() // The call to WebPanelA is ignored.
```

These are some of the main differences between Win and Web environments, as in the Win environment the code is always executed in the order in which it was specified. Also, it is one of the main factors to take into account when making a migration between these environments.

See the summary of the behavior of Web object events below:

1. **Common code processing**
2. **Processing of calls to objects with an interface**

### [What is the role of the Window Data Type in this scheme?](#What+is+the+role+of+the+Window+Data+Type+in+this+scheme%3F)

In Web object events you can also add calls to the Open() method of Window Type variables to open objects or URLs in new windows and in modal mode.  
In which part of the above scheme do they participate? You can see the behavior of Web object events as:

1. **Common code processing**
2. **Processing of Open() methods of Window Type variables**
3. **Processing of calls to objects with an interface**

That is to say, Window Type variables are processed after executing the common code and before solving the rerouting that will take place at the end of the event.  
Something else to take into account is that all calls to Open() methods of Window Type variables will be processed and executed in the order in which they appear.

Samples:

|  |  |
| --- | --- |
| **Event** | **Order of Execution** |
| ```     <Code1>     WindowType.Open()     <Code2>     WebPanel.Call()     <Code3> ``` | ```    <Code1>     <Code2>     <Code3>     WindowType.Open()     WebPanel.Call() ``` |
| ```     <Code1>     WebPanel.Call()     <Code2>     WindowType.Open()     <Code3> ``` | ```     <Code1>     <Code2>     <Code3>     WindowType.Open()     WebPanel.Call() ``` |
| ```     <Code1>     WebPanelA.Call()     <Code2>     WindowType.Open()     <Code3>     WebPanelB.Call()     <Code4> ``` | ```    <Code1>     <Code2>     <Code3>     <Code4>     WindowType.Open()     WebPanelB.Call() ``` |
| ```     <Code1>     WebPanelA.Call()     <Code2>     WindowTypeA.Open()     <Code3>     WebPanelB.Call()     <Code4>     WindowTypeB.Open()     <Code5>     WebPanelC.Call()     <Code6> ``` | ```    <Code1>     <Code2>     <Code3>     <Code4>     <Code5>     <Code6>     WindowTypeA.Open()     WindowTypeB.Open()     WebPanelC.Call() ``` |

So far,  the basic concepts of how Web object events work when the [Window Data Type](https://wiki.genexus.com/commwiki/wiki?7112) is used to call other objects were explained.  
There are many possibilities and code combinations that can be programmed, so now you will see specific considerations for some of these possible cases.

### [Use of the return command](#Use+of+the+return+command)

When the return command appears in an event, it will be taken as the end of the event. That is, everything that has been explained (order of execution), instead of being applied to the programming between the **Event ‘event’** and **EndEvent** lines, will be applied to the programming between **Event ‘event’** and **return**.

If that code has one or more calls to objects with an interface, they will be processed and a rerouting will be made to the last one. If there are no calls to objects with an interface, the return will be executed after closing the popup and a return to the [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) that called the object with the event mentioned above will be made.

Samples:

|  |  |
| --- | --- |
| **Event** | **Order of Execution** |
| ```     <Code1>     WindowType.Open()     <Code2>     return     <Code3> ``` | ```     <Code1>     <Code2>     WindowType.Open()     return ``` |
| ```    <Code1>     return     <Code2>     WindowType.Open()     <Code3> ``` | ```     <Code1>     return ``` |
| ```     <Code1>     WebPanel.Call()     <Code2>     WindowType.Open()     <Code3>     return     <Code4> ``` | ```     <Code1>     <Code2>     <Code3>     WindowType.Open()     WebPanel.Call() ``` |
| ```     <Code1>     WebPanelA.Call()     <Code2>     WindowTypeA.Open()     <Code3>     return     <Code4>     WindowTypeB.Open()     <Code5>     WebPanelB.Call()     <Code6> ``` | ```     <Code1>     <Code2>     <Code3>     WindowTypeA.Open()     WebPanelA.Call() ``` |

### [Use of the refresh command](#Use+of+the+refresh+command)

When using the [Refresh command](https://wiki.genexus.com/commwiki/wiki?25069), a couple of additional considerations have to be made regarding the order of execution of an event's code. The scheme would be as follows:

1. **Processing of common code (of the entire event)**
2. **Processing of Open() methods of Window type variables, but only those included before the refresh command.**
3. **Refresh event**

Samples:

|  |  |
| --- | --- |
| **Event** | **Order of Execution** |
| ```     <Code1>     WebPanelA.Call()     <Code2>     WindowType.Open()     <Code3>     refresh     <Code4> ``` | ```     <Code1>     <Code2>     <Code3>     <Code4>     WindowType.Open()     refresh ``` |
| ```     <Code1>     WebPanelA.Call()     <Code2>     WindowTypeA.Open()     <Code3>     refresh     <Code4>     WindowTypeB.Open()     <Code5>     WebPanelB.Call()     <Code6> ``` | ```     <Code1>     <Code2>     <Code3>     <Code4>     <Code5>     <Code6>     WindowTypeA.Open()     refresh ``` |

### [Opening external URLs with Window Type](#Opening+external+URLs+with+Window+Type)

In addition to a KB object, a URL can be associated with a Window Type variable.  
In this case, the Open() method's behavior will follow these guidelines:

* If the URL belongs to a server other than that of the caller, instead of opening in modal mode (blocking the caller Web page), it will be opened in a new, independent window and the caller will not be blocked.
* In this case, upon closing the new window the control doesn't return to the caller. Thus, the other Open() methods that may appear and common calls to objects with an interface (regardless of whether they are before or after the Open() method of the URL) are ignored.
* If the URL belongs to the same server as the caller page, it is opened in modal mode.
* If the URL and Object properties of a Window Type variable are assigned before running an Open() for it, the last assignment made to one of these two properties will be taken into account.

Samples

|  |  |
| --- | --- |
| **Event** | **Execution** |
| ```     Window.URL = ‘URL’     Window.Object = Object.Create()     Window.Open() ``` | The popup with the object is opened in modal mode. |
| ```     Window.Object = Object.Create()     Window.URL = ‘URL’     Window.Open() ``` | A new window (not modal) is opened with the URL. |
| ```     Window.Object = Object.Create()     Window.Open()     Window.URL = ‘URL’     Window.Open() ``` | The popup with the Object is opened and upon closing it, a new window is opened with the URL. |
| ```     Window.URL = ‘URL’     Window.Open()     Window.Object = Object.Create()     Window.Open() ``` | A new window is opened with the URL (the control        does not return to the caller). |
| ```     Window.URL = ‘URL’     Window.Open()     WebPanel.Call() ``` | A new window is opened with the URL (the control        does not return to the caller). |

### [Several execution lines in an event](#Several+execution+lines+in+an+event)

In an event's code, a single execution line is not always followed. That is, one thing or the other will be executed depending on certain factors.  
To indicate these types of things, use IF or CASE sentences, for example.  
Everything explained so far is applied to each execution line of an event. In other words, this entire mechanism will be applied to the chosen execution line depending on the indicated factors (variable values, and so on).

Samples

|  |  |  |
| --- | --- | --- |
| **Event** | **Execution if &var = 1** | **Execution if &var <> 1** |
| ```     <Code1>     if &var = 1        <Code2>        WindowType.Open()        <Code3>     else        <Code4>     endif     <Code5> ``` | ```     <Code1>     <Code2>     <Code3>     <Code5>     WindowType.Open() ``` | ```     <Code1>     <Code4>     <Code5> ``` |
| ```     <Code1>     if &var = 1        <Code2>        WindowType.Open()        <Code3>        WebPanelA.Call()        <Code4>     else        <Code5>        WebPanelB.Call()     endif     <Code6> ``` | ```     <Code1>     <Code2>     <Code3>     <Code4>     <Code6>     WindowType.Open()     WebPanelA.Call() ``` | ```     <Code1>     <Code5>     <Code6>     WebPanelB.Call() ``` |
| ```    <Code1>     if &var = 1        <Code2>        return        <Code3>        WindowTypeA.Open()        <Code3>     else        <Code4>        WindowTypeB.Open()     endif     <Code5> ``` | ```    <Code1>     <Code2>     return ``` | ```     <Code1>     <Code4>     <Code5>     WindowTypeB.Open() ``` |

### [Procedures](#Procedures)

In a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) code you can use the same elements as in a Web object event, including calls to Open() methods of Window Type variables and calls to Web objects with an interface (Web pages).  
Their behavior is exactly the same as that of an event; that is, you will consider a Procedure as another event. In addition, if this Procedure is called in an event with other Open() methods or calls to objects with an interface, the same guidelines will be followed as if the Procedure's code were there instead of a call.

Samples:

|  |  |  |
| --- | --- | --- |
| **Event** | **Procedure Proc1** | **Order of Execution** |
| ```     <Code1>     Proc1.Call()     <Code2>     WebPanelA.Call()     <Code3> ``` | ```     <Code4>     WindowTypeA.Open()     <Code5>     WebPanelB.Call()     <Code6>     WindowTypeB.Open()     <Code7>     WebPanelC.Call()     <Code8> ``` | ```    <Code1>     <Code4>     <Code5>     <Code6>     <Code7>     <Code8>     <Code2>     <Code3>     WindowTypeA.Open()     WindowTypeB.Open()     WebPanelA.Call() ``` |

### [Use in rules](#Use+in+rules)

When the Open() method of a Window Type variable is used in a rule, it is not triggered in the client using AJAX. It will be executed after making a POST to the server. The same happens if the rules have a Procedure with an Open() method of Window Type variable programmed in its code. More information at [SAC 24214](http://www2.gxtechnical.com/portal/hgxppredirect.aspx?15,26,0,,,24214).
