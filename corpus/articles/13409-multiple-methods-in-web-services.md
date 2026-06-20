---
title: "Multiple methods in Web services"
source_id: 13409
source_url: https://wiki.genexus.com/commwiki/wiki?13409
genexus_version: "18"
---

# Multiple methods in Web services

[Versión en Español](https://wiki.genexus.com/commwiki/wiki?13516,,)

This article describes how to define a SOAP Web Service with multiple methods.

Web Services use to have many methods in order to make them easier to understand and use. In that way, for example, you can have a CustomerServices service with methods BasicInformation and PurchaseHistory. The code of CustomerService [Procedure](https://wiki.genexus.com/commwiki/wiki?6293) (service) would look like the following:

```
// CustomerServices services
…
Stub BasicInformation( in:&CustomerId, out:&BasicInformation)
   For each
	// Navigation to populate &BasicInformation
   Endfor
EndStub

Stub PurchaseHistory( in:&CustomerId, out:&PurchaseHistory)
   For each
	// Navigation to populate &PurchaseHistory
   Endfor
EndStub
```

The WSDL generated for a service having multiple methods like the above can be inspected by other GeneXus Knowledge Bases (Tools > Application Integration > WSDL Import), generating an external object having service's methods that are used as shown in the example below.

```
&CustomerServices = new() 							// &CustomerServices’ data type is CustomerServices (the imported External Object)
&CustomerBasicInformation = &CustomerServices.BasicInformation( 1)
// Process information of Customer with Id = 1.

&CustomerBasicInformation = &CustomerServices.PurchaseHistory( 2)
// Process PurchaseHistory of Customer with Id = 2
```

In the same way, the generated service can be inspected and consumed by programming languages like C#, Java, etc.

### [Notes/Usage](#Notes%2FUsage)

* Objects with Stubs do \_not\_ expose the “execute” method.

If necessary (for compatibility) you must define a Stub with that name (execute).

* Parameters defined in the parm() rule are \_not\_ Stubs parameters too
* Stub objects must not have code out of the Stub/EndStub scope.
* Procedures exposed as REST do not support this feature

### [Availability](#Availability)

Stubs and Web services with multiple methods were implemented in .Net and Java generators as of [GeneXus X Evolution 1](https://wiki.genexus.com/commwiki/wiki?9256,,) Upgrade 2. In previous versions, Web services had only one method named “execute”.
