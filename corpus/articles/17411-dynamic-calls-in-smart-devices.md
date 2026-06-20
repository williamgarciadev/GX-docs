---
title: "Dynamic Calls in Smart Devices"
source_id: 17411
source_url: https://wiki.genexus.com/commwiki/wiki?17411
genexus_version: "18"
---

# Dynamic Calls in Smart Devices

[Call command](https://wiki.genexus.com/commwiki/wiki?8260) is supported in [Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17042). The objects to be called can be defined at design time or in execution time. We call the latter dynamic or variable calls.

The supported syntax is:

**Call(** {'*pgm* ' | *&var* | ATT:att} [ {,*parm*} …]**)**

Other supported ways are stated in [Calls to Elements in Work Withs from Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17160).

### [Dynamic Calls](#Dynamic+Calls)

**Syntax**

**Call(** {*&var* | ATT:att}[ {, *parm*} …]**)**

The format of *&var* or *att* is <type>:<name>[?<parameter>[{, *parm*} …]

The supported types are:

|  |  |
| --- | --- |
| sd | Dashboard, WorkWith for Smart Devices pattern instance, Panel for Smart Devices |
| prc | REST Procedure |
| wbp | Web Object |
| eo | External Object |
|  |  |
| <name> | Stands for the object name |

Note:  
Since [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,) adds optimizations in build mechanisms, only the necessary metadata is generated for each main object and therefore you must also include dummy calls to the objects that are called dynamically and are not in the call tree of the main.

### [Examples](#Examples)

1. A dispatcher with fixed parameter

```
Event 'ViewPerson'
    Composite
        &Object = GetPersonDetailLayout(PersonType)
        call(&Object,PersonId)
    EndComposite
EndEvent
```

```
procedure: GetPersonDetailLayout

Parm(in:&PersonType,out:&Object);

if &PersonType = Type.Person
   &Object = "sd:WorkWithDevicesPerson.Person.Detail"
else
   &Object = "sd:WorkWithDevicesDean.Dean.Detail"
endif
```

2. A dispatcher with dynamic parameter assignment

```
Event 'ViewPerson'
    Composite
        &Object = GetPersonDetailLayout(PersonType,PersonId)
        call(&Object)
    EndComposite
EndEvent
```

```
procedure: GetPersonDetailLayout

Parm(in:&PersonType,in:&PersonId,out:&Object);

if &PersonType = Type.Person
   &Object = "sd:WorkWithDevicesPerson.Person.Detail?"+&PersonId.ToString().Trim()
else
   &Object = "sd:WorkWithDevicesDean.Dean.Detail?"+&PersonId.ToString().Trim()
endif
//and in some place of your main or object included in the main's call tree:
if 1 = 0
   WorkWithDevicesPerson.Person.Detail("1")
   WorkWithDevicesDean.Dean.Detail("1")
endif
```

### [Troubleshooting](#Troubleshooting)

#### [Could not execute dyncall](#Could+not+execute+dyncall)

The following error appears trying to execute a dynamic call.

```
Could not execute dyncall to /webapp/sd:objectname. The referenced object does not exist or is not included in the application call tree; check documentation for more information
```

Make sure you include a static code reference to the object to force its compilation and metadata generation.

### [Note](#Note)

If the variable &Object is empty, the dynamic call ignores it.


|  |
| --- |
| **Backlinks** |
| [Auto-Registration in SD: What to do when a certain action requires the user to log in](https://wiki.genexus.com/commwiki/wiki?19835) | [Offline Database Object Table selection](https://wiki.genexus.com/commwiki/wiki?23561) |

---
