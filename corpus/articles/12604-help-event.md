---
title: "Help Event"
source_id: 12604
source_url: https://wiki.genexus.com/commwiki/wiki?12604
genexus_version: "18"
---

# Help Event

This event invokes the help for an object, attribute or variable. It occurs when the user presses the F1 key or clicks the control associated to the event.

### [Description](#Description)

This standard event is used to invoke the object, attribute, or variable’s help. It occurs when the F1 key or associated control is pressed.

##### [Win Interface:](#Win+Interface%3A)

If the attribute or variable has focus, their help will be invoked. Otherwise the object’s help is invoked.

The associated controls can only be buttons.

##### [Web Interface:](#Web+Interface%3A)

Only the object’s help can be invoked.

The associated controls can be buttons, images, text blocks and read-only edit boxes.

The GeneXus developer cannot associate any code to this event.

### [Scope](#Scope)

**Objects:** [Transactions](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panels](https://wiki.genexus.com/commwiki/wiki?6916), Work Panels  
**Languages:** .NET, Java, Ruby (up to GeneXus X Evolution 3), Cobol, RPG, Visual FoxPro (up to GeneXus X Evolution 3)  
**Interfaces:** Web, Win (up to GeneXus X Evolution 3)

### [See also](#See+also)

[Application Help](https://wiki.genexus.com/commwiki/wiki?12152)
