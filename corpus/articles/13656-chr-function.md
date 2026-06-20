---
title: "Chr function"
source_id: 13656
source_url: https://wiki.genexus.com/commwiki/wiki?13656
genexus_version: "18"
---

# Chr function

Inserts special characters into a string, such as a carriage return. In other words, it allows you to retrieve a character from the ASCII table (in modern languages, from the Unicode table)

### [**Syntax**](#Syntax)

**Chr(***Number***)**

**Where:**  
   *Number*Is the number corresponding to the ASCII table one.

**Type returned:**  
Character(1)

### [Scope](#Scope)

**Objects:**[Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,)

### [Samples](#Samples)

You want to insert a carriage return in a memo field because the message to show is too long. By inserting this special character in the middle, the message will be shown in two lines. For this, you need to use the 13.

```
&Mssg = Concat("This is an example about ", Chr(13))
&Txt  = Concat(&Mssg, " the CHR standard function")
TextBlock1.Caption = &Txt
```

**Note**: Unicode's values are supported in Apple since [GeneXus 17 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?49616,,)

### [**See Also**](#See+Also)

[NewLine function](https://wiki.genexus.com/commwiki/wiki?8469)  
[Asc function](https://wiki.genexus.com/commwiki/wiki?13973)


|  |
| --- |
| **Backlinks** |
| [Asc function](https://wiki.genexus.com/commwiki/wiki?13973) |

---
