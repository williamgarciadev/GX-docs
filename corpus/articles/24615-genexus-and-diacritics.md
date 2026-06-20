---
title: "GeneXus and Diacritics"
source_id: 24615
source_url: https://wiki.genexus.com/commwiki/wiki?24615
genexus_version: "18"
---

# GeneXus and Diacritics

[Diacritics](http://en.wikipedia.org/wiki/Diacritic) are accents used in some languages, they may appear above or below a letter, or in some other position such as within the letter or between two letters.

It is important to manage them correctly so that your application works as espected no matter the language accents.

In GeneXus it is important because you may want to have different behaviour depending in where the conditions are evaluated (client or server side).

To manage accent sensitivity you have two sides:

### [Server side](#Server+side)

In most of the DBMS it is possible to configure accent sensibility.

##### [SQL Server configuration](#SQL+Server+configuration)

In SQL Server\data base properties\Options\[Collation](http://msdn.microsoft.com/en-us/library/ms143726.aspx), you would have to [select one](http://msdn.microsoft.com/en-us/library/ms144250(v=sql.105).aspx) with "\_AI" (accent insensitive) if you want this to be solved. By default SQL server is case insensitive and accent sensitive.

`[imagen omitida: wiki id 24616]`

**Note:** After changing collation, you need to create again the Database tables from GeneXus in order for it to take effect.

##### [MySQL configuration](#MySQL+configuration)

In [MySQL](https://dev.mysql.com/doc/refman/5.0/en/charset-applications.html), by default is "latin1, latin1\_swedish\_ci", which already covers cases of diacritics. By default MySQL is case insensitive and accent insensitive. If you want to change this you can configure it on your MySQL client.

##### [SQLite configuration](#SQLite+configuration)

In SQLite it is not possible to change accent sensibility. By default SQLite is case insensitive and accent sensitive.

### [Client side](#Client+side)

##### [Search, filters and conditions using RemoveDiacritics Method](#Search%2C+filters+and+conditions+using+RemoveDiacritics+Method)

Use [RemoveDiacritics method](https://wiki.genexus.com/commwiki/wiki?24596) on your GeneXus code.

### [Note](#Note)

RemoveDiacritics method is specific to a string and the above mentioned DBMS configurations apply to the whole Database.

### [See also](#See+also)

[HowTo: Change Case Sense on DBMS](https://wiki.genexus.com/commwiki/wiki?24690,,)

[Enable national language support property](https://wiki.genexus.com/commwiki/wiki?11500)


|  |
| --- |
| **Backlinks** |
| [RemoveDiacritics method](https://wiki.genexus.com/commwiki/wiki?24596) |

---
