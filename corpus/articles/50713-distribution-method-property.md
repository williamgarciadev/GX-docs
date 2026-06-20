---
title: "Distribution Method property"
source_id: 50713
source_url: https://wiki.genexus.com/commwiki/wiki?50713
genexus_version: "18"
---

# Distribution Method property

Indicates what type of distribution should be used for the generated Apple application when using Build IPA (Local) Execution Type.

### [Values](#Values)

|  |  |
| --- | --- |
| **Ad Hoc** | The application is built and signed with an Ad-hoc provisioning profile to be distributed to testers. |
| **App Store** | The application is built and signed with a distribution provisioning profile for TestFlight and App Store publishing. |
| **Development** | The application is built and signed with a development provisioning profile to be distributed to testers. |
| **Enterprise** | The application is built and signed for In-house distribution. |

### [Scope](#Scope)

**Generators:** [Apple](https://wiki.genexus.com/commwiki/wiki?14917)  
**Level:** Front end

### [Description](#Description)

Apple applications can be built and distributed for different purposes. This property allows selecting a Distribution Method for the generated application.

The options are based on the [Distribution methods](https://help.apple.com/xcode/mac/current/#/dev31de635e5) provided by the Apple platform.

This property is only available when the [Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658) is set to "*Build IPA (Local).*"

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

To apply the corresponding changes when the property value is configured, Build the [Main Object](https://wiki.genexus.com/commwiki/wiki?5770).

### [Availability](#Availability)

This property is available since [GeneXus 17 Upgrade 10](https://wiki.genexus.com/commwiki/wiki?49971,,).

### [See Also](#See+Also)

[Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658)  
[Deployment and Prototyping in the Apple Platform](https://wiki.genexus.com/commwiki/wiki?16234)


|  |
| --- |
| **Backlinks** |
| [Execution Type property](https://wiki.genexus.com/commwiki/wiki?18658) |

---
