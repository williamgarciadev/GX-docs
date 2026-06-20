---
title: "Triggering context for Events and Rules"
source_id: 11735
source_url: https://wiki.genexus.com/commwiki/wiki?11735
genexus_version: "18"
---

# Triggering context for Events and Rules

Defines specific rules and events for each user interface (Windows or GUI, Web or HTML and Text).

### [Syntax](#Syntax)

EnvironmentAttribute { *rule* | *event* } | { { *rule* … | *event* … } }

**Where:**

*EnvironmentAttribute*  
     Specifies the environment attribute used. The possible values are:

* [win]: Indicates that the events and rules which follow must only be applied to the Windows or GUI forms. In this case, the validation is done the moment the information is saved and sent to the specifier only if the user interface of the associated generator is "Win" type.
* [web]: The events and rules that follow are only valid for the Web or HTML form. The information is sent to the specifier only if the user interface of the associated generator is "Web".
* [text]: The events and rules that follow must only be applied to char based user interfaces.
* [business]: This is the default value and specifies that it applies to all forms; thus, this information is always sent to the specifier. An alternative way to achieve this is to use the previous identifiers concatenated [win] [web] [text].

*rule*  
     Specifies a rule or list of rules (separated by semicolon) associated to the object.

*event*  
     Details an event or list of events associated to the object.

**Note:**

   There are two possible syntaxes:

* **Individual:** This allows you to apply the identifier by event or rule; i.e., individually. To do so, you must include the associated identifier and then, in the following line, the rule/event to be executed.
* **By Block:** Applies one or several attributes to a group of rules or events. You must enclose those rules or events between keys ({ }).

### [Scope](#Scope)

**Objects:**[Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Work Panel](https://wiki.genexus.com/commwiki/wiki?7387,,), [Web Panel Web Layout](https://wiki.genexus.com/commwiki/wiki?8132) (rules and events)  
**Interfaces:** Text, Web, Win

### [Description](#Description)

The [win], [web], [text] and [business] environment attributes allow you to discriminate the environment where the related events and rules will be executed. The user can specify the rules and events according to the form.

Due to backward compatibility with Knowledge Bases of previous GeneXus versions, when these identifiers (environment attributes) are not used the [business] option is assumed by default.

### [Samples](#Samples)

**Example 1**

The following example shows a detailed use of the Individual syntax applied to rules/events.

```
[win] // Rule for GUI environments
Noaccept(CliCod) If Insert On AfterValidate;
[win][web] // Event for Win and Web environments
Event Start
       Call( PSettings , &UserId)
EndEvent // Start
```

The NoAccept rule will only be applied in Windows or GUI environments, while the Start event is valid in Win and Web environments.

**Example 2**

The next example shows the use of the Block syntax.

```
[win]
{
parm(&CliCod , &Mode);
Noaccept&CliCod);
CliCod = &CliCod If Update Or Delete;
CliCod = udp( PNumber , ‘Cli’ ) If Insert On AfterValidate;
}
[win][text]
{
Event Start
       Call(PSettings, &UserId)
EndEvent
Event ‘User’ 8
       // User Event
EndEvent
}
```

The first one specifies that the list of rules within the block delimited by {} must be executed only in Win environments. The other example specifies that the group of events within the block delimited by {} must be executed in Win and Text environments.

### [See Also](#See+Also)

[Web Transactions](https://wiki.genexus.com/commwiki/wiki?8060,,)  
[Transaction rules](https://wiki.genexus.com/commwiki/wiki?8213)  
[Events in Transactions](https://wiki.genexus.com/commwiki/wiki?8042)  
[Web Panel rules](https://wiki.genexus.com/commwiki/wiki?8288)


|  |
| --- |
| **Backlinks** |
| [Printer rule](https://wiki.genexus.com/commwiki/wiki?11734) | [Category:Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) |

---
