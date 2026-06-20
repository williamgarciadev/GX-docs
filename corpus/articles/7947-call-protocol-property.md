---
title: "Call protocol property"
source_id: 7947
source_url: https://wiki.genexus.com/commwiki/wiki?7947
genexus_version: "18"
---

# Call protocol property

Defines how the object is invoked and its output.

### [Values](#Values)

|  |  |
| --- | --- |
| **Command Line** | Allows objects to be executed by command line only. When calling a command line object, the supported input parameters are basic data types (they cannot be Collection, Vector, or Matrix), except for Bitmap and GUID data types. Output parameters are not supported. |
| **Enterprise Java Bean** | When Java is the selected generator, Procedures, Data Providers and Business Component Transactions can apply this value in the property. By setting this value, this object will be automatically implemented as a session bean (stateless) and also as message-driven beans. |
| **HTTP** | Generates objects callable via the HTTP protocol, and allows adding information in the HTTP Response using HttpResponse data type. |
| **Internal** | Usual call type used for objects in GeneXus. This is the default value. |
| **SOAP** | Generates objects to be called via SOAP protocol. It is a particular case of HTTP type. These objects are known as Web Services. |

### [Scope](#Scope)

**Objects:** [Data Provider](https://wiki.genexus.com/commwiki/wiki?5270), [Procedure](https://wiki.genexus.com/commwiki/wiki?6293), [Transaction](https://wiki.genexus.com/commwiki/wiki?1908)  
**Generators:** [Java](https://wiki.genexus.com/commwiki/wiki?12258), [.NET](https://wiki.genexus.com/commwiki/wiki?49815,,), [.NET Core](https://wiki.genexus.com/commwiki/wiki?49825,,)

### [Description](#Description)

#### [Internal](#Internal)

Input parameters: Parameters come instanced by each generator's usual mechanism.  
Output parameters: Parameters are returned through each generator's usual mechanism.

#### [HTTP](#HTTP)

Input parameters: Parameters come after the question mark '?' in the URL used to invoke the object through HTTP.  
Output parameters: Parameters are not returned.  
Output: HTTP response content.

#### [Command Line](#Command+Line)

Note that Command line limits vary widely with the operating system. Some examples are: Linux / UNIX / BSD.

Input parameters: Space-separated parameters following the name of the executable.  
Output parameters: Parameters are not returned.  
Output: Standard output.

#### [SOAP](#SOAP)

Input parameters: Parameters come in the Body of the HTTP Request used in the invocation.  
Output parameters: They are returned in the Body of the HTTP Response Body.  
Output: The output is an HTTP Response with the modified parameters in its Body.

#### [Enterprise Java Bean ([EJB](https://wiki.genexus.com/commwiki/wiki?1818))](#Enterprise+Java+Bean+%28wiki%3F1818%2CEJB+EJB%29)

When the object is called with the [Call method](https://wiki.genexus.com/commwiki/wiki?16224), the SESSION BEAN is called synchronously. When the object is called with the [Submit method](https://wiki.genexus.com/commwiki/wiki?24382), the MESSAGE-DRIVEN BEAN is called asynchronously.

Enterprise Java Beans can be called from external objects. The [Expose as Enterprise Java Bean property](https://wiki.genexus.com/commwiki/wiki?8011) must be set in order to expose the GeneXus Procedure as EJB. If the object has its **Call protocol** property = Enterprise Java Bean, by default the object can be called from GeneXus objects and from external objects automatically. But if you want to expose it only for external objects, and use the Procedure in GeneXus as a common Procedure, then the **Call protocol** property can keep the Internal value, and the [Expose as Enterprise Java Bean property](https://wiki.genexus.com/commwiki/wiki?8011) = True.

#### [When to configure the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) and **Call protocol** property?](#When+to+configure+the+wiki%3F7407%2CMain%2Bprogram%2Bproperty+Main+program+property+and+Call+protocol+property%3F)

When you want to define a different output than the default (Internal) for an object, you can leave its [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) with the default value (False), and configure the **Call protocol** property according to the output of the Procedure (SOAP, EJB, HTTP). The benefit of doing this is that it reduces the number of main objects in the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

One reason for configuring the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True is to be able to compile the object because it is not in the call tree of any other object of the [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836).

For example, in the case of calling the object as a Web Service (SOAP) or an Enterprise Java Bean from an object of the same Knowledge Base, you do not need to set the object as a main program; you just need to set the **Call protocol** property to the corresponding value.  
The same happens to PDF reports, which do not need to be declared as main objects.

Likewise, in order to expose a Web Service or Enterprise Java Bean to be called from outside the Knowledge Base, there is no need to configure the Main Program property, but to configure the [Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480) or the [Expose as Enterprise Java Bean property](https://wiki.genexus.com/commwiki/wiki?8011), respectively.

**Note:**In the case of command line Procedures, it is necessary to configure the [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) = True, in all cases.

If a Procedure has its [Expose as Web Service property](https://wiki.genexus.com/commwiki/wiki?36480) = True and the value of its **Call protocol** property isn't SOAP the internal call from a GeneXus object is not via SOAP but internal. Configure its **Call Protocol** property= SOAP if you want that.

**Important:** There is no support for a Procedure with **Call protocol = HTTP** and SOAP Protocol = True.

### [Runtime/Design time](#Runtime%2FDesign+time)

This property applies only at design-time.

### [See Also](#See+Also)

[What is EJB](https://wiki.genexus.com/commwiki/wiki?2076,,)  
[What is J2EE](https://wiki.genexus.com/commwiki/wiki?2003,,)  
[HowTo: Download a file using HTTP Protocol](https://wiki.genexus.com/commwiki/wiki?14144)  
[HttpResponse data type](https://wiki.genexus.com/commwiki/wiki?6934)


|  |
| --- |
| **Backlinks** |
| [AddHeader method](https://wiki.genexus.com/commwiki/wiki?7064) | [AddString method](https://wiki.genexus.com/commwiki/wiki?7063) | [Category:API object](https://wiki.genexus.com/commwiki/wiki?46151) |
| [KB:BitBitNews](https://wiki.genexus.com/commwiki/wiki?39308) | [Cancel caller execution on error property](https://wiki.genexus.com/commwiki/wiki?36669) | [DBConnection Data Type](https://wiki.genexus.com/commwiki/wiki?6923) | [Deploy a command-line procedure to Docker containers](https://wiki.genexus.com/commwiki/wiki?51121) |
| [Docker base image property](https://wiki.genexus.com/commwiki/wiki?37047) | [Expose as Enterprise Java Bean property](https://wiki.genexus.com/commwiki/wiki?8011) | [GAM - Automatic Permissions generated by GeneXus (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53950) | [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function](https://wiki.genexus.com/commwiki/wiki?47729) |
| [HowTo: Create a GeneXus Procedure to be deployed as an Azure or AWS Function (GeneXus 18 Upgrade 2)](https://wiki.genexus.com/commwiki/wiki?53875) | [HowTo: Deployment of a Command Line Procedure in Java](https://wiki.genexus.com/commwiki/wiki?55200) | [HowTo: Download a file using HTTP Protocol](https://wiki.genexus.com/commwiki/wiki?14144) | [HowTo: Get the User ID when using chatbots and WhatsApp channel](https://wiki.genexus.com/commwiki/wiki?45850) |
| [HowTo: Integrate a new WhatsApp partner into a GeneXus Chatbot](https://wiki.genexus.com/commwiki/wiki?46271) | [HowTo: Integrate Chatbots using Facebook Messenger](https://wiki.genexus.com/commwiki/wiki?44358) | [HowTo: invoke a main Procedure that uses GAM's API in a Java environment](https://wiki.genexus.com/commwiki/wiki?54205) | [HowTo: Start a Process from an External Application](https://wiki.genexus.com/commwiki/wiki?9988) |
| [HowTo: Upload an image, video, or audio file via an API object](https://wiki.genexus.com/commwiki/wiki?51411) | [Location property](https://wiki.genexus.com/commwiki/wiki?7956) | [Main program property](https://wiki.genexus.com/commwiki/wiki?7407) |
| [PDF Reports](https://wiki.genexus.com/commwiki/wiki?13531) | [PDF Reports (GeneXus 18 Upgrade 3 or prior)](https://wiki.genexus.com/commwiki/wiki?54937) | [PDF Reports (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55935) | [Permission Prefix property](https://wiki.genexus.com/commwiki/wiki?17571) |
| [Permission Prefix property (GeneXus 18 Upgrade 2 or prior)](https://wiki.genexus.com/commwiki/wiki?53928) | [Permission Prefix property (GeneXus 18 Upgrade 5 or prior)](https://wiki.genexus.com/commwiki/wiki?55357) | [Reading and writing chunked responses](https://wiki.genexus.com/commwiki/wiki?55630) | [Runtime external object](https://wiki.genexus.com/commwiki/wiki?33076) |
| [Use native SOAP support in Java](https://wiki.genexus.com/commwiki/wiki?27172) |

---
