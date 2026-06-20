---
title: "Interop.CanOpen method"
source_id: 23732
source_url: https://wiki.genexus.com/commwiki/wiki?23732
genexus_version: "18"
---

# Interop.CanOpen method

Indicates whether the device is able to open a specific URL

### [Syntax](#Syntax)

```
Interop.CanOpen(<URL>)
```

The *<URL>* parameter is the URL we want to open. The method checks whether it can be opened or not.

**Type returned**  
[Boolean](https://wiki.genexus.com/commwiki/wiki?4374), indicating if the URL can be opened or not.

### [Sample](#Sample)

```
Event 'OpenTweetGenexus'
Composite
  &AppInstalled = Interop.CanOpen("twitter://user?screen_name=GeneXus")
  if &AppInstalled
   Interop.Open("twitter://user?screen_name=GeneXus")
  endif
EndComposite
EndEventt
```

In this example, the URL "twitter://user?screen\_name=GeneXus" can be opened only if the Twitter app is installed.

### [Scope](#Scope)

**Object:** [Objects for Native Mobile applications development](https://wiki.genexus.com/commwiki/wiki?20087) only in user event  
**Generator:**[Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Notes](#Notes)

* On Apple, this method returns False, unless you set [Application Queries Schemes property](https://wiki.genexus.com/commwiki/wiki?29371).

### [Availability](#Availability)

As from [GeneXus X Evolution 3 RC (codename: Tilo)](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?24448,,)

### [See Also](#See+Also)

[Interop external object](https://wiki.genexus.com/commwiki/wiki?23734)  
[Interop.Open method](https://wiki.genexus.com/commwiki/wiki?23733)

### [Sample KB](#Sample+KB)

This KB provides an additional example of using Interop.CanOpen.

* [EventDay](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?22550,,)


|  |
| --- |
| **Backlinks** |
| [Interop external object](https://wiki.genexus.com/commwiki/wiki?23734) | [Interop external object (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?55183) |
| [Interop.Open method](https://wiki.genexus.com/commwiki/wiki?23733) |

---
