---
title: "Changing the value of DateTime Storage property at application installation/upgrade time"
source_id: 22045
source_url: https://wiki.genexus.com/commwiki/wiki?22045
genexus_version: "18"
---

# Changing the value of DateTime Storage property at application installation/upgrade time

This document describes the scenarios that a GeneXus developer may face when installing or upgrading an application with [TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988).

### [Installing an application for the first time](#Installing+an+application+for+the+first+time)

In a brand new installation there is no data in the Database. If you have to convert data from legacy systems, follow the steps described in "Upgrading an application" below.

If the application was generated using the Undefined value for [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218), you cannot change it at installation time (see [Changing the value of DateTime Storage property](https://wiki.genexus.com/commwiki/wiki?22022) for exceptions).

If the application was generated using either UTC or Application server values for DateTime storage timezone property, you may change it if you need to. To do so, change the [Application configuration file](https://wiki.genexus.com/commwiki/wiki?22044,,).

### [Upgrading an application](#Upgrading+an+application)

When upgrading an application, the main consideration is about Database data. Does it have to be converted or not? Is there a way to convert it?

The following table describes possible scenarios and the actions that may be required.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| *Current Database Scenario* | |  | *Value of DateTime Storage TimeZone property in the new application* | | |
| Undefined | UTC | Application server |
| All DateTime attributes are stored in the same Time Zone | UTC | No conversion required. | No conversion required | You may either change the Application configuration file to match current data (UTC) or write and run a data conversion program (see below). |
| Application Server | You may either change the Application configuration file to match current data (Application Server) or write and run a data conversion program (see below). | No conversion required |
| Other | Write and run a data conversion program (see below) that converts DateTime values from their TimeZone to UTC. | You can either:   * Write and run a data conversion program (see below) that converts DateTime values from their TimeZone to Application Server. * Or change your server's TimeZone to match your existing data. |
| The TimeZone of DateTime attributes is known but it may be different from attribute to attribute | | Write and run a data conversion program (see below) that converts DateTime values from their TimeZone to Application Server. | | |

### [Conversion program skeleton](#Conversion+program+skeleton)

When upgrading your application from previous GeneXus versions or when changing the value of [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218), you may need to write and run a conversion program to make all DateTime attributes of the database  share a unique TimeZone (either UTC or Application Server).

Below is a program skeleton that guides you to write that conversion program. Just in case, remember to backup your database \_before\_ running the conversion program.

```
// Set the default timezone to UTC.
// If you need it to be a different one just change the parameter
DateTime.SetTimeZone( Timezones.UTC)
for each
   ...
   // DateTimeAttribute is known to be in Timezones.New_York time zone.
   // The following statement converts its value from New_York to UTC (value set by previous SetTimeZone command)
   DateTimeAttribute = DateTimeAttribute.FromTimeZone( Timezones.New_York)
   ...
endfor
Commit
```

### [**Note**s](#Notes)

* Conversion programs MUST be generated and run when [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) is set to Undefined.
* Change the value of [DateTime storage timezone property](https://wiki.genexus.com/commwiki/wiki?17218) \_after\_ running the conversion programs

To improve update performance, you may want to take a look at [Blocking Data Updates](https://wiki.genexus.com/commwiki/wiki?5572).


|  |
| --- |
| **Backlinks** |
| [Changing the value of DateTime Storage property](https://wiki.genexus.com/commwiki/wiki?22022) | [Toc:TimeZone Support](https://wiki.genexus.com/commwiki/wiki?21988) |

---
