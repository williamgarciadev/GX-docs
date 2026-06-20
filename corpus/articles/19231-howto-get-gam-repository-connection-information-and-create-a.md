---
title: "HowTo: Get GAM Repository connection information and create a connection file"
source_id: 19231
source_url: https://wiki.genexus.com/commwiki/wiki?19231
genexus_version: "18"
---

# HowTo: Get GAM Repository connection information and create a connection file

**Deprecated**: Since [GeneXus 17 Upgrade 5](https://wiki.genexus.com/commwiki/wiki?48247,,).

This document explains how to programmatically get the [GAM](https://wiki.genexus.com/commwiki/wiki?14960) Repository Connection information in XML format, using the GAM API. The resulting XML is suitable for copy & paste in a [connection.gam](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,E,0,,30451) file, so it includes all the information needed to connect to a GAM Repository.

This is useful when the [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) administrator creates a new [GAM Repository](https://wiki.genexus.com/commwiki/wiki?17568) and later needs to create a connection.gam file, to give it to the administrator of the new Repository so as to connect to it. See [HowTo: Creating New Repositories](https://wiki.genexus.com/commwiki/wiki?18642) for more information about this scenario.

So, given a Repository GUID and a [GAM Repository Connection](https://wiki.genexus.com/commwiki/wiki?16150) name, the GAM API provides a method that allows getting the XML needed to include in connection.gam file so as to connect to this Repository using the connection name provided.

### [Sample of use](#Sample+of+use)

The method used for this purpose is GetConnectionsFile (a method of GAM external object).

It receives as a parameter a collection of GAMRepositoryConnectionFileFilter (an SDT that has the Repository GUID and the Repository Connection name). So, this method can receive many Repositories as filter and return an XML file with the connection information of all of them.

It also receives as a parameter the user name and user password of [GAM Manager Repository](https://wiki.genexus.com/commwiki/wiki?18617) user.

See the example below:

Define a variable named &GAMRepositoryConnectionFileFilter based on GAMRepositoryConnectionFileFilter data type, and a variable &GAMRepositoryConnectionFileFilters which is a collection of GAMRepositoryConnectionFileFilter data type. These data types are part of GAM library.

Code the following in order to get the connection.gam information into a string variable (&TextXML):

```
&GAMRepositoryConnectionFileFilter.GUID = &GUID  // &GUID of the Repository
&GAMRepositoryConnectionFileFilter.Name = &ConnectionName // &ConnectionName of the Repository Connection
&GAMRepositoryConnectionFileFilters.Add(&GAMRepositoryConnectionFileFilter)
GAM.GetConnectionsFile(&gamadminuser,&gamadminpwd,&GAMRepositoryConnectionFileFilters,&TextXML,&Errors) //set the information of the connection into &TextXML variable

//process the errors
for &Error in &Errors
    msg(&Error..Message + !"(GAM" + &Error.Code.ToString().Trim() + !")")
endfor
```

A connection file with the information obtained above is created as shown below:

```
&XmlWriter.open("connection.gam")
&XmlWriter.WriteRawText(&TextXML)
&XmlWriter.close()
```

### [Note](#Note)

In order to get the information from the [connection.gam](http://www2.gxtechnical.com/portal/hgxpp001.aspx?15,4,61,O,E,0,,30451) file directly you need to use the [GAM GetConnections method](https://wiki.genexus.com/commwiki/wiki?19245).


|  |
| --- |
| **Backlinks** |
| [GAM - Repository Connections](https://wiki.genexus.com/commwiki/wiki?16150) | [HowTo: Create New Repositories using GAM](https://wiki.genexus.com/commwiki/wiki?18642) |

---
