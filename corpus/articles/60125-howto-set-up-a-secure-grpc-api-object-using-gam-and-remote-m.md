---
title: "HowTo: Set Up a Secure gRPC API Object using GAM and Remote Modules"
source_id: 60125
source_url: https://wiki.genexus.com/commwiki/wiki?60125
genexus_version: "18"
---

# HowTo: Set Up a Secure gRPC API Object using GAM and Remote Modules

This article presents an example of how to securely expose functionality through an [API object](https://wiki.genexus.com/commwiki/wiki?46151) using the gRPC protocol, with all communications protected by the security layer provided by [GeneXus Access Manager (GAM)](https://wiki.genexus.com/commwiki/wiki?24746).

The example starts from a simple base scenario. A [Knowledge Base](https://wiki.genexus.com/commwiki/wiki?1836) is used that includes an API Object named "APIMovies". This object is configured with the following properties:

* [gRPC Protocol](https://wiki.genexus.com/commwiki/wiki?46381) = True
* [REST Protocol](https://wiki.genexus.com/commwiki/wiki?37254) = False
* [Integrated Security Level](https://wiki.genexus.com/commwiki/wiki?15214) = Authentication

The API Object is located within a module named **ModuleMovies**.

`[imagen omitida: wiki id 60126]`

Right-clicking on the API Object and selecting the **Run** option from the context menu opens a user interface where the API object can be tested using the gRPC protocol.

In this interface, you can select values such as **Service Name** and **Method Name**.  
Within the **Metadata** section, you must include the **Authorization header**, since the service is secured and requires authentication.

`[imagen omitida: wiki id 60127]`

Using GAM for security in the context of the gRPC protocol is quite similar to using it for other other service types. To obtain the access token, refer to the following documentation:

* [HowTo: Develop Secure REST Web Services in GeneXus](https://wiki.genexus.com/commwiki/wiki?15918)
* [HowTo: Use Postman to access secure REST services defined via API Objects](https://wiki.genexus.com/commwiki/wiki?50055)

By clicking on the **Invoke** button, the request is executed and the following screen is displayed containing a successful response.

`[imagen omitida: wiki id 60128]`

**Note**: The service is running on localhost using port 5001, which is the default for .NET applications.

If, for any reason, the gRPC UI does not appear, keep in mind that when the API Object is executed, a Kestrel server window and/or grpcui.exe should open, as shown in the image below. These windows provide additional details that can help identify any errors that may have occurred during execution.

**Important:** **Do not close these windows, as they are required for the testing session to continue.**

`[imagen omitida: wiki id 60129]`

### [Next Step: Publishing the Module](#Next+Step%3A+Publishing+the+Module)

The next step is to [publish the module](https://wiki.genexus.com/commwiki/wiki?46751).

In this case, the module will be published **locally**.

`[imagen omitida: wiki id 60130]`

### [Installing the Module in a New Knowledge Base](#Installing+the+Module+in+a+New+Knowledge+Base)

In a new Knowledge Base, go to the main menu and select [Manage Module References](https://wiki.genexus.com/commwiki/wiki?40172).  
Choose the **Local** option to install the previously published module.

`[imagen omitida: wiki id 60131]`

### [Consuming the Remote API from the New Knowledge Base](#Consuming+the+Remote+API+from+the+New+Knowledge+Base)

In the new Knowledge Base, create a [Procedure object](https://wiki.genexus.com/commwiki/wiki?6293) with the following properties:

* [Main program](https://wiki.genexus.com/commwiki/wiki?7407) = True
* [Call protocol](https://wiki.genexus.com/commwiki/wiki?7947) = Command line

Then, add the following code in the [Procedure Source](https://wiki.genexus.com/commwiki/wiki?6664):

```
// Select Grpc protocol
ModuleMovies.APIMovies.Protocol= GeneXus.Protocol.Grpc

// Setup location, including access token
&location.Host ="localhost"
&location.Port = 5001
&location.Secure = 1
&location.AccessToken = "526b55c9-168c-48e6-887d-ada1192b84da!KcRNHyw6ZFXBF8s2QlMuArdkjL4wGvK29po4cIoP0nt4IHHBJbw7HALsbG7M9ZByvA8QYj1nIKif37"
ModuleMovies.APIMovies.Location= &location

// Remote call
ModuleMovies.MoviesList(&SDTMovies)
Msg(&SDTMovies.ToJson(), status)
```

When executing the procedure directly, the expected response from the remote API is displayed in the output — specifically, a list of movies.

`[imagen omitida: wiki id 60132]`

### [Scope](#Scope)

**Generators:** [.NET](https://wiki.genexus.com/commwiki/wiki?38604)

### [Availability](#Availability)

This feature is available since [GeneXus 18 Upgrade 13](https://wiki.genexus.com/commwiki/wiki?59630).


|  |
| --- |
| **Backlinks** |
| [Table of contents:First Steps with API objects](https://wiki.genexus.com/commwiki/wiki?49754) |

---
