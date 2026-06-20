---
title: "Dynamic Services URL property"
source_id: 20366
source_url: https://wiki.genexus.com/commwiki/wiki?20366
genexus_version: "18"
---

# Dynamic Services URL property

Indicates if GeneXus generates the server URL in the code or if it is dynamic and can be set at runtime.

### [Values](#Values)

|  |
| --- |
| **False** |
| **True** |

### [Scope](#Scope)

**Level:** Front end

### [Description](#Description)

A common scenario in mobile applications is that the server where the app gets the data is given by the end-user, so the Services URL can be changed at runtime.

**Possible values**

* **False:** GeneXus generates the server URL in the code, and it doesn't allow the end-user to change this value because it is embedded in the binary file. This is the default value.

Note that if the Dynamic Services URL property = False but the [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) is blank, the end-user will be asked to enter its value anyway.

* **True:** GeneXus will allow the end-user to change the server URL. The way to change the URL depends on the Operating System on which the device is running.

Note that if the value of the property is set to True, the [Services URL Configuration Panel property](https://wiki.genexus.com/commwiki/wiki?49768) will be displayed.

**Note for Apple:** Take into account that the URLs entered by the end-user must comply with [App Transport Security property group](https://wiki.genexus.com/commwiki/wiki?29368).

### [See Also](#See+Also)

[Services URL property](https://wiki.genexus.com/commwiki/wiki?21146)  
[Services URL Configuration Panel property](https://wiki.genexus.com/commwiki/wiki?49768)


|  |
| --- |
| **Backlinks** |
| [HowTo: Change the URL Services of a Native Mobile application](https://wiki.genexus.com/commwiki/wiki?16159) | [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) |
| [Network external object](https://wiki.genexus.com/commwiki/wiki?31310) | [Services URL Configuration Panel property](https://wiki.genexus.com/commwiki/wiki?49768) | [Services URL property](https://wiki.genexus.com/commwiki/wiki?21146) |

---
