---
title: "External Object: WSDL - Web Service"
source_id: 6154
source_url: https://wiki.genexus.com/commwiki/wiki?6154
genexus_version: "18"
---

# External Object: WSDL - Web Service

External Objects (EO) of WSDL type allow Web Services references to be added to the [KB](https://wiki.genexus.com/commwiki/wiki?2428) from its WSDL.

These EOs store all the related information (name, properties, methods, parameters, etc.) required for using the Web Service described in its WSDL.

`[imagen omitida: wiki id 53692]`

**Note**: The EO can be created manually by indicating each one of its properties or by using a wizard, WSDL Import, which can be accessed through the Tools option in the GeneXus menu under Reverse Engineer.

## [Properties](#Properties)

### [External Object](#External+Object)

`[imagen omitida: wiki id 53693]`

***Name:*** name of the EO.  
***Description:*** description.  
**[Type](https://wiki.genexus.com/commwiki/wiki?53690)*:*** EO type (WSDL).  
**[Use Native Soap](https://wiki.genexus.com/commwiki/wiki?13446):** method to be used.  
***Namespace:*** WS namespace.  
***Folder:*** folder where the EO is located  
**[Object Visibility](https://wiki.genexus.com/commwiki/wiki?22473):** accessibility from other objects in different Modules.  
***XML Name:*** name of the WS given in the WSDL.

### [Methods](#Methods)

`[imagen omitida: wiki id 53695]`

**Internal Name:** internal name of the method.  
***Description:*** description.  
***Type:*** GeneXus data type of the return value.  
***Style:*** WS, RPC, or Document style binding.  
***Use:*** SOAP binding use, Encoded or Literal.  
***Address:*** WS address. This property implies that you can modify the address value for prototyping purposes (another option is to use the [Location data type](https://wiki.genexus.com/commwiki/wiki?6981) or XML).  
***Action:*** action associated with the method.  
***Request Namespace:*** namespace of the WS request.  
***Response Namespace:*** namespace of the WS response.  
***XML Name:*** external name of the method.  
***XML Namespace:*** method namespace in the WS.  
***SOAP Type:*** data type of the return value in the SOAP message.  
***Collection Serialization:***  collection serialization type: Wrapped or Sequence.

### [Parameters](#Parameters)

`[imagen omitida: wiki id 53696]`

***Access Type:*** IN, OUT, INOUT.  
***Internal Name:*** name given in GeneXus to the parameter.  
***Type:*** data type given in GeneXus.  
***XML Name:*** external name of the parameter.  
***XML Namespace:*** parameter namespace in the WS.  
***SOAP Type:*** data type of the parameter given in the SOAP message.

## [Use](#Use)

Suppose you create an EO of the WSDL type called GoogleSearchService. Then you define a GoogleSearchService variable called &ws and a variable GoogleSearchResult variable &res (collection of GoogleResult).

In your code you can do the following:

```
Event Enter
  &res = &ws.doGoogleSearch(&key,&text, 0, 10, 0, "", 0, "", "", "")
EndEvent

Event Load
    for &resultElement in &res.resultElements
        &title = &resultElement.title
        load
    endfor
EndEvent
```

Here, *doGoogleSearch* is the Web Service method to be invoked to search for the text (*&text*) passed as a parameter. Then, the resulting values would be loaded into a grid.

**Note**: The Google Web Search API has been deprecated; for more information, click [here](https://developers.google.com/web-search/docs/).

## [See Also](#See+Also)

[Parameters Style property in External Object](https://wiki.genexus.com/commwiki/wiki?53486)


|  |
| --- |
| **Backlinks** |
| [Business Component - Publication as Web Service](https://wiki.genexus.com/commwiki/wiki?2282) | [Consuming SOAP web services in GeneXus](https://wiki.genexus.com/commwiki/wiki?21003) | [Category:External object](https://wiki.genexus.com/commwiki/wiki?5669) |
| [Parameters Style property in External Object](https://wiki.genexus.com/commwiki/wiki?53486) | [TLS Services](https://wiki.genexus.com/commwiki/wiki?39253) |
| [Type property in External Object](https://wiki.genexus.com/commwiki/wiki?53690) | [WSDL Import Wizard](https://wiki.genexus.com/commwiki/wiki?6181) | [Xml SoapType property (SDT)](https://wiki.genexus.com/commwiki/wiki?7451) |

---
