---
title: "SetFocus method"
source_id: 8836
source_url: https://wiki.genexus.com/commwiki/wiki?8836
genexus_version: "18"
---

# SetFocus method

Directs the user's input to the specified control.

### [Syntax](#Syntax)

*Control***.Setfocus()**  
  
**Where:**  
*Contro*l  
    Is the name of a control inserted in the form.

### [Scope](#Scope)

**Objects:** [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,),[Panel](https://wiki.genexus.com/commwiki/wiki?24829),[Work With pattern and Work With object](https://wiki.genexus.com/commwiki/wiki?15974)  
**Controls:** [Button](https://wiki.genexus.com/commwiki/wiki?6011), Check Boxes, Combo Boxes, [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599), Edits, [Forms](https://wiki.genexus.com/commwiki/wiki?14619), Grids, List Boxes, Radio Buttons  
**Generators:** 

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Samples](#Samples)

```
Event 'GetClient'
    GetCli.Call(CliCode, CliName)
    SupCod.Setfocus()
EndEvent
```

Suppose there's a button in a form that calls a procedure to obtain the client’s name given its code and you want to direct the input (locate the cursor) to the SupCode attribute after the call is performed. This is done by using this method with the SupCode attribute within the event associated to the button, as shown in the example.

**Note**: When this method is used on elements in a Grid, it is supported for the first row only.

### [See Also](#See+Also)

[Focus control property](https://wiki.genexus.com/commwiki/wiki?8838)  
[IsValid Event for Web Applications](https://wiki.genexus.com/commwiki/wiki?6564)
