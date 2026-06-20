---
title: "Translation exceptions property"
source_id: 13245
source_url: https://wiki.genexus.com/commwiki/wiki?13245
genexus_version: "18"
---

# Translation exceptions property

Lists the exceptions that must not be translated.

### [Scope](#Scope)

**Level:** [Environment](https://wiki.genexus.com/commwiki/wiki?7115)

### [Description](#Description)

When using [GeneXus Application Localization](https://wiki.genexus.com/commwiki/wiki?6330), there may be many string constants in an application that must not be translated. They can be marked as not translatable by preceding each one with the "!" (bang) sign. Doing so one at a time is usually an error-prone and time-consuming task.

In many situations, you will notice that untranslatable strings share certain patterns ([Regular Expressions (RegEx)](https://wiki.genexus.com/commwiki/wiki?4606)). To name a few untranslatable string constant patterns:

* String constants holding HTML (or XML) code usually start with a "<" and end with a ">" sign.
* Numeric constants only have numbers, a decimal separator, and an optional sign.
* String constants holding a single character are usually codes.

This property is intended as a "development time saver" holding a list of regular expressions. If a string constant matches any of these expressions, it is considered as if it were preceded by a “!” symbol (i.e. not translatable).

It will be considered when the value of the [Translation type property](https://wiki.genexus.com/commwiki/wiki?9126) is *Run-time* or *Static*.

Examples are: HTML code, SQL Statements (using the standard create/update/delete/insert keywords), strings representing numbers, underlining, etc. Regular expression syntax is described below (it is a partial list of the default regular expressions):

|  |  |
| --- | --- |
| [- ]?\d \.?\d\* | Strings representing numbers |
| [ \t\-\_=x\\*] | Underlining |
| #[0123456789ABCDEF]{6} | HTML color |
| .\*javascript.\* | Javascript code |
| <.\*> | XML or HTML code |

GeneXus incorporates a list of default values displayed in the property. They can be deleted and changed, and new ones can be entered using the associated editor.

`[imagen omitida: wiki id 19930]`

The *Add*, *Delete,* and *Edit* buttons will allow you to add, delete and change an exception. Case sensitivity can be changed with the *Toggle Case* button to determine the interpretation of uppercase and lowercase characters.

To enter or edit an exception, read the document [Regular Expressions (RegEx)](https://wiki.genexus.com/commwiki/wiki?4606) that explains the rules for writing exceptions.

### [Translating untranslatable string constants](#Translating+untranslatable+string+constants)

Having, for example, “<.\*>” as a Translation Exception so that HTML (or XML) tags are not translatable will make the string constant “<Enter>” to be considered untranslatable too. To translate the constant, follow one of the alternatives below:

* Replace the constant with:

format(“<%1>”, “Enter”)

Note that here the “Enter” constant is to be translated but not the “<%1>” constant.

* Delete the Translation Exception and in the code look for all the constants starting with “<” and ending with “>” to add a “!” symbol in front of them.

#### [Considerations](#Considerations)

Since [GeneXus 17 upgrade 4](https://wiki.genexus.com/commwiki/wiki?47936,,) the following exceptions were removed:

```
create[[:blank:]]+.*
delete[[:blank:]]+.*[[:blank:]]+from[[:blank:]]+.*
insert[[:blank:]]+into[[:blank:]]+.*
select[[:blank:]]+ .*[[:blank:]]+from[[:blank:]]+.*
truncate[[:blank:]]+table[[:blank:]]+.*
update[[:blank:]]+.*[[:blank:]]+set[[:blank:]]+.*
```

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [[How to apply changes](https://wiki.genexus.com/commwiki/wiki?17719)](#wiki%3F17719%2CApplying%2Bproperty%2Bchanges+How+to+apply+changes)

|  |
| --- |
| To apply the corresponding changes when the property value is configured, execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691). |

### [See Also](#See+Also)

[Translation type property](https://wiki.genexus.com/commwiki/wiki?9126)  
[Translate to language property](https://wiki.genexus.com/commwiki/wiki?13242)  
[Regular Expressions (RegEx)](https://wiki.genexus.com/commwiki/wiki?4606)
