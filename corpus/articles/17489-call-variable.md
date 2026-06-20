---
title: "Call Variable"
source_id: 17489
source_url: https://wiki.genexus.com/commwiki/wiki?17489
genexus_version: "18"
---

# Call Variable

Allows the user to make a dynamic call, providing flexibility to the smart device applications. The objects to be called can be defined at design time or execution time.

### [Syntax](#Syntax)

**Call(** {*&var* | ATT:att} [ {,  *parm*} …] **)**

The format of the string value of &var or att  is <**Supported type**>:<object name>[?<parameter>[{, *parm*} …]]

### [Supported types](#Supported+types)

* **sd** (Dashboard, Workwith for smart devices pattern instance, Panel for Smart Devices)
* **prc** (REST Procedure)
* **wbp**(Web Object)

e.g:

&Object = "sd:WorkWithDevicesPerson.Person.Detail?"+&PersonId.ToString().Trim()  
call(&object)

### [Example](#Example)

1) In this example we want to redirect the user or the program flow depending on a control that we are going to do in a procedure once the user select a person from a list. What we want to control is that the selected user has all the data we want from him. `[imagen omitida: wiki id 17511]` steps: Create a work with smart devices to show a list of persons and edit the default action of the grid in order to perform an action when the user select a person of the list. `[imagen omitida: wiki id 17512]` **Event select fo the grid** // MissingData is a procedure that checks if the selected person have all the information complete and redirect the user to the next screen depending on this.

```
Event 'Select'
  Composite
   MissingData.Call(PersonId,&object)
   call(&object,PersonId)
  EndComposite
EndEvent
```

**MissingData procedure code**// this procedure check the person information an return a variable object that will be used in the work with smart device panel to redirect

```
for each 
  where PersonId = &PersonId
   &PersonAddress = PersonAddress
   &PersonName = PersonName
   &PersonPhone = PersonPhone
   &PersonPhoto = PersonPhoto
endfor
 
do case
  case &PersonAddress.IsEmpty()
  &ok = false
 
  case &PersonName.IsEmpty()
  &ok = false
 
  case &PersonPhone.IsEmpty()
  &ok = False
 
  case &PersonPhoto.IsEmpty()
  &ok = false
 
  otherwise
  &ok = true 
endcase
 
 
if &ok = false
   &Object = "sd:WorkWithDevicesPerson.Person.Detail.Update"
else
   &Object = "wbp:ViewPersonWeb"
endif
```

2) Dispatcher with fixed parameter

```
Event 'ViewPerson'
 Composite
   &Object = GetPersonDetailLayout(PersonType)
   call(&Object,PersonId)
 EndComposite
EndEvent
```

```
procedure GetPersonDetailLayout
Parm(in:&PersonType,out:&Object);
if &PersonType = Type.Person
 &Object = "sd:WorkWithDevicesPerson.Person.Detail"
else
 &Object = "sd:WorkWithDevicesDean.Dean.Detail"
endif
```

3) Dispatcher with dynamic parameter assignment

```
Event 'ViewPerson'
 Composite
   &Object = GetPersonDetailLayout(PersonType,PersonId)
   call(&Object)
 EndComposite
EndEvent
```

```
procedure GetPersonDetailLayout
Parm(in:&PersonType,in:&PersonId,out:&Object);
if &PersonType = Type.Person
 &Object = "sd:WorkWithDevicesPerson.Person.Detail?"+&PersonId.ToString().Trim()
else
 &Object = "sd:WorkWithDevicesDean.Dean.Detail?"+&PersonId.ToString().Trim()+","+&SecurityLevelId.ToString().Trim()

endif
```

### [From Variable to Fixed](#From+Variable+to+Fixed)

Note the other ways to call an object

1) Using [Link Function](https://wiki.genexus.com/commwiki/wiki?8444)  
&Object = WorkWithDevicesPerson.Person.Detail.link(&PersonId.ToString().Trim())  
call(&object)

2) Calling directly (ref.: [Call command](https://wiki.genexus.com/commwiki/wiki?8260))  
WorkWithDevicesPerson.Person.Detail(&PersonId.ToString().Trim())

### [Scope](#Scope)

**Objects**: Smart devices **Platform:** Android, iOS

### [See Also](#See+Also)

[Call command](https://wiki.genexus.com/commwiki/wiki?8260)   
[Calls to Elements in Work Withs from Native Mobile Applications Events](https://wiki.genexus.com/commwiki/wiki?17160).


|  |
| --- |
| **Backlinks** |
| [Create function](https://wiki.genexus.com/commwiki/wiki?8359) | [Dynamic Component Creation](https://wiki.genexus.com/commwiki/wiki?5404) | [Link Function](https://wiki.genexus.com/commwiki/wiki?8444) |

---
