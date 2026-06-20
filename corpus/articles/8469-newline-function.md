---
title: "NewLine function"
source_id: 8469
source_url: https://wiki.genexus.com/commwiki/wiki?8469
genexus_version: "18"
---

# NewLine function

Returns the string needed to 'skip a line' on the platform that it runs.

### [Syntax](#Syntax)

*NewLine()*

**Type returned:**  
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With for Smart Devices](https://wiki.genexus.com/commwiki/wiki?15974), [Work With for Web pattern](https://wiki.genexus.com/commwiki/wiki?25475)   
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453)

### [Samples](#Samples)

```
msg(Trim(&UserName) + '  you are registered to the meeting.' + NewLine() + '  See you there!.')
```

```
TextBlock.Caption = 'Welcome' + Newline() + &UserName
```


|  |
| --- |
| **Backlinks** |
| [Chr function](https://wiki.genexus.com/commwiki/wiki?13656) | [Confirm function](https://wiki.genexus.com/commwiki/wiki?31634) | [Format property](https://wiki.genexus.com/commwiki/wiki?46309) |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) | [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657) |
| [Msg function](https://wiki.genexus.com/commwiki/wiki?31635) |

---
