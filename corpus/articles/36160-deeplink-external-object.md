---
title: "DeepLink external object"
source_id: 36160
source_url: https://wiki.genexus.com/commwiki/wiki?36160
genexus_version: "18"
---

# DeepLink external object

The DeepLink external object helps you manually manage [deep linking](https://wiki.genexus.com/commwiki/wiki?36163) on your applications.

|  |  |
| --- | --- |
|  |  |

## [Properties](#Properties)

It does not have any.

## [Methods](#Methods)

It does not have any.

## [Events](#Events)

### [Handle event](#Handle+event)

Every link whose base is given by the [Deep Link Base URL property](https://wiki.genexus.com/commwiki/wiki?36161) will be captured by this event when the device tries to open it. When the event is triggered, it receives a URI and you as a developer must advice when the processing has been handling successful. This action is done by setting an output parameter to True (by default is False) before calling the appropriate panel.

|  |  |
| --- | --- |
| **Input** | Uri:[URL](https://wiki.genexus.com/commwiki/wiki?15668) |
| **Output** | Handled:[Boolean](https://wiki.genexus.com/commwiki/wiki?4374) |

## [Example](#Example)

Suppose you have an e-commerce website and you are developing the mobile app. It is desirable that the end user will be able to view products on the app when it receives a URL of the website (e.g. by email, WhatsApp, Facebook, or another third-party resource). Also, you want to handle such request for processing or register other information. In such case, in the Smart Device's Main object (which has [Deep Link Base URL property](https://wiki.genexus.com/commwiki/wiki?36161) set), you must write the following event.

```
Event DeepLink.Handle( &URL, &IsHandled )
    Composite
      // Suppose that our website handles URIs such https://www.mystore.com/viewproduct?1
      if &URL.ToLower().StartsWith("https://www.mystore.com/")
      and &URL.Contains("viewproduct") 
         &Index = &URL.indexof( "?" )+1
         &Query = &URL.Substring( &Index)
         &ProductId = &Query.Trim().ToNumeric()
         &IsHandled = True 
         SDViewProduct(&ProductId)
      endIf
    EndComposite
EndEvent
```

Note how the code is written. First, we must ensure that the request is made to the desired domain (because we can handle a set of different URIs) and then we identify which content has been requested (in our case, "viewproduct"). The following lines parse the parameters in the query (the ProductId), set the process as handled and finally call the Smart Device Panel which knows how to process the request.

## [Notes](#Notes)

* This external object must be used only in the [Smart Devices Main object](https://wiki.genexus.com/commwiki/wiki?17817).
* A call for a panel which serves a deep link follows the [CallOptions](https://wiki.genexus.com/commwiki/wiki?23666) set.
* When the Handled out parameter is set to True, won't trigger the [automatic](https://wiki.genexus.com/commwiki/wiki?36163) deep linking mechanism.
* For parsing multiple parameters, the following code might be helpful.  
  + **Nominated scenario** (i.e. &Query.Contains("&") condition is satisfied)

    ```
    for &Parm in &Query.SplitRegEx("&") // Paramters are separated by ampersand as key=value
        &i   = &Parm.IndexOf("=")
        &Key = &Parm.Substring(1,&i-1)
        &Val = &Parm.Substring(&i+1)
        do Case
            case &Key = "parm1"
                &parm1 = transform1(&Val)
            case &Key = "parm2"
                &parm2 = transform2(&Val)
            ...
         endCase
     endFor</parm2></parm1>
    ```
  + **Positioned scenario**

    ```
    &i = 1
    for &Parm in &Query.SplitRegEx(",") // Paramters are separated by comma
        do Case
            case &i = 1
                &parm1 = transform1(&Parm)
            case &i = 2
                &parm2 = transform2(&Parm)
            ...
        endCase
        &i += 1
    endFor
    ```For both cases, transformioperation will transform a string value to the appropriate parmi  data type.  
  For example, If parm1:Numeric(4.0) and parm2:VarChar(40), the transform operations could be:  
  - &parm1 = &str.Trim().ToNumeric()  
  - &parm2 = &str.Replace("%20"," ")

## [Availability](#Availability)

This external object is available as of [GeneXus 15 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?35908,,).

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Platforms** | Smart Devices (iOS, Android) |

## [See also](#See+also)

* [Deep Link Base URL property](https://wiki.genexus.com/commwiki/wiki?36161)
* [HowTo: Deep Linking on Native Mobile](https://wiki.genexus.com/commwiki/wiki?36163)


|  |
| --- |
| **Backlinks** |
| [GeneXus Core module](https://wiki.genexus.com/commwiki/wiki?31268) | [GeneXus Core module (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?54413) | [HowTo: Deep Linking on Native Mobile](https://wiki.genexus.com/commwiki/wiki?36163) |
| [Category:Smart Devices API](https://wiki.genexus.com/commwiki/wiki?15288) | [Category:Smart Devices API (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55174) |

---
