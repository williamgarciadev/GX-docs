---
title: "WebSession data type"
source_id: 6321
source_url: https://wiki.genexus.com/commwiki/wiki?6321
genexus_version: "18"
---

# WebSession data type

It enables storing data on a Web server user session. Thus, global variables can be accessed while the session is active.

Web servers allow you to handle the concept of a session. A session is identified by a unique key, which is maintained while the user continues on the site.

The WebSession object can store information that will be visible from any Web object within the active session as if they were variables global to the site.

To use the WebSession object, define a variable of this type and apply the appropriate methods and properties:

### [Properties](#Properties)

|  |
| --- |
| [Id](https://wiki.genexus.com/commwiki/wiki?6809) |

### [Methods](#Methods)

|  |
| --- |
| [Set](https://wiki.genexus.com/commwiki/wiki?6810) |
| [Remove](https://wiki.genexus.com/commwiki/wiki?6811) |
| [Get](https://wiki.genexus.com/commwiki/wiki?6812) |
| [Destroy](https://wiki.genexus.com/commwiki/wiki?6813) |
| [Clear](https://wiki.genexus.com/commwiki/wiki?7084) |

### [Notes](#Notes)

* The session ID is stored on a client cookie, although this is transparent for the developer.
* The WebSession's validity is similar to that of cookies; i.e. they are valid only for the session. If a new browser instance is opened, the session is lost, but if it is opened on a new window, the session is kept.
* A session's data and ID are different for each generator. This implies that it is not possible to link a .NET Web Panel to a Java Web Panel and keep the session values.

### [Id](#Id)

Returns a String which will be the session identifier.

**Syntax**

**&***WebSession***.Id**

**Type Returned**:  
String

### [Set](#Set)

Allows entering once in the active session.

**Syntax**

**&***WebSession***.Set(***Key***,** *Value***)**

**Where**:  
*Key*  
Is the Session key, must be a String

*Value*  
Must be a String

### [Get](#Get)

Returns a string corresponding to the key entered for the session.

**Syntax**

**&***WebSession***.Get(***Key***)**

**Type Returned:**  
String

**Where**:  
*Key*  
Is the Session key, must be a String

### [Remove](#Remove)

Allows removing a session value.

**Syntax**

**&***WebSession***.Remove(***Key***)**

**Where**:  
*Key*  
Is the Session key, and must be a String.

### [Destroy](#Destroy)

Destroys the session contents. Its use is recommended when the user logs out, provided this concept exists in it.

**Syntax**

**&***WebSession***.Destroy()**

### [Scope](#Scope)

|  |  |
| --- | --- |
| **Languages** | Java, .NET, Ruby |
| **Interfaces** | Web |
|  |  |


|  |
| --- |
| **Backlinks** |
| [Clear method](https://wiki.genexus.com/commwiki/wiki?7084) | [ClientStorage external object](https://wiki.genexus.com/commwiki/wiki?31272) | [Data Provider: Input](https://wiki.genexus.com/commwiki/wiki?6292) |
| [Data types list](https://wiki.genexus.com/commwiki/wiki?6779) | [Destroy method](https://wiki.genexus.com/commwiki/wiki?6813) | [Category:Extended data types](https://wiki.genexus.com/commwiki/wiki?6560) | [Get method](https://wiki.genexus.com/commwiki/wiki?6812) |
| [GetString method](https://wiki.genexus.com/commwiki/wiki?8831) | [HowTo: Convert online applications into offline applications](https://wiki.genexus.com/commwiki/wiki?24591) | [HowTo: Deploy mobile services to AWS Serverless using AWS Lambda and AWS API Gateway](https://wiki.genexus.com/commwiki/wiki?35355) | [HowTo: Deploy to AWS Lambda Function](https://wiki.genexus.com/commwiki/wiki?51533) |
| [Id property](https://wiki.genexus.com/commwiki/wiki?6809) | [Load balancing considerations](https://wiki.genexus.com/commwiki/wiki?45291) | [Remove method](https://wiki.genexus.com/commwiki/wiki?6811) | [KB:Sales](https://wiki.genexus.com/commwiki/wiki?23672) |
| [Set method](https://wiki.genexus.com/commwiki/wiki?6810) |

---
