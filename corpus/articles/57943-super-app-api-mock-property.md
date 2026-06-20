---
title: "Super App API Mock property"
source_id: 57943
source_url: https://wiki.genexus.com/commwiki/wiki?57943
genexus_version: "18"
---

# Super App API Mock property

Specifies a mock Super App object that replicates the API structure of the real Super App.

### [Scope](#Scope)

**Objects:** [Mini App](https://wiki.genexus.com/commwiki/wiki?58037)  
**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)

### [Description](#Description)

This property facilitates the independent execution of a Mini App by providing a simulated version of the [Super App's API](https://wiki.genexus.com/commwiki/wiki?58207). This mock API serves as a substitute during the development and testing phases, allowing developers to work on the Mini App without relying on the actual implementation of the Super App's API, which resides within the Super App.

By referencing a Super App (Mock) object, you can emulate the behavior of the real Super App object within the Mini App's environment. This enables effortless testing and prototyping, ensuring that the Mini App works correctly even without direct access to the Super App.

**Note:** It's important to note that this functionality is applicable when launching the application from [GeneXus Project Navigator](https://wiki.genexus.com/commwiki/wiki?14974). It does not apply when the application is run standalone.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244).

### [See Also](#See+Also)

[Super App API External Object property](https://wiki.genexus.com/commwiki/wiki?57944)  
[Main Object property (for Mini Apps)](https://wiki.genexus.com/commwiki/wiki?53629)  
[Super App Source](https://wiki.genexus.com/commwiki/wiki?53457)


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?54244) | [Table of contents:GeneXus Super Apps and Mini Apps](https://wiki.genexus.com/commwiki/wiki?50899) | [Category:Mini App object](https://wiki.genexus.com/commwiki/wiki?58037) |
| [Super App API External Object property](https://wiki.genexus.com/commwiki/wiki?57944) | [Super App API Mocking](https://wiki.genexus.com/commwiki/wiki?58219) |

---
