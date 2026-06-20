---
title: "API object Considerations"
source_id: 50053
source_url: https://wiki.genexus.com/commwiki/wiki?50053
genexus_version: "18"
---

# API object Considerations

Below are several considerations to keep in mind when using [API object](https://wiki.genexus.com/commwiki/wiki?46151)s.

### [Considerations when generating with the [.NET Generator](https://wiki.genexus.com/commwiki/wiki?38604)](#Considerations+when+generating+with+the+com.gxwiki.wiki%3F38604%2CCategory%253AGeneXus%2B.NET%2BGenerator+.NET+Generator)

PUT and DELETE methods are not enabled by default in the Internet Information Services Manager configuration.

This video shows how to do so:

`[imagen omitida: wiki id 49794]`

### [Considerations when generating with the [Java Generator](https://wiki.genexus.com/commwiki/wiki?12258)](#Considerations+when+generating+with+the+com.gxwiki.wiki%3F12258%2CCategory%253AGeneXus%2BJava%2BGenerator+Java+Generator)

The names of the parameters are case-sensitive, as you can see in [SAC#49817](https://www.genexus.com/es/developers/websac?data=49817).  
In other words, the use of uppercase or lowercase letters must be respected when parameters are defined and used.

### [Considerations when generating with the [.NET Framework Generator](https://wiki.genexus.com/commwiki/wiki?2892)](#Considerations+when+generating+with+the+com.gxwiki.wiki%3F2892%2CCategory%253AGeneXus%2B.NET%2BFramework%2BGenerator+.NET+Framework+Generator)

To use the verb OPTIONS, see [SAC 47447](https://www.genexus.com/es/developers/websac?data=47447;;)

### [Considerations when [deploying the application](https://wiki.genexus.com/commwiki/wiki?32092)](#Considerations+when+com.gxwiki.wiki%3F32092%2CTable%2Bof%2Bcontents%253AApplication%2BDeployment%2Btool+deploying+the+application)

It could be important to set the properties such as [Web Root](https://wiki.genexus.com/commwiki/wiki?9287) and [Protocol specification](https://wiki.genexus.com/commwiki/wiki?8079) with the appropriate values to make it work in the target [Environment](https://wiki.genexus.com/commwiki/wiki?7115).

If the default values are "http://localhost/baseurl/" and "HTTP", respectively, you should set the Environment properties according to the executing Environment before calling the service.


|  |
| --- |
| **Backlinks** |
| [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) |

---
