---
title: "Error Codes and Messages for Location Data Type"
source_id: 7106
source_url: https://wiki.genexus.com/commwiki/wiki?7106
genexus_version: "18"
---

# Error Codes and Messages for Location Data Type

### [Error Codes at Client](#Error+Codes+at+Client)

|  |  |  |
| --- | --- | --- |
| **Code** | Message | Comments |
| 0 | No error | There was no error. |
| Greater than 0 and lower than 10000 | Name of parameter N different from expected | A parameter returned by the server does not have the expected name. The error code indicates the position of the parameter causing the conflict. |
| Lower than 0 and greater than –10000 |  | An error occurred upon interpreting the XML response.  This will happen when the response is not XML or if it is not a well formed XML. If we take the error code's absolute value, the result will correspond to an error code of the XMReader object. Anyway, getSOAPErrMsg() will return a description of the error. |
| Lower than  -10000 |  | An error occurred in the HTTP communication. If we take the error code's absolute value and subtract 10000 from it, the result will correspond to an error code of the HTTPClient object. Anyway, getSOAPErrMsg() will return a description of the error. |
| -20001 | Malformation of SOAP message | The response received is a valid XML, but it is not a valid SOAP message. |
| -20004 |  | The server returned that an error occurred in the SOAP request made by client. In this case, getSOAPErrMsg() will return a message containing the code and the error message returned by the server. If the server is a GeneXus procedure or report, it will return some of the error codes described below. |
| -20006 |  | A unidentified error occurred. In this case, getSOAPErrMsg() will return a message containing the code and the error message returned by the server. |
| -20007 | Invalid location name | Invalid location name. This occurs when the GetLocation(*Name*) function is called with a location name that is not defined for any object in the KB. |

[HTTPClient debug in Java](https://wiki.genexus.com/commwiki/wiki?24170,,)

### Error Codes at Server

|  |  |  |
| --- | --- | --- |
| **Code** | Message | Comments |
| -20000 |  | No SOAP message was received. |
| -20001 | Malformed SOAP message | The message received is a valid XML but it is not a valid SOAP message (same as in client). |
| -20002 |  | The called method is not the expected one. (The SOAP method of the GeneXus objects is always called “Execute”). |


|  |
| --- |
| **Backlinks** |
| [GetSOAPErr function](https://wiki.genexus.com/commwiki/wiki?7021) | [GetSOAPErrMsg function](https://wiki.genexus.com/commwiki/wiki?7022) |

---
