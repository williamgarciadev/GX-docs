---
title: "Printer rule"
source_id: 11734
source_url: https://wiki.genexus.com/commwiki/wiki?11734
genexus_version: "18"
---

# Printer rule

Defines the printer form (a list of printer settings) to be used.

### [Syntax](#Syntax)

**Printer(**{ '*FormName'*| *att* | *&var* }**);**

**Where:**

*FormName | att | &var*Represent the printer's form name (i.e., ‘DefaultPrinter’). When using a variable or an attribute, it must be a Character data type.

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3),

### [Description](#Description)

The printer rule is used to select a printing form. When using the iSeries generator, this rule specifies the printer file to be used in the iSeries.

For each printer rule defined in any report or procedure, a form is generated in a file called [GXPRN.INI](https://wiki.genexus.com/commwiki/wiki?17091) (located where the application is executed) with the default values taken from the report or procedure.

When the object containing the printer rule is executed, the [INI](https://wiki.genexus.com/commwiki/wiki?17091) file is opened and the selected form is read to get the associated printer setting; the object is printed using these parameters.

#### [Win environment](#Win+environment)

You can use the GxSetFrm utility to set the desired value for each form defined; check [this](https://wiki.genexus.com/commwiki/wiki?13722,,) article for further information.

#### [Web environment](#Web+environment)

The [GXPRN.INI](https://wiki.genexus.com/commwiki/wiki?17091) file must be located in the application virtual directory when using C# generator; for the Java generator locate it in the web application's WEB-INF directory.

The file is automatically created once the report or procedure object is executed (only if the file does not exist); the GeneXus design values are set.  
If you want to modify the printer form settings, you have to:

* stop the application.
* modify the file manually.
* restart the application.

#### [iSeries environment](#iSeries+environment)

GeneXus uses the General Purpose library (QGPL) QPRINT Printer File by default. The Printer rule allows you to use a different Printer File instead of the QPRINT file, so you can apply whatever options you wish.

The file used must satisfy the following requirements:

* It must be a Program Defined File (Not DDS).
* The name cannot have invalid COBOL characters (such as underscore, etc.)
* The name's length cannot exceed 8 characters in RPG and 10 characters in COBOL.

The procedure suggested to define a Printer File is: copy the QPRINT file and then use the CHGPRTF (Change Printer File) command to set the desired options.

**Note**: For each rule or set of rules, you can force them to be triggered \_only\_ for certain environment(s). See more details in the following document: [Form-specific Events and Rules](https://wiki.genexus.com/commwiki/wiki?11735).

### [See Also](#See+Also)

[Printing with GeneXus](https://wiki.genexus.com/commwiki/wiki?5489)  
[Client side printing in web applications](https://wiki.genexus.com/commwiki/wiki?13692,,)  
[GXPRN.INI Format](https://wiki.genexus.com/commwiki/wiki?17091)


|  |
| --- |
| **Backlinks** |
| [GXPRN.INI Format](https://wiki.genexus.com/commwiki/wiki?17091) | [Printing text reports on the client machine without changing the printer settings](https://wiki.genexus.com/commwiki/wiki?28296) |
| [Web printing on client printer (without an applet)](https://wiki.genexus.com/commwiki/wiki?33912) |

---
