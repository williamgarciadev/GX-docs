---
title: "Call method"
source_id: 16224
source_url: https://wiki.genexus.com/commwiki/wiki?16224
genexus_version: "18"
---

# Call method

Calls a [GeneXus object](https://wiki.genexus.com/commwiki/wiki?1866) (either with transfer of parameters or not) such as a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916) or a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), etc., from another object (which is the caller).

### [Syntax](#Syntax)

*ObjectName***.Call(**[parm1, .... , parN]**)**

**Where:**  
*ObjectName*  
     Is the name of the object you want to call.

*par1, …, parN*  
     Are optional parameters that can be sent to the called object with some purpose (and they must be received in the called object by declaring them with the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)).

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)

### [Description](#Description)

The Call method can be written in different sections of the caller object, depending on whether the caller is a [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), a [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), a [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), etc. (if the caller is a Procedure, the Call method must be included in some line of its Source; if the caller object is a Transaction, the call can be included in its Rules section as well as inside an Event, depending on the requirement, etc.).

**Note**: The syntax of the Call method allows you to omit the dot and the Call, and the invocation will be exactly the same, as GeneXus has the intelligence to detect that you are calling an object.

### [Samples](#Samples)

**Example 1**

Suppose you have a Web Panel in your [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?2428), that only has a button included in its form. When the user presses the button, the event associated with the button is executed and the objective is to call a Procedure that prints all the customers. So, you define the following code inside the event associated with the button, to achieve the objective:

```
Event 'Print all customers'
    PrintAllCustomers.call()
EndEvent
```

The following code behaves exactly like the above:

```
Event 'Print all customers'
    PrintAllCustomers()    //the dot and the call were omited
EndEvent
```

In both examples, the Procedure named PrintAllCustomers is called without parameters (so, no [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) is needed to be defined in the Procedure).

**Example 2**

Now suppose the Web Panel has a [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598) in its form, that shows all the countries stored in the database. And the button is also present in the form. The user will select a country and after that, he will press the button. The objective in this case, is to call a Procedure that prints all the customers who belong to the country selected by the user.

`[imagen omitida: wiki id 24260]`

When the user selects a country, the CountryId attribute value will be assigned to the &CountryId variable associated with the [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598). After that, when the user presses the button, the event associated with the button will be executed.

So, inside the event associated with the button, you have to define the invocation to the Procedure. In this case, you have to send to the Procedure the &CountryId variable as a parameter. The Procedure will receive the parameter (you must declare the parameter in the Procedure with the [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862)); finally, you will use the received value in the Procedure, in order to filter the customers that belong to that country.

The following code inside the event associated with the button, is calling the Procedure named PrintCustomers, and the &CountryId variable is sent to it as a parameter:

```
Event 'Print customers'
    PrintCustomers(&CountryId)    
EndEvent
```

The Procedure must have defined the following rule:

```
parm(&CountryId);
```

and the &CountryId variable is used in the Procedure source in order to filter the customers that belong to that country, like the following code shows:

`[imagen omitida: wiki id 24267]`

**Note**: For Smart Devices objects, the Call method must be written in the [Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042).

### [See Also](#See+Also)

[Udp method](https://wiki.genexus.com/commwiki/wiki?3964)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Communication between objects](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/communication-between-objects-gx15?p=5256)


|  |
| --- |
| **Backlinks** |
| [Call command](https://wiki.genexus.com/commwiki/wiki?8260) | [Call protocol property](https://wiki.genexus.com/commwiki/wiki?7947) | [Definition of type of parameters received (in, out, inout)](https://wiki.genexus.com/commwiki/wiki?8220) |
| [DesignOps - Guide for designers](https://wiki.genexus.com/commwiki/wiki?46871) | [Toc:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) | [New command](https://wiki.genexus.com/commwiki/wiki?6714) | [Parameter encryption on Dynamic calls](https://wiki.genexus.com/commwiki/wiki?29842) |
| [Parm rule](https://wiki.genexus.com/commwiki/wiki?6862) | [Udp method](https://wiki.genexus.com/commwiki/wiki?3964) | [Variable definition](https://wiki.genexus.com/commwiki/wiki?7375) |

---
