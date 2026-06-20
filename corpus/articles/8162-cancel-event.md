---
title: "Cancel Event"
source_id: 8162
source_url: https://wiki.genexus.com/commwiki/wiki?8162
genexus_version: "18"
---

# Cancel Event

To cancel the execution of a program when the user presses the ESC key or clicks the associated control.

### [Description](#Description)

#### [Win interface:](#Win+interface%3A)

When the user presses the ESC key or the control associated to the event, the execution cancels, returning to the caller object. The application ends if the object is main.

The associated controls may only be buttons.

#### [Web interface:](#Web+interface%3A)

When the user presses the control associated to the event, the execution cancels, closing the web browser.

The associated controls may be buttons, images, text blocks and read-only edit boxes.

**Note:** The GeneXus developer cannot associate any code to this event.

### [Scope](#Scope)

**Objects:** [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** .NET, Cobol, Java, RPG, Visual Basic, Visual FoxPro  
**Interfaces:** Web, Win

####
