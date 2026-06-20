---
title: "GeneXus for SAP B1 Systems"
source_id: 45694
source_url: https://wiki.genexus.com/commwiki/wiki?45694
genexus_version: "18"
---

# GeneXus for SAP B1 Systems

GeneXus For SAP B1 Systems is GeneXus´s solution to extend SAP Business One functionality through the development of third party applications.

### [How does it work?](#How+does+it+work%3F)

Integration with SAP Business One systems is achieved using OData technology, available in the Service Layer of SAP Business One system.

Services published in the Service Layer can be consumed by applications developed in GeneXus.

Hence, it is possible to build software that integrates directly to SAP Business One system, allowing it to receive and send information.

### [SAP Business One Requirements](#SAP+Business+One+Requirements)

For SAP Business One systems that use HANA, Service Layer is available from version 9.2.

For SAP Business One systems that use SQL, Service Layer is available from version 10.

The developer must have the following

* URL of the Service Layer in order to access SAP Business One metadata
* User credentials to log on to the SAP Business One system

### [What does GeneXus for SAP B1 Systems contain?](#What+does+GeneXus+for+SAP+B1+Systems+contain%3F)

GeneXus for SAP B1 Systems contains the following:

* Fiori 2.0 and Fiori 3.0 Design System
* Inspector OData which allows you to create the required objects needed to interact with simple entities (one level of information) automatically.
* SAP B1 Integration Module, containing the definition of base entities, that allow the modelling and interaction with complex entities (two or more levels of information) and ready to use procedures to send and receive information to and from SAP Business One system

### [Proof of concept](#Proof+of+concept)

A proof of concept case was developed in GeneXus, building a software integrated with SAP Business One, allowing the user to create a Customer Invoice containing information for the invoice items as well as for the invoice payments.

Features of this proof of concept:

* Creation of Customer Invoice with invoice items and invoice payments
* Notification Email after creation of the invoice
* Activity Log, recording requests sent to the SAP Business One system and the responses received as result.

The application built connects with SAP Business One by consuming the services published in Service Layer.

Once the information is sent by the application built in GeneXus, SAP Business One will impact the information received regarding the creation of the new Invoice in all the referenced structures, such as stock inventory, customer accounts payable, and so on.


|  |
| --- |
| **Backlinks** |
| [Toc:GeneXus for SAP Systems](https://wiki.genexus.com/commwiki/wiki?33616) |

---
