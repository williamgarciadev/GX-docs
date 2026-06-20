---
title: "GIK Naming Convention"
source_id: 9020
source_url: https://wiki.genexus.com/commwiki/wiki?9020
genexus_version: "18"
---

# GIK Naming Convention

[Spanish Version](https://wiki.genexus.com/commwiki/wiki?1872,,)

The GIK naming convention is a standard defined by GeneXus for creating attribute names.

Using the GIK (GeneXus Incremental Knowledge Base) naming convention is important because it:

* Makes the naming task easier
* Simplifies the integration of [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836)s
* Makes it possible to reuse knowledge between Knowledge Bases
* Facilitates code reading
* Enables other programmers to understand the code
* Simplifies maintenance

The GIK naming convention determines that an attribute name is made up of 4 components (some of them are optional, marked between straight brackets):

**Transaction object name + Category** **[****+ Qualifier + Complement****]**

**Where:**

*Transaction object name*  
    Name of the Entity or [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) (for example: Customer, Invoice, InvoiceLine).  
   
*Category*  
    Semantic category of the attribute (for example: Id (identifier), Code (code), Name (name), Date (date), Description (description), Price (price). That is, it defines the role played by the attribute within the object. Preferably, it should not exceed 10 characters.

*Qualifier*  
    An adjective or adverb of about 10 characters that provides a conceptual differentiation to the attribute name in order to make it unique (for example: Initial, Final).

*Complement*  
     Free text up to the maximum number of significant characters (30) for the name.

**Note**: The syntax order is applicable for languages where adjectives are placed after nouns. If the attribute name is defined in English, it is the other way around, so the Category (noun) goes at the end.

### [Sample](#Sample)

```
Customer
{
    CustomerId*
    CustomerName
    Branch
    {
          CustomerBranchId*
          CustomerBranchAddress
          CustomerBranchPhone
    }
}
```

### [See Also](#See+Also)

[Attribute definition](https://wiki.genexus.com/commwiki/wiki?7240)
