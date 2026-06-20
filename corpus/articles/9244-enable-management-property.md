---
title: "Enable Management property"
source_id: 9244
source_url: https://wiki.genexus.com/commwiki/wiki?9244
genexus_version: "18"
---

# Enable Management property

Allows monitoring distributed applications using the JMX standard for Java applications and WMI for .NET applications.
Any JMX or WMI monitor can be used to read the information obtained.

### [Values](#Values)

|  |  |
| --- | --- |
| **No** | Does not generate information to evaluate the system behavior. This is the default value. |
| **Yes** | Generates information that can be analyzed using any JMX or WMI monitor. |

### [Scope](#Scope)

**Generators:** [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

Large applications need additional support to define whether they are feasible or not, that is to say, to confirm that they are not sure-fail applications.

In general it is required to get information on the system's behavior, identify critical application spots and establish if it will be necessary to reprogram them or modify their settings to change the detected behavior.

By setting Enable Management Property it is possible to monitor applications to help in the 'diagnosis' explained previously. As it runs, the application shows information in a JMX console, such as variables related to the connection pool, users, cursors, statements, procedures, etc.

In addition to publishing application variables, it allows you to change certain variables instantly through the console.

You can also execute certain operations such as recycling the connection pool or generating notifications when a variable reaches a value for which a prompt is to be triggered.

#### [Note](#Note)

In general JMX is used for distributed applications, but it can be used for 2-tier applications also: [Monitor 2-Tier applications](https://wiki.genexus.com/commwiki/wiki?5918,,).

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.

### [See Also](#See+Also)

[Instrumented property](https://wiki.genexus.com/commwiki/wiki?8971,,) (.NET)  
[Monitoring and Management of GX applications](https://wiki.genexus.com/commwiki/wiki?1997,,)


|  |
| --- |
| **Backlinks** |
| [.NET Platform restrictions](https://wiki.genexus.com/commwiki/wiki?39853) | [Applying property changes](https://wiki.genexus.com/commwiki/wiki?17719) | [Database performance from the GeneXus perspective](https://wiki.genexus.com/commwiki/wiki?26285) |
|
|

---
