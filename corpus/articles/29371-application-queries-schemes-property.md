---
title: "Application Queries Schemes property"
source_id: 29371
source_url: https://wiki.genexus.com/commwiki/wiki?29371
genexus_version: "18"
---

# Application Queries Schemes property

Specifies the URL schemes you want the app to be able to use with Interop.CanOpen(), required for iOS 9.0 and later.
Values should be separated with commas (,).

### [Scope](#Scope)

**Objects:** [Menu](https://wiki.genexus.com/commwiki/wiki?16321), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974) (Only [Main Objects](https://wiki.genexus.com/commwiki/wiki?5770))  
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

For each URL scheme you want your app to use with the CanOpen() method, add it as a string in this list.

### [Values](#Values)

A comma-separated list of required schemes.

### [Samples](#Samples)

```
twitter,fb
```

To query whether Twitter.app and/or Facebook.app are installed.

### [See Also](#See+Also)

[LSApplicationQueriesSchemes documentation](https://developer.apple.com/library/prerelease/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW14)


|  |
| --- |
| **Backlinks** |
| [Interop.CanOpen method](https://wiki.genexus.com/commwiki/wiki?23732) | [Native Mobile Main object properties](https://wiki.genexus.com/commwiki/wiki?17817) |

---
