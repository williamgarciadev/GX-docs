---
title: "Calling rest API Using Postman app"
source_id: 50054
source_url: https://wiki.genexus.com/commwiki/wiki?50054
genexus_version: "18"
---

# Calling rest API Using Postman app

This article describes how to call a Rest API using a client application; in this case: [Postman](https://www.postman.com/).

First, set the API object [Generate OpenAPI interface property](https://wiki.genexus.com/commwiki/wiki?31859) to Yes and save.

`[imagen omitida: wiki id 50262]`

After that, select [Build All/Rebuild All](https://wiki.genexus.com/commwiki/wiki?5691).

Next, run the API object and download the YAML definition file: http://server/BaseUrl/APIObjectName.yaml.

.NET: http://localhost/APIObjectExampleFromScratch.NETFrameworkEnvironment/APICustomers.yaml  
Java: http://localhost:8080/APIObjectExampleFromScratchJavaEnvironment/static/APICustomers.yaml

Below you can see all the steps being executed:

`[imagen omitida: wiki id 49795]`

You have to import de YAML file in Postman.

Finally, you can test all the services:

* [ListCustomers](https://wiki.genexus.com/commwiki/wiki?50051)
* [GetByKey](https://wiki.genexus.com/commwiki/wiki?50052)
* [Insert](https://wiki.genexus.com/commwiki/wiki?49778)
* [Update](https://wiki.genexus.com/commwiki/wiki?49780)
* [Delete](https://wiki.genexus.com/commwiki/wiki?49781)


|  |
| --- |
| **Backlinks** |
| [Toc:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) | [Prototyping an API with Swagger](https://wiki.genexus.com/commwiki/wiki?50008) |

---
