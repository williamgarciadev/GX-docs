---
title: "External Object: Java Session Bean"
source_id: 6197
source_url: https://wiki.genexus.com/commwiki/wiki?6197
genexus_version: "18"
---

# External Object: Java Session Bean

External Objects (EO) of the Java Session Beans type allow calling Java Session Beans hosted in a JEE server.

The Java Session Bean EO will store all the necessary information to make the call to the Session EJB regarding context parameters, EJB interfaces, etc. Once the EO has been defined, you will be able to invoke the real EJB in the same way you use any other GeneXus object.

`[imagen omitida: wiki id 53702]`

## [Properties](#Properties)

### [External Object](#External+Object)

`[imagen omitida: wiki id 53704]`

***Name:*** name of the EO.  
***Description:*** description of the EO.  
***[Type](https://wiki.genexus.com/commwiki/wiki?53690):*** EO type, Java Session Bean.  
***EJB Version:*** EJB version being called (either 2.x or 3.x).  
***EJB Home Object:*** EJB home or local home interface (applies only when EJB Version = 2.x).  
***EJB Object:*** EJB component interface.  
***EJB JNDI name:*** JNDI name to reference the EJB.  
***Specify JNDI context properties:*** set to Yes if context properties for the EJB lookup must be specified; otherwise, set to No.  
***[Object Visibility](https://wiki.genexus.com/commwiki/wiki?22473):*** accessibility from other objects in different Modules.

When ***"Specify JNDI context properties = YES"*** the following properties are displayed:

`[imagen omitida: wiki id 53705]`

***INITIAL\_CONTEXT\_FACTORY:*** initial context factory class.  
***PROVIDER\_URL:*** provider URL where the EJB is located.  
***SECURITY\_PRINCIPAL:*** principal to authenticate.  
***SECURITY\_CREDENTIALS:*** credentials that will be used to authenticate the principal.

### [Methods](#Methods)

`[imagen omitida: wiki id 53706]`

***Internal Name:*** internal name of the method.  
***Description:*** description.  
***Type:*** data type of the returned value, if any.  
***External Type:*** external data type of the returned value.  
***External Name:*** external name of the method.

### [Parameters](#Parameters)

`[imagen omitida: wiki id 53707]`

***Access Type*:** indicates whether the parameter is an input only, output only, or input/output parameter.  
***Internal Name*:** internal name of the parameter.  
**Description:** description of the parameter.  
***Type*:** data type that the parameter will have in GeneXus.  
***External Type:*** external data type of the parameter.

## [Use](#Use)

Suppose you want to call a Session EJB located in another server. Basically, you will follow 2 steps:

1. Create the external object according to the Session EJB.
2. Write the necessary GX code to invoke the EJB.

For the first step, the Session EJB developer must provide the JAR package containing the EJB interfaces needed to make the call. Once you have the jar file, place it in the model classpath and create the EO according to the interfaces given in the jar file (of course, it is also necessary to specify the JNDI name and probably its context properties). It will also be necessary to add a jar file with the [standard classes](https://wiki.genexus.com/commwiki/wiki?18859) needed when invoking EJBs (containing implementations of EJBLocalHome, EJBLocalObject etc.). This jar file may be different according to the version of the EJB being called (2.x or 3.x) and its name may be ejb.jar ejb3.jar o similar.

Once the EO has been defined, you simply use it as any other GX object. For example:

```
Event Enter
  &first = "Hello "
  &second = "Session Beans"
  &concat = &externalObj.Concat(&first, &second) 
  msg(&concat) //prints "Hello Session Beans"
EndEvent
```

&externalObj is a variable based on the EO for the Session EJB, &concat-&first-&second are character variables, and Concat is a method in the EO that matches a method in the EJB. As shown, the Concat being called returns the concatenation of two character variables.

## [Deployment](#Deployment)

When deploying the application through the GeneXus Deployment Wizard, it is necessary to add the EJB provider jar file as an additional library.


|  |
| --- |
| **Backlinks** |
| [Category:External object](https://wiki.genexus.com/commwiki/wiki?5669) | [Type property in External Object](https://wiki.genexus.com/commwiki/wiki?53690) |

---
