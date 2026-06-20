---
title: "SRC Error Codes and messages"
source_id: 38589
source_url: https://wiki.genexus.com/commwiki/wiki?38589
genexus_version: "18"
---

# SRC Error Codes and messages

SRC is an abbreviation of the source term. The following list shows the error messages related to the GeneXus source that can appear in the Output window when you try to save an [object](https://wiki.genexus.com/commwiki/wiki?1866).

| Code | Message |
| --- | --- |
|  | |
| **src0202** | **'****%1****'** **is not in a table.** |
|  | This message informs you that the attribute is not present either physically or logically in any table. It is defined in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) because at some point it was part of the model, but now it is not in a table. |
|  | |
|
|  | |
| **src0020** | **Line** **is too long.** |
|  | This message informs you that the length of a code line is longer than allowed. |
|  | |
| **src0206** | **'%1' command is out of scope.** |
|  | This message informs you that a certain command is being used inside an object or section that is not allowed. |
|  | |
| **src0213** | **'%1' invalid date constant; expected format: #YYYY-MM-DD HH:MM:SS.SSS#** |
|  | This message is displayed when you assemble several values to create a date but the format is incorrect. |
|  | |
| **src0216** | **'%1' invalid property.** |
|  | This error informs you that an [SDT](https://wiki.genexus.com/commwiki/wiki?2427) property or External Object property is being used in a GeneXus object but the property was removed and no longer exists in the SDT or External Object. |
|  | |
| **src0222** | **%1 is a deprecated %2.** |
|  | This warning message indicates that a function, rule, method, etc., used in an object is deprecated.  **Sample:**src0222: 'Deletefile' is a deprecated function. (Web Panel 'WebPanel1' Events, Line: 6, Char: 6, Details) |
|  | |
| **src0227** | **Conflict between %1 Function and Object Name.** |
|  | This warning message is displayed when an object in the KB has the same name as a function. For example, GeneXus offers the [Color function](https://wiki.genexus.com/commwiki/wiki?8345), so, if an object has the same name, this error will be displayed. To avoid this warning, rename the object so that the conflict disappears. |
|  | |
| **src0229** | **%1****is ambiguous. There is a program name and an image with the same name.** |
|  | This warning message is displayed when a code line cannot be solved because an object has the same name as an image. To solve this error, rename one of them or precede in the code line the name with **obj:** or **image:** as shown below.   ``` img.FromImage(image:GenexusUnanimo.Favorite) ``` |
|  | |
| **src0246** | **Call to non-defined object '%1'** |
|  | Informational message displayed when the object '%1' is an external program (look at [Call command](https://wiki.genexus.com/commwiki/wiki?8260) for additional information); an external program is not modeled inside the Knowledge Base, you must provide its implementation or a compilation error will be found.    Note: [FTP functions](https://wiki.genexus.com/commwiki/wiki?8393) are modeled as external programs (they are not a GeneXus standard function even when the [standard classes](https://wiki.genexus.com/commwiki/wiki?18859) can provide its implementation). |
|  | |
| **src0274** | **Last** **parameter cannot be omitted.** |
|  | This message is displayed when you are applying a method to an object, variable, etc., the method accepts optional parameters, and you have left a comma before the final parenthesis.  The last parameter you decide to specify must be followed by the final parenthesis. On the other hand, if you specify something like &var.method(par1,) or &var.method(par1,,,,) this message will be displayed as an error or warning depending on the case.  If you don't want to specify an optional parameter in the middle, you can define &var.method(par1,,par3) but if you don't want to specify some last optional parameters, you only have to omit them. |
|  | |
| **src0287** | **Program %1 does not exist.** |
|  | This message is displayed when you invoke an object that does not exist in the KB. |
|  | |
| **src0294** | **Unknown function %1.** |
|  | This message is displayed when you invoke an object that returns a value and the object is not defined in the KB. |
|  | |
| **src0297** | **Variables cannot be used in formulas.** |
|  | This message is displayed when you use a variable in a formula. Remember that Variables are local and formulas are global. Ref.: [Global Formulas](https://wiki.genexus.com/commwiki/wiki?6440) |
|  | |
| **src0299** | **Wrong number parameters: %1 expects at least %2 parameters.** |
|  | This message is displayed when a GeneXus function -like 'addyr'- requires a different number of parameters than those declared. |
|  | |
| **src0306** | **%1 subroutine is defined but never used.** |
|  | This message notifies that an object has a subroutine defined but not called. |
|  | |
| **src0310** | **%1 is not a transaction or transaction level.** |
|  | This message notifies that the name referenced as a [Base Transaction](https://wiki.genexus.com/commwiki/wiki?25418) next to a For each command is incorrect because there is no Transaction with that name nor a TransactionName.LevelName. |
|  | |
| **src0311** | **Conflict between %1 rule and Object Name.** |
|  | This warning message is displayed when an object in the KB has the same name as a rule. For example, GeneXus offers the [Order rule](https://wiki.genexus.com/commwiki/wiki?8256), so, if an object has the same name, this error will be displayed. To avoid this warning, rename the object so that the conflict disappears. |
|  | |
| **src0312** | **'%1' command is out of scope. It is not guaranteed to work.** |
|  | This message informs you that a certain command is being used inside an object or section that is not allowed. |

## [See also](#See+also)

* [Reorganization Error Codes and Messages](https://wiki.genexus.com/commwiki/wiki?5952)
* [Reorganization Operation Error Codes and messages](https://wiki.genexus.com/commwiki/wiki?5965)


|  |
| --- |
| **Backlinks** |
| [Toc:Coded Messages](https://wiki.genexus.com/commwiki/wiki?47288) | [Disabled warnings property](https://wiki.genexus.com/commwiki/wiki?8009) | [GeneXus deprecated functions, methods, and rules](https://wiki.genexus.com/commwiki/wiki?6620) |
| [Warnings treated as errors property](https://wiki.genexus.com/commwiki/wiki?8010) |

---
