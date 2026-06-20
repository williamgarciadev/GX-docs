---
title: "Automatic variable definition"
source_id: 12557
source_url: https://wiki.genexus.com/commwiki/wiki?12557
genexus_version: "18"
---

# Automatic variable definition

When you write variables directly in the code, GeneXus automatically defines them if possible. The criteria used to determine the type are as follows:

* **Based on**: If you have, for example, a "*Name*" [Domain](https://wiki.genexus.com/commwiki/wiki?7221) (or Attribute) and you write *&CountryName* in the source, the variable *CountryName* is defined based on the Domain (Attribute) "*Name*". If the attribute "*CountryName*" exists, it will be based on it instead.
* **Boolean**: If the variable has the prefix "&is","&Is","&has" or "&Has", followed by a string starting with a capital letter, it will be defined as Boolean.
* **Collection**: If the variable has this format: "*&xx[<Attribute Name>|<Domain Name>|<SDT Name>]Collection*", with "xx" being a free text, it will be defined as a collection based on the attribute|domain|SDT (provided there isn't an attribute, domain, or SDT with that full name). For instance, suppose you have an SDT named "Customer". If you write *&MyCustomerCollection*, the variable is defined as a collection of the Customer data type.
* **Boolean Collection**: 3 components are required to automatically define a variable as a Boolean Collection: *"&is" + <free text starting with capital letter> +"Collection"*. For instance: *&isAvailableCollection*.

### Specification and Variables not defined

Undefined variables, which have not been manually or automatically defined using the above criteria, are assigned a type at specification time using the following criteria:

* If an attribute is assigned to the variable, the type and length of the attribute will be used to define the variable.  
  That is, when *&ClientName = ClientName*, the type and length of the *ClientName* attribute are assumed for the variable. If there is more than one for the variable, only the first one is taken into account to assume the type.

* If a function is assigned to the variable, the returned type of the function is assumed for the variable. In this case, the length cannot be automatically assumed. Therefore, Numeric variables will have length = 10,2 and Character variables will have length = 40.  
  That is, when &Variable1 = val(Attribute), Variable1 will be N(10.2);  
  &Variable2 = Attribute.ToString(), Variable2 will be C(40).

* Otherwise, Numeric type and length = 10,2 are assumed for undefined variables.

In all cases, when a type is assumed for a variable at specification time, a warning is displayed in the navigation report: **warning: spc0047: Variable Variable2 not defined; N(10.2) assumed.**


|  |
| --- |
| **Backlinks** |
| [Table of contents:GeneXus - Table of contents](https://wiki.genexus.com/commwiki/wiki?22331) |

---
