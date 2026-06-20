---
title: "HowTo: Migrate an External Object for iOS from Evolution 3 to GeneXus 15"
source_id: 33805
source_url: https://wiki.genexus.com/commwiki/wiki?33805
genexus_version: "18"
---

# HowTo: Migrate an External Object for iOS from Evolution 3 to GeneXus 15

## [Introduction](#Introduction)

External Objects (and User Controls) for iOS, created to be used in [GeneXus X Evolution 3](https://wiki.genexus.com/commwiki/wiki?20247,,), will need to be modified to be used in [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,).

The reason for this is that the Flexible Client provided by GeneXus changed from one monolithic framework to several smaller frameworks. For that reason, the previous Xcode project linked to the old framework will not work in the new version.

## [Migration process](#Migration+process)

### [Start a new project](#Start+a+new+project)

For [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,) we provide an Xcode template that already links to all the necesary frameworks, so it is highly recommended that you start a new Xcode project.

See also: [Framework template for iOS User Controls or External Objects](https://wiki.genexus.com/commwiki/wiki?32508).

But don't worry, most of the code you already have will still work with some minor modifications.

### [Programming language](#Programming+language)

Even though the generated code changed from Objective-C (in Evolution 3) to Swift (in version 15), you can still use your preferred programming language to develop your user controls or external objects. If you already have Objective-C code, it can be used in [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,) taking into account some minor modifications.

### [Imports](#Imports)

In Evolution 3, you had to #import the specific header files. For example:

```
#import "GXExternalObjectBase.h"
```

Now you can @import the necessary modules. In Objective-C it would be:

```
@import GXStandardClasses;
```

and in Swift:

```
import GXStandardClasses
```

Note: there is no easy way to tell in which module each class is. As a general rule, most of the classes you may need are located in the following frameworks: *GXStandardClasses*, *GXCoreUI* or *GXCoreBL*.

### [Numeric data types](#Numeric+data+types)

Note: this is only valid when the external object is called from generated code, not when called from a user event.

The Objective-C generator used **NSNumber** and **NSDecimalNumber** for the numeric attributes and variables.

Now, the Swift generator uses **Int**(1), **Int64**(2) and **Decimal**(3), so you may need to convert some of your methods.

### [Method definitions](#Method+definitions)

Note: this is only valid when the external object is called from generated code, not when called from a user event.

The GeneXus X Evolution 3 Objective-C generator required the methods to receive the parameters in an NSArray.

This is no longer the case for the GeneXus 15 Swift generator, now the parameters must be comma-separated and without name label.

For example, suppose your external object has a method *RepeatString* that takes a *Character* and a *Numeric* argument, and it repeats the string the number of times indicated by the second parameter.

The Objective-C definition of this method would be:

```
- (NSString *)repeatString:(NSArray *)params;
```

Now, in Swift it should be:

```
func repeatString(_ str: String, _ num: Int) -> String
```

Tip: since you already have the Objective-C implementation, and you probably don't want to migrate the implementation to Swift, a quick solution would be to provide an extension in Swift that calls the Objective-C method. In this case, you need to create a new *"MyExternalObjectImplementation".swift*  file containg something similar to:

```
public extension MyExternalObjectImplementation {
    public class func repeatString(_ str: String, _ num: Int) -> String {
        let params: Array<Any> = [str, NSNumber(value: num)]
        return MyExternalObjectImplementation().repeatString(params)
    }
}
```

Actually, since GeneXus 15 you don't need the method receiving the parameters array, so if you already have a method with the desired parameters you can directly call your implementation from the swift extension; for example

```
public extension MyExternalObjectImplementation {
    public class func repeatString(_ str: String, _ num: Int) -> String {
        return MyExternalObjectImplementation().repeatString(message:str, count: num)
    }
}
```

For this to work you need to modify the MainName-Bridging-Header.h file from the "GeneXusInstallDir"\iOS\Templates\iOS\_Genexus location and add the import of your objects so the project compiles, for example

```
#import "MyExternalObjectImplementation.h"
```

Why? Because GeneXus 15 uses Swift and we are calling an Objective-C implementation; for technical details [check here](https://developer.apple.com/library/content/documentation/Swift/Conceptual/BuildingCocoaApps/MixandMatch.html#//apple_ref/doc/uid/TP40014216-CH10-XID_75).


(1) **Int** is used for the Numeric data type in GeneXus, without decimals and up to a length of 9.

(2) **Int64** is used for the Numeric data type in GeneXus, without decimals and of length larger than 9.

(3) **Decimal** is used for the Numeric data type in GeneXus, with decimals and of any length.

## [Scope](#Scope)

|  |  |
| --- | --- |
| **Objects** | [External object](https://wiki.genexus.com/commwiki/wiki?18072) |
| **SD Generators** | [iOS](https://wiki.genexus.com/commwiki/wiki?14917) |

## [Availability](#Availability)

As from [GeneXus 15](https://wiki.genexus.com/commwiki/wiki?28265,,)

---
