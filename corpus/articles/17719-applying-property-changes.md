---
title: "Applying property changes"
source_id: 17719
source_url: https://wiki.genexus.com/commwiki/wiki?17719
genexus_version: "18"
---

# Applying property changes

It is important for GeneXus developers to be aware of what they have to do, after changing [object](https://wiki.genexus.com/commwiki/wiki?1866) properties and [general preferences](https://wiki.genexus.com/commwiki/wiki?7109), to be sure the changes are applied to the generated application, specially for properties in the following levels:

* [General Preferences](https://wiki.genexus.com/commwiki/wiki?7109)
  + [Version](https://wiki.genexus.com/commwiki/wiki?7860)
  + [Environment](https://wiki.genexus.com/commwiki/wiki?7115)
  + [Generator](https://wiki.genexus.com/commwiki/wiki?7116)
  + [Data store](https://wiki.genexus.com/commwiki/wiki?7117)
* [Object Level](https://wiki.genexus.com/commwiki/wiki?1866)

### [Preferences](#Preferences)

Preferences are the Knowledge Base, Version, Environment, Generator and Data store level properties.

Depending on the changed property, you will need to execute different operations to reflect the change in the generated code; refer to each property documentation for further information.

* Build any object
* Rebuild all objects
* Create Database

#### [Build any object](#Build+any+object)

Some properties are translated to configuration file changes (i.e. the property value is just stored in a file that the generated application access to behave accordingly). If you change one of these properties you will need to force the generation of any object using the [Build With This Only](https://wiki.genexus.com/commwiki/wiki?5693) operation.

This operation will update the configuration file.

Some examples are the following properties:

* [Log JDBC Activity property](https://wiki.genexus.com/commwiki/wiki?9135)
* [Use Native Soap property](https://wiki.genexus.com/commwiki/wiki?13446)
* [Enable Management property](https://wiki.genexus.com/commwiki/wiki?9244)

#### [Rebuild all objects](#Rebuild+all+objects)

For those cases when a property implementation affects the objects generation, a complete Rebuild All operation is needed to apply the change Knowledge Base wide.

Some examples are the following properties:

* [HTML Document Type property](https://wiki.genexus.com/commwiki/wiki?13517)
* [DataSource property](https://wiki.genexus.com/commwiki/wiki?13604)
* [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548)

#### [Create Database](#Create+Database)

When a property change impacts the database definition, you will need to execute the [Create Database Tables](https://wiki.genexus.com/commwiki/wiki?7158) Build option to apply the change.

Some examples are the following properties:

* [Enable national language support property](https://wiki.genexus.com/commwiki/wiki?11500) at version level.
* [Declare referential integrity property](https://wiki.genexus.com/commwiki/wiki?9093) at data store level.

### [Object Level](#Object+Level)

When changing an Object property, you will have to build the object for the change to apply. To build the object you may use either of the following Build submenu options:

* [Build/Run](https://wiki.genexus.com/commwiki/wiki?5692) or [Build/Run With This Only](https://wiki.genexus.com/commwiki/wiki?5693): Use any of these options if the object whose property was changed is in the call chain of the current [Startup Object](https://wiki.genexus.com/commwiki/wiki?5393) or the object is a [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?7273,,).
* Build All: Use this option if
  + the [object](https://wiki.genexus.com/commwiki/wiki?1866) whose property was changed is *not* in the call chain of the current Startup Object to avoid compilation problems; click [here](https://wiki.genexus.com/commwiki/wiki?18996) for further information.
  + a [domain](https://wiki.genexus.com/commwiki/wiki?7221), [attribute](https://wiki.genexus.com/commwiki/wiki?7240) or [subtype group](https://wiki.genexus.com/commwiki/wiki?20206) is modified.
* Rebuild All: Use this option if a [Theme](https://wiki.genexus.com/commwiki/wiki?4375) or [Language](https://wiki.genexus.com/commwiki/wiki?7258) object is modified.
* Compile any object: Use this option when a File object is changed.
* No Action needed: When modifying a [Diagram](https://wiki.genexus.com/commwiki/wiki?23941) or [Document](https://wiki.genexus.com/commwiki/wiki?10344) no further action is needed.

Notice that there are some cases when a [Create Database](https://wiki.genexus.com/commwiki/wiki?7158) is needed; it will be detailed there too.

### [What to do to make sure a property change is applied?](#What+to+do+to+make+sure+a+property+change+is+applied%3F)

If you are in doubt whether to execute a *Rebuild All* or *Rebuild any object* operation, check the property documentation.

Each property details when a *build* \ *build any object* \ *rebuild all* operation is needed, you will notice the *How to apply changes?* tag with the following values:

* *Build any object*: execute a [Build With This Only](https://wiki.genexus.com/commwiki/wiki?5693) operation.
* *Rebuild all objects*: execute a [Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691) operation.
* *Create database*: execute a [Create Database Tables](https://wiki.genexus.com/commwiki/wiki?7158) operation.


|  |
| --- |
| **Backlinks** |
| [Automatic Grid Refresh](https://wiki.genexus.com/commwiki/wiki?6744) |
| [Blob local storage directory property](https://wiki.genexus.com/commwiki/wiki?6979) | [Build Mode property for .NET generator](https://wiki.genexus.com/commwiki/wiki?3936) | [Cache Password Property](https://wiki.genexus.com/commwiki/wiki?31333) |
| [ColorPalette property](https://wiki.genexus.com/commwiki/wiki?31292) |
| [DatePicker property](https://wiki.genexus.com/commwiki/wiki?8998) |
| [DB2 UDB Version property](https://wiki.genexus.com/commwiki/wiki?10479) | [Default HTML Format (TextBlocks only) property](https://wiki.genexus.com/commwiki/wiki?9083) | [Default Tables Storage Area property](https://wiki.genexus.com/commwiki/wiki?9088) | [Dynamic Pattern Update Property](https://wiki.genexus.com/commwiki/wiki?11605) |
| [Enable Logging property](https://wiki.genexus.com/commwiki/wiki?37876) | [Category:Environments](https://wiki.genexus.com/commwiki/wiki?7115) | [Invisible Mode property](https://wiki.genexus.com/commwiki/wiki?22743) |
| [Join management property](https://wiki.genexus.com/commwiki/wiki?7966) |
|
| [Report output property](https://wiki.genexus.com/commwiki/wiki?7943) |
| [Server Name Property](https://wiki.genexus.com/commwiki/wiki?9117) | [Significant attribute name length property](https://wiki.genexus.com/commwiki/wiki?7248) |
| [Standard and non standard functions](https://wiki.genexus.com/commwiki/wiki?8565) | [Standard Functions property at Knowledge Base level](https://wiki.genexus.com/commwiki/wiki?7403) |
| [Use Custom JDBC URL Property](https://wiki.genexus.com/commwiki/wiki?9381) | [User Interface property](https://wiki.genexus.com/commwiki/wiki?13602) |
| [Workflow Generator property](https://wiki.genexus.com/commwiki/wiki?13608) |

---
