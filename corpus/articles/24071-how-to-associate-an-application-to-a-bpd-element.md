---
title: "How to associate an application to a BPD element"
source_id: 24071
source_url: https://wiki.genexus.com/commwiki/wiki?24071
genexus_version: "18"
---

# How to associate an application to a BPD element

Once you have modeled the [Business Process](https://wiki.genexus.com/commwiki/wiki?48918) you should convert the business process diagram in a functional application.

The way to accomplish that is by associating GeneXus objects to the [Business Process Diagram](https://wiki.genexus.com/commwiki/wiki?16486) elements. This stage is known as Automation and is part of the [BPM Cycle](https://wiki.genexus.com/commwiki/wiki?44029).

Assume that you have a BPD from a ticket reservation process, in a Travel Agency.

`[imagen omitida: wiki id 24082]`

The first step in the process is to enter the reservation for the ticket. To accomplish this task, you should use an object that allows entering the reservation information using a web form and store the data in a database.

This action is usually accomplished by a GeneXus [Transaction object](https://wiki.genexus.com/commwiki/wiki?1908).
