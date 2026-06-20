---
title: "UserId function"
source_id: 8518
source_url: https://wiki.genexus.com/commwiki/wiki?8518
genexus_version: "18"
---

# UserId function

Returns the User Identification.

### [Syntax:](#Syntax%3A)

**Userid()**  
  
**Type Returned:**  
Character

### [Scope](#Scope)

**Objects:** [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908), [Web Panel](https://wiki.genexus.com/commwiki/wiki?6916), [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270)  
**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604), [.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892), [Java](https://wiki.genexus.com/commwiki/wiki?12258), RPG, Cobol, Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3), Visual Basic (up to GeneXus X Evolution 3)

### [Description](#Description)

If the variable is defined in N characters and the user assigned to it is longer than the variable length, the characters will be truncated.

In the **iSeries environment**, this function returns the User Identification defined in the User Profile.  
  
In a **PC environment**, this function returns the user's name (using API Windows functions) if the LOGNAME environment variable is not set. Otherwise, this variable's value is used. This is the expected behavior whether there is network support or not.  
  
In a **Client/Server environment**, this function could also return the identification of the user connected to the database server. If the user is not connected, the function returns blank spaces. It must be written using the following syntax: **USERID('Server').** The word Server must be written between quotes as shown.

**Note**: You cannot use this function if the [Connect to server property](https://wiki.genexus.com/commwiki/wiki?8536) has the value “At first request”, and the database has not been accessed yet.

### [See Also](#See+Also)

[Work Station Function](https://wiki.genexus.com/commwiki/wiki?8520)


|  |
| --- |
| **Backlinks** |
| [Functions in Procedures](https://wiki.genexus.com/commwiki/wiki?8504) | [Functions in Transactions](https://wiki.genexus.com/commwiki/wiki?8546) | [Functions in Web Panels](https://wiki.genexus.com/commwiki/wiki?8566) |
| [HowTo: Use GAM and Windows Authentication](https://wiki.genexus.com/commwiki/wiki?24034) | [WrkSt function](https://wiki.genexus.com/commwiki/wiki?8520) |

---
