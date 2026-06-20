---
title: "Business Component"
source_id: 5846
source_url: https://wiki.genexus.com/commwiki/wiki?5846
genexus_version: "18"
---

# Business Component

The Business Component (BC) concept provides a way to use all the power of a [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908) from other GeneXus objects.

It allows updating the database from any object, executing Transactions in a 'silent' mode (without showing its forms) but taking advantage of all the benefits offered by them!

### [Most important benefits](#Most+important+benefits)

* **[Database update guaranteeing data integrity](https://wiki.genexus.com/commwiki/wiki?42576)**
* **Less coding:** The business logic defined in the Transaction is reused (rules and formulas are triggered, etc.)
* **All GeneXus objects can update the database:** For example in a [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916) the only way to update directly the database (without calling a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293)) is using the business component concept.
* **[Rest](https://wiki.genexus.com/commwiki/wiki?14573):** A Business Component may be exposed as a Rest web service.
* **[SOA](https://wiki.genexus.com/commwiki/wiki?1813,,) interface:** A Business Component may be defined as a SOAP web service, allowing updates via SOAP.
* **[EJB](https://wiki.genexus.com/commwiki/wiki?1818):** A Business Component can be defined as a [Enterprise Java Bean](https://wiki.genexus.com/commwiki/wiki?1818) so you can execute it in an EJB Container of any J2EE Server.

### [Business Component definition](#Business+Component+definition)

Every Transaction offers the [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548) to define it as a Business Component.

### [See Also](#See+Also)

[DB update using two-level business components](https://training.genexus.com/en/learning/courses/genexus/genexus-16-course-analyst/db-update-using-two-level-business-components-v16?p=5498)

### [Videos](#Videos)

`[imagen omitida: wiki id 20668]` [Database Update Using Business Components. Justification.](https://training.genexus.com/en/learning/courses/genexus/v18/core/content/database-update-using-business-components-justification-6104768)


* [Business Component property](https://wiki.genexus.com/commwiki/wiki?9548)
* [Properties of BC variables](https://wiki.genexus.com/commwiki/wiki?2276)
* [Methods for BC variables](https://wiki.genexus.com/commwiki/wiki?2277)
  + [Load](https://wiki.genexus.com/commwiki/wiki?23211)
  + [Save](https://wiki.genexus.com/commwiki/wiki?23229)
  + [Insert](https://wiki.genexus.com/commwiki/wiki?31695)
  + [Update](https://wiki.genexus.com/commwiki/wiki?31696)
  + [InsertOrUpdate](https://wiki.genexus.com/commwiki/wiki?31697)
  + [Delete](https://wiki.genexus.com/commwiki/wiki?23238)
  + [Check](https://wiki.genexus.com/commwiki/wiki?23401)
  + [Fail](https://wiki.genexus.com/commwiki/wiki?23402)
  + [Success](https://wiki.genexus.com/commwiki/wiki?23404)
  + [GetMessages](https://wiki.genexus.com/commwiki/wiki?23475)
  + [ToXml](https://wiki.genexus.com/commwiki/wiki?23483)
  + [FromXml](https://wiki.genexus.com/commwiki/wiki?23633)
  + [ToJson](https://wiki.genexus.com/commwiki/wiki?37817)
  + [FromJson](https://wiki.genexus.com/commwiki/wiki?37809)
  + [Add](https://wiki.genexus.com/commwiki/wiki?23662)
  + [GetByKey](https://wiki.genexus.com/commwiki/wiki?31846)
  + [RemoveByKey](https://wiki.genexus.com/commwiki/wiki?31847)
  + [Mode](https://wiki.genexus.com/commwiki/wiki?23790)
  + [GetOldValues](https://wiki.genexus.com/commwiki/wiki?23804)
* [Error handling](https://wiki.genexus.com/commwiki/wiki?2279)
* [Inserting a BC variable in a form](https://wiki.genexus.com/commwiki/wiki?2281)
* [Transaction rules when executed as BC](https://wiki.genexus.com/commwiki/wiki?2280)
* [Transaction events when executed as BC](https://wiki.genexus.com/commwiki/wiki?23813)
* [Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282)
* [Publication as an Enterprise Java Bean](https://wiki.genexus.com/commwiki/wiki?1993,,)
* [Samples](https://wiki.genexus.com/commwiki/wiki?2278)
  + [Insert](https://wiki.genexus.com/commwiki/wiki?2278)
  + [Update](https://wiki.genexus.com/commwiki/wiki?2278)
  + [Delete](https://wiki.genexus.com/commwiki/wiki?2278)
  + [Insert or Update](https://wiki.genexus.com/commwiki/wiki?2278)
  + [Insert a line](https://wiki.genexus.com/commwiki/wiki?2278)
  + [Update a line](https://wiki.genexus.com/commwiki/wiki?2278)
  + [Delete a line](https://wiki.genexus.com/commwiki/wiki?2278)

---
