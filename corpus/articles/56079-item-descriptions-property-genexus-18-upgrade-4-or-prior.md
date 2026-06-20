---
title: "Item Descriptions property (GeneXus 18 Upgrade 4 or prior)"
source_id: 56079
source_url: https://wiki.genexus.com/commwiki/wiki?56079
genexus_version: "18"
---

# Item Descriptions property (GeneXus 18 Upgrade 4 or prior)

Indicates the attribute whose data (descriptions that contain semantic meaning) will be accepted and displayed instead of the corresponding identifiers.

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), [Android](https://wiki.genexus.com/commwiki/wiki?14453), [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Controls:** Attribute/Variable (Control Type: [Dynamic Combo Box](https://wiki.genexus.com/commwiki/wiki?7598), [Dynamic List Box](https://wiki.genexus.com/commwiki/wiki?7599))

### [Description](#Description)

This property is offered for attributes/variables whose [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) is set to Descriptions.

Consider an attribute/variable that stores an identifier (i.e. CountryId) with its [InputType property](https://wiki.genexus.com/commwiki/wiki?8799) set to Descriptions. The **ItemDescriptions property** allows indicating an attribute whose data will be accepted and displayed (i.e. CountryName) instead of the CountryId.

Thus, on the screen, the CountryId attribute will be “disguised” as CountryName. End users will see a field to type/select a CountryName, but the attribute is not CountryName. On the contrary, it is the CountryId attribute.

When an end user writes “Uruguay”, an internal search is performed to retrieve the code that corresponds to "Uruguay". That value (for example: 1) is stored in the CountryId attribute. This is totally transparent for the end user.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design time.

### [See Also](#See+Also)

[Item Values property](https://wiki.genexus.com/commwiki/wiki?8808)
