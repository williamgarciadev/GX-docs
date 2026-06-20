---
title: "WSAddressing Data Type"
source_id: 44549
source_url: https://wiki.genexus.com/commwiki/wiki?44549
genexus_version: "18"
---

# WSAddressing Data Type

Consume WS-Addressing services with the property Use Native Soap = Yes

### [Description](#Description)

The [WS-Addressing](http://www.w3.org/Submission/2004/SUBM-ws-addressing-20040810/) SOAP services are a type of service where a SOAP message is included, a header with information that allows you to track and route the SOAP message.

Information about:

Message ID - message identifier, used to maintain the relationship between messages that are exchanged.  
Recipient URI  
Source URI - indicates where the message is from  
Reply URI - indicates where the message should be answered (if necessary)  
Failure URI - indicates where to send a message when the service fails.  
Action: contains semantics that indicates how to process the message

### [WSAddressing Properties](#WSAddressing+Properties+)

|  |  |
| --- | --- |
| To | Character |
| Action | Character |
| MessageID | Character |
| From | WSAddressingEndPoint |
| ReplyTo | WSAddressingEndPoint |
| FaultTo | WSAddressingEndPoint |

### [WSAddressingEndPoint Properties](#WSAddressingEndPoint+Properties+)

|  |  |
| --- | --- |
| Address | Character |
| PortType | Character |
| ServiceName | Character |
| Properties | Character |
| Parameters | Character |

### [Sample](#Sample)

```
&location = getLocation("EObjectName")
&wsaddressing.Action = "urn:antel:mdm:system:epagos:b2b:comercio:iniciarSolicitud"
&wsaddressing.MessageID = "uuid:e5403230-9bab-4152-a2ba-e4e47165f135"
&wsaddressing.To = "urn:antel:mdm:system:epagos"
&wsaddressing.From = &wsaddressingendpoint
&wsaddressing.ReplyTo = &otherwsadressingendpoint
&location.WSAddressing = &wsaddressing
```

### [Availability](#Availability)

This property is available since [GeneXus 16 upgrade 4](https://wiki.genexus.com/commwiki/wiki?42755,,).

### [Scope](#Scope)

**Objects:** [Procedures](https://wiki.genexus.com/commwiki/wiki?6293), [Web Panel object](https://wiki.genexus.com/commwiki/wiki?6916)  
**Languages:** Java

[Locations](https://wiki.genexus.com/commwiki/wiki?6981)
