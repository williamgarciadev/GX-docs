---
title: "Msg command"
source_id: 31635
source_url: https://wiki.genexus.com/commwiki/wiki?31635
genexus_version: "18"
---

# Msg command

Displays warning messages.

### [Syntax](#Syntax)

**Msg(** Message [ , nowait | status ] **)**

**Where:**  
*Message*  
    The message to be displayed. It can be constant or stored in a variable. It is possible to add [newlines](https://wiki.genexus.com/commwiki/wiki?8469) in the string.

*Mode*  
    There are two modes to display the message, each one with an associated constant value:

* *nowait*

Stores the message in an internal variable and processing continues. The user will not see the message until program processing ends. This improves program performance as less screen input/output is required.  
For Native Mobile applications, it works as a "toast message".

* *status*

The message is displayed at the moment it is originated. It is useful for giving the user information about program processing status.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908),[Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Panel](https://wiki.genexus.com/commwiki/wiki?24829)  
**Generators:**[Apple](https://wiki.genexus.com/commwiki/wiki?14917), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [.NET](https://wiki.genexus.com/commwiki/wiki?38604),  [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Considerations](#Considerations)

* This message option degrades performance due to the required screen input/output.
* It is used to display the literal, variable, or character expression contents in the message popup window (or message line, depending on the working environment).  
  The moment when the user actually sees the message will depend on where the command is declared and on the option selected.
* When using a variable, GeneXus controls, at specification time, that the variable type is Character.
* When the Mode option is not specified:
  + **Web Panels and Transactions**  
    It sends the message and waits for the Enter key to be pressed.
  + **Procedures**  
    See s*tatus* option.
  + **Panels**  
    Msg has no effect in Start, Refresh, and Load events in Panels as it is considered a [Client-side event](https://wiki.genexus.com/commwiki/wiki?24332).

**Note**: To customize the text format, please refer to [HowTo: Format plain text programmatically](https://wiki.genexus.com/commwiki/wiki?31657). Only available since [GeneXus 15](https://wiki.genexus.com/commwiki/com.gxwiki.wiki?28265,,).

### [Samples](#Samples)

```
Msg("Hello user." + newline() + "Have a good day!")
Msg(&Today)
Msg(Format('B: %1', B))                   // Where B is Character type
Msg(Concat('Entered Date: ',  DtoC(C)))   // Where C is Date type.
Msg(Concat('Entered Date Hour', TtoC(D))) // Where and D is Datetime type.
&var = "Hello user." + newline() + "And on this line I say: good day to you"
Msg(&var, nowait)                         // Where &var is character type
```

### [See Also](#See+Also)

[Msg rule](https://wiki.genexus.com/commwiki/wiki?6854)  
[Format function](https://wiki.genexus.com/commwiki/wiki?8406)  
[Client-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24332)  
[Server-side Events in Native Mobile Applications](https://wiki.genexus.com/commwiki/wiki?24234)


|  |
| --- |
| **Backlinks** |
| [A03:2021 - Injection](https://wiki.genexus.com/commwiki/wiki?50183) | [Business Component GetOldValues method](https://wiki.genexus.com/commwiki/wiki?23804) |
| [Business Component Mode method](https://wiki.genexus.com/commwiki/wiki?23790) | [Commands in Procedures](https://wiki.genexus.com/commwiki/wiki?7924) | [Commands in Transactions](https://wiki.genexus.com/commwiki/wiki?8649) | [DesignOps - Conventions](https://wiki.genexus.com/commwiki/wiki?46872) |

---
