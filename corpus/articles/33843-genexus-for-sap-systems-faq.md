---
title: "GeneXus for SAP Systems - FAQ"
source_id: 33843
source_url: https://wiki.genexus.com/commwiki/wiki?33843
genexus_version: "18"
---

# GeneXus for SAP Systems - FAQ

In this article, you can find frequently asked questions (FAQ) about [SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616).

#### [**1. How is SAP HANA database on SAP Business Technology Platform used?**](#1.+How+is+SAP+HANA+database+on+SAP+Business+Technology+Platform+used%3F)

You can use a trial account in SAP Cloud Platform to create a database using SAP Hana in-memory database. More information at [How to use SAP HANA Database on SAP Business Technology Platform](https://wiki.genexus.com/commwiki/wiki?47848).

#### [**2. How is an application to SAP Business Technology Platform deployed?**](#2.+How+is+an+application+to+SAP+Business+Technology+Platform+deployed%3F)

More information on [Deploy to SAP Cloud Foundry - SAP BTP](https://wiki.genexus.com/commwiki/wiki?49572).

#### [**3. What's the difference between the values "1.0" and "1.0 SPS 11 or higher" of the Data Store property "Database Information/SAP HANA version"?**](#3.+What%27s+the+difference+between+the+values+%221.0%22+and+%221.0+SPS+11+or+higher%22+of+the+Data+Store+property+%22Database+Information%2FSAP+HANA+version%22%3F)

See [SAC 41124](https://www.genexus.com/developers/websac?en,,,41124).

#### [**4. Why doesn't work new when duplicate on HANA DB?**](#4.+Why+doesn%27t+work+new+when+duplicate+on+HANA+DB%3F)

See [SAC 41934](https://www.genexus.com/developers/websac?en,,,41934).  
Use for each when none instead.

#### [**5. Inspecting an OData service from SAP Business One I get an error Could not parse as Edmx document?**](#5.+Inspecting+an+OData+service+from+SAP+Business+One+I+get+an+error+Could+not+parse+as+Edmx+document%3F)

The complete message is: HTTP 500 - java.lang.IllegalArgumentException: Could not parse as Edmx document.  
This is because of the version of the OData service, the supported one is V4.0 or up (you can check this in the metadata of the service (<edmx:Edmx Version="4.0" xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx">).  
Sometimes, in B1 the URI of the service indicate that, i.e. http://www.xx.yy.zzz:50001/b1s/v2 (v2 refers to the version, but there is no relationship between the number 2 and the version number).

#### [**6. Inspecting an OData service from SAP Business One, I get an error Unsupported kind for attribute BankPagesDueDate: None, Edm.DateTime?**](#6.+Inspecting+an+OData+service+from+SAP+Business+One%2C+I+get+an+error+Unsupported+kind+for+attribute+BankPagesDueDate%3A+None%2C+Edm.DateTime%3F)

This is because the metadata has an entity with an attribute with the Edm.DateTime type, which is supported for Odata v2, but no longer supported for v4. In the OData v4 the type Edm.DateTimeOffset is used instead. This irregularity with the types and version is given because even if on the metadata is defined that follows the OData v4 protocol, sometimes for Business One, the data types are not the ones used on that version.

#### [**7. Can I do a Single Sign On from a GeneXus applicaton to a SAP Business One?**](#7.+Can+I+do+a+Single+Sign+On+from+a+GeneXus+applicaton+to+a+SAP+Business+One%3F)

See [SAC 47423](https://www.genexus.com/developers/websac?en,,,47423) - SSO con SAP Business One.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
