---
title: "External Name property"
source_id: 48445
source_url: https://wiki.genexus.com/commwiki/wiki?48445
genexus_version: "18"
---

# External Name property

Specifies the external name used when the variable is a service parameter.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258)  
**Level:** [Variable](https://wiki.genexus.com/commwiki/wiki?7375)

### [Description](#Description)

This property lets you define the name of the corresponding parameter to use in the service URL. If the property is not set, the default name for the parameter is the capitalized variable name.

It is available for the [Java](https://wiki.genexus.com/commwiki/wiki?12258) generator since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,) and for the [.NET](https://wiki.genexus.com/commwiki/wiki?38604) and [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892) generators since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [Samples](#Samples)

This property is only valid for variables defined in [API object](https://wiki.genexus.com/commwiki/wiki?46151)s.

If you have an API object named "API1" and you have defined a GetCustomerDetails service that receives a CustomerNumber as a parameter:

*GetCustomerDetail( in:&CustomerNumber, out:&CustomerInfo) =>  .....*

To avoid using the full "CustomerNumber" as a parameter name, you can set the **ExternalName** property for the CustomerNumber variable:  **ExternalName = number**

The URL for the service call should be:

*...API1/GetCustomerDetail?number=33*

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Build with this Only](https://wiki.genexus.com/commwiki/wiki?5693) of the object.


|  |
| --- |
| **Backlinks** |
| [Azure Cosmos DB external data store](https://wiki.genexus.com/commwiki/wiki?53330) |

---
