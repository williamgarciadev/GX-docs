---
title: "SOAP Action property in Data Providers"
source_id: 56002
source_url: https://wiki.genexus.com/commwiki/wiki?56002
genexus_version: "18"
---

# SOAP Action property in Data Providers

Determines the SOAP action of the web service method in Data Provider objects.

### [Scope](#Scope)

**Objects:** [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258)

### [Description](#Description)

This SOAP Action is a logical name that is exposed in the WSDL and travels as a header in SOAP messages.

This property is offered when [Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480) = True and when [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446) = Use Environment property value or Yes.

**Note:** This property applies to all methods exposed. It is not possible to determine a different action for every method.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

### [Availability](#Availability)

This property is available since [GeneXus 18 Upgrade 7](https://wiki.genexus.com/commwiki/wiki?54241).

### [See Also](#See+Also)

SOAP Action property in Procedures
