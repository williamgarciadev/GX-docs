---
title: "MailRecipientCollection New method"
source_id: 7758
source_url: https://wiki.genexus.com/commwiki/wiki?7758
genexus_version: "18"
---

# MailRecipientCollection New method

Returns a MailRecipient type object that is stored in the collection.

### [Syntax](#Syntax)

*&**VarBasedOn**MailRecipientCollection*.**New(***Name*, *Address***)**

**Where:**  
  
*Name*  
     Name of the new MailRecipient type object within the collection. If this parameter is an empty string, the new object to be created in the collection will be assigned a Name property equal to the Address property.

*Address*  
     Address of the new MailRecipient type object within the collection. If the Address parameter is an empty string, the call to the New method will be ignored.

**Type Returned:**  
Numeric

### [Scope](#Scope)

**Extended Data Types:** [MailRecipientCollection](https://wiki.genexus.com/commwiki/wiki?6996)  
**Generators:**

[.NET](https://wiki.genexus.com/commwiki/wiki?38604),
[.NET Framework](https://wiki.genexus.com/commwiki/wiki?2892),
[Java](https://wiki.genexus.com/commwiki/wiki?12258), Ruby (up to GeneXus X Evolution 3), Visual FoxPro (up to GeneXus X Evolution 3)

### [Description](#Description)

It creates a new MailRecipient type object within a collection, in the name and address specified in the Name and Address parameters respectively.

**Note**: This method returns an error code, so it is possible to call it as a function (i.e.:  &Err = &MailRecipientCollection.New(.....)).

### [See Also](#See+Also)

[MailRecipient Data Type](https://wiki.genexus.com/commwiki/wiki?6926)  
[MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996)


|  |
| --- |
| **Backlinks** |
| [MailRecipientCollection Data Type](https://wiki.genexus.com/commwiki/wiki?6996) |

---
