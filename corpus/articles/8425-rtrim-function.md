---
title: "RTrim function"
source_id: 8425
source_url: https://wiki.genexus.com/commwiki/wiki?8425
genexus_version: "18"
---

# RTrim function

Returns the specified character expression with all trailing blanks removed.

### [Syntax](#Syntax)

**RTrim(** *St**r* **)**  
  
**Where:**  
  
*Str*   
    Is the character expression from which you want to trim all trailing blanks.

**Type Returned:**  
Character

### [Scope](#Scope)

**Objects****:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), RPG, Visual FoxPro (up to GeneXus X Evolution 3), [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453),
[Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Description](#Description)

Returns a character string that results from removing the trailing blanks from the character expression *Str*.

**Note**: In Cobol for iSeries this function is ignored because the strings length is fixed.

### [Samples](#Samples)

```
&Text = RTrim("My character expression    ")

// Result of &Text: “My character expression”
```

### [See Also](#See+Also)

[Trim function](https://wiki.genexus.com/commwiki/wiki?8424)  
[LTrim function](https://wiki.genexus.com/commwiki/wiki?8423)  
[TrimEnd method](https://wiki.genexus.com/commwiki/wiki?12719)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [LTrim function](https://wiki.genexus.com/commwiki/wiki?8423) | [Methods and Functions matching](https://wiki.genexus.com/commwiki/wiki?12530) | [PadL function](https://wiki.genexus.com/commwiki/wiki?8475) | [PadLeft method](https://wiki.genexus.com/commwiki/wiki?12705) |
| [PadR function](https://wiki.genexus.com/commwiki/wiki?8476) | [PadRight method](https://wiki.genexus.com/commwiki/wiki?12706) | [Query object expressions](https://wiki.genexus.com/commwiki/wiki?11782) | [Trim function](https://wiki.genexus.com/commwiki/wiki?8424) |
| [Trim method](https://wiki.genexus.com/commwiki/wiki?12718) |

---
