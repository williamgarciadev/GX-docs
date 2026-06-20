---
title: "Json 2 SDT"
source_id: 22574
source_url: https://wiki.genexus.com/commwiki/wiki?22574
genexus_version: "18"
---

# Json 2 SDT

[RESTful web APIs](http://en.wikipedia.org/wiki/Representational_State_Transfer#RESTful_web_APIs) are becoming an industry standard. It is the way companies have to provide functionallity to customers and providers over a well known protocol ([http](http://en.wikipedia.org/wiki/Http)).

With that, the lightweight and human-readable capabilities of [Json](http://en.wikipedia.org/wiki/JSON) have turned it into the standard for data interchange.  
When considering using an external service with Genexus, you have to create a [Structured Data Type (SDT) object](https://wiki.genexus.com/commwiki/wiki?10021) ([SDT](http://wiki.gxtechnical.com/commwiki/servlet/hwikibypageid?1878)) to manipulate data from the service. SDTs give you the possibility of using typed data and iteration, among other features.  
Creating such a structure can become quite challenging. Every property must match the exact casing of the source, levels (arrays) are kind of tricky to define. It is quite easy to make a mistake, and that's where Json Inspector comes into play.

### [Json to SDT](#Json+to+SDT)

The Json Inspector can be reached from the Tools->Aplication Integration menu in Genexus' IDE. When you select Json Import a dialog shows up asking for several fields.

**Source of the Json data**  
Can be either a file from your local computer or the url to a service that serves Json data.

If you do have a service, it is strongly recomended to use it, since copying Json from your browser to paste into a file can affect the encoding and throw parsing errors.

**Name and description of an SDT**  
It is the name of a new or existing SDT. If it already exists, you will be prompted to update (see below) or completely replace it.

**The [Folder object](https://wiki.genexus.com/commwiki/wiki?9757) the SDT must belong to**  
When you hit OK the tool parses the Json and if it is valid, an SDT ready to be used with the provided Json will be created in your Knowledge Base. You can use the [HttpClient data type](https://wiki.genexus.com/commwiki/wiki?6932) to get the data and the functions to populate the recently created SDT.

```
&url = Format('https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/%1/%2/dep/%3/%4/%5?appId=%6&appKey=%7&utc=false&codeType=%8&extendedOptions=useInlinedReferences',&airline, &number, &year, &month, &day, FlightStatsAPI.ID, FlightStatsAPI.Key, &codeType)
&HttpClient.Execute('GET', &url)
&response = &HttpClient.ToString()
&FSStatus.FromJson(&response)
```

Sample code using the recently created SDT

### [Considerations](#Considerations)

**Json Arrays**  
Json Inspector maps Json arrays to SDT collections. The data type of each SDT collection item is the data type of the first Json array element.

**Heterogene​ous arrays**  
Heterogeneous (in contrast to homogeneous) arrays are those where each item has its own, different, data type (i.e. ["hello", 1, true] is an array with a String, then a Number and then a Boolean).

They are not supported by GeneXus. The Json Inspector, however, generates an SDT collection using the data type of the first element of the array.

**Data types**  
Json Inspector guesses the data type of each SDT member based on the value of the first instance in the Json file inspected. It is therefore recommended to check each member's data type after importing.

The following table shows how Json data types are mapped to Genexus data types.

|  |  |
| --- | --- |
| **Json** | **Genexus** |
| Number | Numeric(10.5) |
| String | VarChar(100) |
| Boolean | Boolean |
| DateTime | DateTime |
| Object | SDT Level |
| Array | SDT Collection Level |

### [Availability](#Availability)

This feature is built in as of [GeneXus Tilo Beta 1](https://wiki.genexus.com/commwiki/wiki?22217,,)  
There's a downloadable version of Json2SDT Extension for Genexus X Ev2 U3 available [here](http://marketplace.genexus.com/product.aspx?json2sdt).
