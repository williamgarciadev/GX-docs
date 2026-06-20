---
title: "Date Constants"
source_id: 4372
source_url: https://wiki.genexus.com/commwiki/wiki?4372
genexus_version: "18"
---

# Date Constants

You can use date and date-time constants with ANSI/ISO (AAAA-MM-DD HH:MM:SS) format in any GeneXus expression (Rules, Conditions, Procedures, Formulas, etc).

### [Syntax](#Syntax)

<date>::=    [0-9]{1,4}"/"[0-9]{1,2}"/"[0-9]{1,2} | [0-9]{1,4}"."[0-9]{1,2}"."[0-9]{1,2} | [0-9]{1,4}"-"[0-9]{1,2}"-"[0-9]{1,2}

<hms>::=    [0-9]{1,2}[ap] | [0-9]{1,2}":"[0-9]{1,2}[ap]? | [0-9]{1,2}":"[0-9]{1,2}":"[0-9]{1,2}[ap]?

<constant> ::=   "#"<date>"#" | "#"<date> <hms>"#" | "#"<hms>"#"

### [Description](#Description)

These constants can be used in Rules, Events, Properties, and any code edition that involves the parser.

### [Samples](#Samples)

Assigning a date value:

```
&InitialDate=#2007-01-01#
```

Assigning a date-time value:

```
&InitialDateTime=#07-1-1 11:15a#
```

Assigning a time value:

```
&InitialTime=#11a#
```

Constants provide a simpler way to initialize variables/attributes, or an alternative to using character-conversion functions like CTOD or TTOC where needed, as in previous versions.

**Notes:**

* Century Handling: When the constant does not include the century (07-01-01), the [First year of 20th century property](https://wiki.genexus.com/commwiki/wiki?7631) is applied.
* To initialize the date or date-time attribute/variable with an "empty value", it is recommended to use the "nullvalue" function or "setempty" method (i.e.: &InitialDate=NullValue(&InitialDate)) instead of assigning a constant like #0001-01-01#. The reason for this is that #0001-01-01# is not a supported value for all DBMSs. For example, MS SQL Server does not support this value; the lowest date value supported is  #1753-01-01# (See [Attribute Empty Value for each DBMS and Data Type](https://wiki.genexus.com/commwiki/wiki?19150) for more details).
* The time part of a datetime may be expressed using 12-hour or 24-hour formats; the value range of these formats can be viewed at <http://en.wikipedia.org/wiki/12-hour_clock>.


|  |
| --- |
| **Backlinks** |
| [Category:Constants](https://wiki.genexus.com/commwiki/wiki?6880) | [HowTo: Deep Linking on Native Mobile](https://wiki.genexus.com/commwiki/wiki?36163) |

---
