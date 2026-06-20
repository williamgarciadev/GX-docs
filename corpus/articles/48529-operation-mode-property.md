---
title: "Operation mode property"
source_id: 48529
source_url: https://wiki.genexus.com/commwiki/wiki?48529
genexus_version: "18"
---

# Operation mode property

When set to Single read, the control reads the first code and then stops scanning. When Continuous read is selected, it reads all the codes it can while the control is visible, non-stop.

### [Values](#Values)

|  |
| --- |
| **Continuous read** |
| **Single read** |

### [Scope](#Scope)

**Generators:** [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Scanner](https://wiki.genexus.com/commwiki/wiki?15310))  
**Level:** [Attribute](https://wiki.genexus.com/commwiki/wiki?7240), [Domain](https://wiki.genexus.com/commwiki/wiki?7221), [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

This property is offered in [Panel object](https://wiki.genexus.com/commwiki/wiki?24829)s for variables or attributes whose [Control Type property](https://wiki.genexus.com/commwiki/wiki?9550) = Scanner.

It enables the [Scanner Control](https://wiki.genexus.com/commwiki/wiki?15310) to control how the reading will be handled.

Use the *CodeRead* or *ControlValueChanged* events to process it.  
The difference between both events is that *CodeRead* will scan non-stop and possibly repeat the same detection, while *ControlValueChanged* will not repeat consecutive reads.

This property is available in a [Panel object](https://wiki.genexus.com/commwiki/wiki?24829) with a variable or attribute Scanner [control](https://wiki.genexus.com/commwiki/wiki?9550).

#### [Single Read](#Single+Read)

The control reads the first code and then stops scanning.

#### [Continuous Read](#Continuous+Read)

The control reads all the codes it can while the control is visible (non-stop). Set the control *Visible* property to false if you want to stop reading codes.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [Samples](#Samples)

Define *&code1* and *&code2* as Varchar variables and set the Scanner control type.

To process different codes, use the *ControlValueChanged* event:

```
Event &code1.ControlValueChanged // Inline + Continuous Read
    Composite
        &CodesCollection.Add(&code1)
    EndComposite
Endevent
```

To process all codes, use the *CodeRead* event:

```
Event &code2.CodeRead // Inline + Continuous Read
    Composite
        &CodesCollection.Add(&code1)
    EndComposite
Endevent
```

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).

### [See Also](#See+Also)

[Display mode property](https://wiki.genexus.com/commwiki/wiki?48528)


|  |
| --- |
| **Backlinks** |
| [Scanner Control](https://wiki.genexus.com/commwiki/wiki?15310) |

---
