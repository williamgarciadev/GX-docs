---
title: "Confirm function"
source_id: 31634
source_url: https://wiki.genexus.com/commwiki/wiki?31634
genexus_version: "18"
---

# Confirm function

Displays a message that allows capturing end user confirmation.

### [Syntax](#Syntax)

**Confirm(***Message***)**

**Where:**  
  
*Message*  
    The message to be displayed. It can be constant or stored in a variable. It is possible to add [newlines](https://wiki.genexus.com/commwiki/wiki?8469) in the string.

**Type Returned:**  
Boolean

**Note**: It indicates if the end-user has confirmed or not. Its value can not be captured. In case the end-user cancels the operation, the composite block is aborted (It does not continue with the next line of execution). If your want to capture its value, you must use [Interop Confirm method](https://wiki.genexus.com/commwiki/wiki?17334).

### [Scope](#Scope)

**Objects**: [Panel](https://wiki.genexus.com/commwiki/wiki?24829), [Work With](https://wiki.genexus.com/commwiki/wiki?15974)   
**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Angular](https://wiki.genexus.com/commwiki/wiki?42550)

### [Samples](#Samples)

```
Event 'Say hello'
    Composite
        &Message = "Hello user" + Newline() + "Do you feel good today?"
        Confirm(&Message)
        Msg("I'm glad you're ok!",nowait)
    EndComposite
Endevent
```

In case the end-user presses the "ok" button, it will display the message. Otherwise, no message will be displayed.

`[imagen omitida: wiki id 31648]`


|  |
| --- |
| **Backlinks** |
| [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657) |

---
