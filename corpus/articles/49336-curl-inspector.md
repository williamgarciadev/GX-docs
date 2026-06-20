---
title: "cURL Inspector"
source_id: 49336
source_url: https://wiki.genexus.com/commwiki/wiki?49336
genexus_version: "18"
---

# cURL Inspector

The cURL Inspector Wizard, located under Tools > Application Integration, allows you to create a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) and the variables required to emulate a specific cURL script using GeneXus code.

#### [Step 1:](#Step+1%3A)

Enter a Name, Description, and a valid cURL script as shown below:

```
curl -k -i -X POST -H "Content-Type: text/xml" -H "SOAPAction: \"\"" --data-binary @request3.xml http://SERVER/BASEURL/resource2
```

It looks as follows:

`[imagen omitida: wiki id 49341]`

Optionally, you can indicate a folder where the object will be stored in the KB.

#### [Step 2:](#Step+2%3A)

After confirming the dialog, a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) will be created:

`[imagen omitida: wiki id 49342]`

For further information on how to consume a service, see: [Consuming web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?20777,,)

### [Availability](#Availability)

Since [GeneXus 17 Upgrade 6](https://wiki.genexus.com/commwiki/wiki?48684,,).
