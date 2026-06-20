---
title: "Workflow Setting Data Type"
source_id: 15084
source_url: https://wiki.genexus.com/commwiki/wiki?15084
genexus_version: "18"
---

# Workflow Setting Data Type

This Data Type represents a [Workflow Setting](https://wiki.genexus.com/commwiki/wiki?15097) and it is provided by the [Workflow API](https://wiki.genexus.com/commwiki/wiki?51350).

### [Properties](#Properties)

|  |  |  |  |
| --- | --- | --- | --- |
| **Property** | **Type** | **Access** | **Description** |
| Id | [WorkflowSettingId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Id |
| Value | [WorkflowValue](https://wiki.genexus.com/commwiki/wiki?15734) | Read/Write | Value |
| Visible | Boolean | Read | Indicates whether the setting is visible. |
| Description | [WorkflowDescription](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Description |
| Dependency | [WorkflowSettingId](https://wiki.genexus.com/commwiki/wiki?15734) | Read | If this setting has a dependency on another setting, it represents the identifier of that setting. |
| DependencyValue | [WorkflowValue](https://wiki.genexus.com/commwiki/wiki?15734) | Read | If dependency is not null, then dependency value represents the value it depends on. |
| DefaultValue | [WorkflowValue](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Default value of this setting |
| IsDefault | Boolean | Read | Indicates whether the setting is set to its default value. |
| IsPassword | Boolean | Read | Indicates whether the setting represents a password. |
| ControlType | [WorkflowSettingControlType](https://wiki.genexus.com/commwiki/wiki?15734) | Read | Indicates whether this setting is an edit or a combo. |
| EnumValues | Collection ([WorkflowSettingValue](https://wiki.genexus.com/commwiki/wiki?56532,,)) | Read | List of possible values that a WorkflowSetting instance can have when its ControlType property is set to combo. |


|  |
| --- |
| **Backlinks** |
| [GeneXus 18 Upgrade 8](https://wiki.genexus.com/commwiki/wiki?54242) | [HowTo: Create a settings menu using the Workflow API](https://wiki.genexus.com/commwiki/wiki?54056) | [Category:Workflow Data Types](https://wiki.genexus.com/commwiki/wiki?17240) |
| [Workflow Server Data Type](https://wiki.genexus.com/commwiki/wiki?11671) | [WorkflowUser Data Type](https://wiki.genexus.com/commwiki/wiki?17273) |

---
